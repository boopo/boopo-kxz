import time

import requests
from bs4 import BeautifulSoup

from App.ext import redis_client, db
from App.models import User

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}


class Pids():
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
            coo = self.session.cookies
            l1 = []
            for single in coo:
                l1.append(single.value)
            try:
                redis_client.set(name=self.username, value='JSESSIONID=' + l1[3], ex=43200)
                print("redis正常", self.username, l1[3])
                if User.query.filter(User.username.__eq__(self.username)).first() is None:
                    user = User()
                    user.username = self.username
                    user.permission = 2
                    db.session.add(user)
                    db.session.commit()
                    print("新用户", self.username)
            except Exception as e:
                print("redis异常", e)
            return True
        if q.status_code == 200:
            soup_obj = BeautifulSoup(q.text, "html5lib")
            tips = soup_obj.find_all(id="msg")
            span = tips[0].string
            print(span)  # 打印错误原因
            return False


def check_captcha(username):
    url = 'http://ids.cumt.edu.cn/authserver/needCaptcha.html?username=' + username + '&_=' + str(int(time.time()))
    r = requests.get(url=url)
    if 'true' in r.text:
        return True
    else:
        return False
