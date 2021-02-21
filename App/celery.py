from time import sleep, time

import requests
from bs4 import BeautifulSoup
from celery import Celery
from flask import current_app

from App.apis.new_login.utils.utils_encry import get_token
from App.ext import redis_client

celery_app = Celery(__name__)

url_login = 'http://authserver.cumt.edu.cn/authserver/login?service=http%3A//portal.cumt.edu.cn/casservice'  # 登录
url_post = 'http://authserver.cumt.edu.cn/authserver/login?service=http%3A%2F%2Fportal.cumt.edu.cn%2Fcasservice'  # 提交表单
url_balance_re1 = 'http://ykt.cumt.edu.cn:8088/ias/prelogin?sysid=FWDT'  # 一卡通跳转1
url_balance_re2 = 'http://ykt.cumt.edu.cn/cassyno/index'  # 一卡通跳转2
url_library_re = 'http://121.248.104.188:8080/CASSSO/login.jsp'  # 图书馆认证跳转

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}


class newIds_delay:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

    def login(self):
        r = self.session.get(url=url_login, headers=headers)
        soup = BeautifulSoup(r.text, 'html5lib')
        salt = soup.find('input', id='pwdEncryptSalt')['value']
        execution = soup.find('input', id='execution')['value']
        # 密码加密
        salt_pwd = get_token(self.password, salt)
        form_login = {
            'username': self.username,
            'password': salt_pwd,
            '_eventId': 'submit',
            'cllt': 'userNameLogin',
            'execution': execution
        }
        r1 = self.session.post(url=url_post, data=form_login, headers=headers, allow_redirects=False)
        if r1.status_code == 302:
            url_re = r1.headers['Location']
            r2 = self.session.get(url=url_re)
            #    SESS l1[0]
            # 用SEES拿到hall和jwt
            try:
                r3 = self.session.get(url=url_balance_re1, headers=headers)
                hall_soup = BeautifulSoup(r3.text, 'html5lib')
                token = hall_soup.find('input', id='ssoticketid')['value']
                form_hall = {
                    "errorcode": 1,
                    "continueurl": '',
                    "ssoticketid": token
                }
                # hall l1[7]
                r4 = self.session.post(url=url_balance_re2, headers=headers, data=form_hall)
                # jwt  r8.headers['Location'][43:-12]
                r5 = self.session.get(url=url_library_re, headers=headers, allow_redirects=False)
                r6 = self.session.get(url=r5.headers['Location'], headers=headers, allow_redirects=False)
                r7 = self.session.get(url=r6.headers['Location'], headers=headers, allow_redirects=False)
                r8 = self.session.get(url=r7.headers['Location'], headers=headers, allow_redirects=False)
                l1 = []
                for a in self.session.cookies:
                    l1.append(a.value)
                cookie_list = {
                    "sess": l1[0],
                    "hall": l1[8],
                    "jwt": r8.headers['Location'][43:-12]
                }
                set_sso_token(self.username, cookie_list)
                print(cookie_list)
                return True
            except Exception as e:
                print(e)
                return False


def set_sso_token(username, mapping):
    try:
        redis_client.hmset(name='new' + username, mapping=mapping)
        return True
    except Exception as e:
        print(e)
        return False




@celery_app.task
def new_login():
    print("oooooo")
    sleep(3)
    from App.ext import redis_third
    redis_third.set(name="celery", value="异步操作")
    return "okk"

@celery_app.task()
def new_id_login(username, password):
    a = time()
    print("正在异步调用")
    print(username+password)
    user = newIds_delay(username,password)
    if user.login():
        print("成功")
    else:
        print("失败")
    b = time()
    print("用时")
    print(b-a)
    return "ok"



