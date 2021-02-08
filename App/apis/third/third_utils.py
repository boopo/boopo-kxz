import base64
import time

import jwt
import requests
from bs4 import BeautifulSoup

from App._settings import ThirdSecretKey


def token_generator(username, password):
    body = {
        "username": username,
        "password": password
    }
    headers = {
        'alg': "HS256",  # 声明所使用的算法
    }

    jwt_token = jwt.encode(body, ThirdSecretKey, algorithm="HS256", headers=headers).decode('ascii')
    return '<' + username + '>' + jwt_token


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}


class ThirdIds():
    def __init__(self, username, password):
        self.err = []
        self.username = username
        self.password = password
        self.session = requests.session()

    def login(self):
        r = self.session.get(
            url='http://ids.cumt.edu.cn/authserver/login?service = http%3A%2F%2Fmy.cumt.edu.cn%2Flogin.portal',
            headers=headers)
        # print('第一次GET',r.status_code)
        text = r.text
        soup = BeautifulSoup(text, 'html5lib')
        lt = soup.find('input', {'name': 'lt'})['value']
        execution = soup.find('input', {'name': 'execution'})['value']
        From_Data = {  # 表单
            'username': self.username,
            'password': self.password,
            'lt': lt,
            'execution': execution,
            '_eventId': 'submit',
            'rmShown': '1',
            'signln': ''
        }
        self.err.append(From_Data)
        q = self.session.post(
            url='http://ids.cumt.edu.cn/authserver/login?service = http%3A%2F%2Fmy.cumt.edu.cn%2Flogin.portal',
            data=From_Data, headers=headers, allow_redirects=False)
        self.err.append(q.status_code)
        if q.status_code == 302:
            self.cookies = q.cookies
            #    print('第二次POST',q.cookies)
            text = q.headers['Location']
            s = self.session.get(url=text)
            #    print('第三次GET',s.status_code)

            a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
            _data = {
                'xnm': '2020',
                'xqm': '1',
            }
            return True
        if q.status_code == 200:
            return False

    # 此模块实现了验证码的自动识别并提交
    def login_pro(self):
        _r = self.session.get(
            url='http://ids.cumt.edu.cn/authserver/login?service = http%3A%2F%2Fmy.cumt.edu.cn%2Flogin.portal',
            headers=headers)
        text = _r.text
        soup = BeautifulSoup(text, 'html5lib')
        lt = soup.find('input', {'name': 'lt'})['value']
        execution = soup.find('input', {'name': 'execution'})['value']
        _url = 'http://ids.cumt.edu.cn/authserver/captcha.html'
        _rs = self.session.get(url=_url)
        _rs_data = base64.b64encode(_rs.content)
        _rs_data_base64 = _rs_data.decode()
        # print("base64", _rs_data_base64)
        _data = get_captcha_code(_rs_data_base64)
        # print("验证码为", _data)
        From_Data = {
            'username': self.username,
            'password': self.password,
            'lt': lt,
            'execution': execution,
            '_eventId': 'submit',
            'rmShown': '1',
            'signln': '',
            'captchaResponse': _data
        }
        self.err.append(From_Data)
        q = self.session.post(
            url='http://ids.cumt.edu.cn/authserver/login?service = http%3A%2F%2Fmy.cumt.edu.cn%2Flogin.portal',
            data=From_Data, headers=headers, allow_redirects=False)
        self.err.append(q.status_code)
        if q.status_code == 302:
            self.cookies = q.cookies
            #    print('第二次POST',q.cookies)
            text = q.headers['Location']
            s = self.session.get(url=text)
            #    print('第三次GET',s.status_code)

            a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
            _data = {
                'xnm': '2020',
                'xqm': '1',
            }
            return True
        else:
            return False

    def get_self_info(self):  # 只爬到一个html，emmm。。。
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
        form_data = {
            'gndm': 'N100801'
        }

        a = self.session.post(
            'http://jwxt.cumt.edu.cn/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default',
            data=form_data)
        a.encoding = a.apparent_encoding
        # r = re.findall('<p class="form-control-static">(.*?)</p>',a.text) 只可返回姓名
        soup = BeautifulSoup(a.text, 'html5lib')
        x = soup.find_all('p', class_='form-control-static')
        ss = []
        data = []
        for a in x:
            data.append(a.string)
        #  格式是固定的
        ss.append(data[1])  # 姓名
        ss.append(data[24][7:-4])  # 学院
        ss.append(data[26][7:-4])  # 年级
        ss.append(data[28][7:-4])  # 班机
        ss.append(data[7][7:-4])  # 性别
        return ss


def t_check_captcha(username):
    url = 'http://ids.cumt.edu.cn/authserver/needCaptcha.html?username=' + username + '&_=' + str(int(time.time()))
    r = requests.get(url=url)
    if 'true' in r.text:
        return True
    else:
        return False


def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=avCnCK6HjFTcneeTWhlOsnzy&client_secret=v0XE79GT9nsHpmnd5nRwNVVPfTndwgqz'
    r = requests.post(url=url)
    if r.status_code == '200':
        secret = r.json()['session_key']
        return secret


def get_captcha_code(image_base64):
    access_token = '24.206fcbd2838aa199b358948770fdb5ca.2592000.1612714667.282335-23122968'
    url_ocr = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
    _headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'image': image_base64
    }
    ocr_data = requests.post(url=url_ocr, data=body, headers=_headers)
    if ocr_data.status_code == 200:
        print("ok")
        return ocr_data.json()['words_result'][0]['words'].replace(" ", "")
    else:
        return False
