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
    return '<'+username+'>'+jwt_token


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}


class ThirdIds():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

    def login(self):
        self.err = []
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
            return True
        if q.status_code == 200:
            return False
