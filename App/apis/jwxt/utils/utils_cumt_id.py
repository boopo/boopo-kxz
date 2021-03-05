import base64
import time
import re
import requests
from bs4 import BeautifulSoup

from App._settings import BaiduClientSecret, BaiduClientId

from App.ext import redis_client, db
from App.models import User
from App.utils.captcha import Captcha

session = requests.session()

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}
'''
2021/3/5
此模块失效
'''

# 目前Ids仅用于登录获取 cookie，其他函数已搁置（未完成持久化）
class Ids:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.err = []

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
            coo = self.session.cookies
            l1 = []
            for single in coo:
                l1.append(single.value)
            try:
                redis_client.set(name=self.username, value='JSESSIONID=' + l1[3], ex=83200)
                print("redis正常")
                if User.query.filter(User.username.__eq__(self.username)).first() is None:
                    user = User()
                    user.username = self.username
                    user.permission = 2
                    db.session.add(user)
                    db.session.commit()
                    print("新用户")
            except Exception as e:
                print("redis异常", e)
            return True
        if q.status_code == 200:
            soup_obj = BeautifulSoup(q.text, "html5lib")
            tips = soup_obj.find_all(id="msg")
            span = tips[0].string
            print(span)  # 打印错误原因
            return False

    '''       if span == "您提供的用户名或者密码有误。":
                return False
        else:
            return False
    '''

    # 带验证码的
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
        _rs_data_base64 = base64.b64encode(_rs.content).decode()
        capcha = Captcha(BaiduClientSecret, BaiduClientId, _rs_data_base64)
        _data = capcha.get_result()
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

