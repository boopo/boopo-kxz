import logging
import re

import requests
from bs4 import BeautifulSoup

from App.apis.new_login.utils.utils_encry import get_token
from App.ext import redis_client, db
from App.models import User

url_login = 'http://authserver.cumt.edu.cn/authserver/login?service=http%3A//portal.cumt.edu.cn/casservice'  # 登录
url_post = 'http://authserver.cumt.edu.cn/authserver/login?service=http%3A%2F%2Fportal.cumt.edu.cn%2Fcasservice'  # 提交表单
url_balance_re1 = 'http://ykt.cumt.edu.cn:8088/ias/prelogin?sysid=FWDT'  # 一卡通跳转1
url_balance_re2 = 'http://ykt.cumt.edu.cn/cassyno/index'  # 一卡通跳转2
url_library_re = 'http://121.248.104.188:8080/CASSSO/login.jsp'  # 图书馆认证跳转
url_jwxt_login = 'http://authserver.cumt.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.cumt.edu.cn%2Fsso%2Fjziotlogin' # 教务系统跳转




headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}


class newIds:
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
            try:
                url_re = r1.headers['Location']
                r2 = self.session.get(url=url_re)
                #    SESS l1[0]
                r3 = self.session.get(url=url_jwxt_login, headers = headers,allow_redirects= False)
                if r3.status_code == 302:
                    u1 = r3.headers['Location']
                    r4 = self.session.get(url=u1, headers=headers)
                    l1 = []
                    for a in self.session.cookies:
                        l1.append(a.value)
                    redis_client.set(name=self.username, value="SESS9595b993ee90002d725a39f1284c4520="+l1[0])
                    redis_client.set(name='j'+self.username, value="JSESSIONID="+l1[6])
                    if User.query.filter(User.username.__eq__(self.username)).first() is None:
                        user = User()
                        user.username = self.username
                        user.permission = 2
                        db.session.add(user)
                        db.session.commit()
                        logging.info("新用户"+User.username)
                    return True
                return False
            except Exception as e:
                logging.info("new_login_error" + e)
                return False
        else:
            return False

    def login_with_captcha(self):
        pass

    def login_with_card(self):
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
            try:
                url_re = r1.headers['Location']
                r2 = self.session.get(url=url_re)
                r3 = self.session.get(url= url_balance_re1, headers=headers)
                soup = BeautifulSoup(r3.text, 'html5lib')
                token = soup.find('input', id='ssoticketid')['value']
                form = {
                    "errorcode": 1,
                    "continueurl": '',
                    "ssoticketid": token
                }
                r4 = self.session.post(url=url_balance_re2, headers=headers, data=form)
                l1 = []
                for s in self.session.cookies:
                    l1.append(s.value)
                redis_client.set(name=self.username, value="SESS9595b993ee90002d725a39f1284c4520=" + l1[0])
                redis_client.set(name='y' + self.username, value="hallticket=" + l1[7])

                return True
            except Exception as e:
                logging.info("card_login_error" + e)
                return False
        else:
            return False

    def login_with_lib(self):
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
            try:
                url_re = r1.headers['Location']
                r2 = self.session.get(url=url_re)
                r3 = self.session.get(url=url_library_re, headers=headers, allow_redirects=False)
                r4 = self.session.get(url=r3.headers['Location'], headers=headers, allow_redirects=False)
                r5 = self.session.get(url=r4.headers['Location'], headers=headers, allow_redirects=False)
                r6 = self.session.get(url=r5.headers['Location'], headers=headers, allow_redirects=False)
                if r6.status_code == 302:
                    jwt = r6.headers['Location'][43:-12]
                    l1 = []
                    for a in self.session.cookies:
                        l1.append(a.value)
                    redis_client.set(name=self.username, value="SESS9595b993ee90002d725a39f1284c4520=" + l1[0])
                    redis_client.set(name='l' + self.username, value=jwt)
                    return True
                return False
            except Exception as e:
                logging.info("card_login_error")
                return False
        else:
            return False
        return True

    def login_with_self_info(self):
        url ="http://jwxt.cumt.edu.cn/jwglxt/xtgl/index_cxYhxxIndex.html?xt=jw"
        r = self.session.get(url, headers= headers)
        r.encoding = r.apparent_encoding
        if r.text.__sizeof__() <= 5000:
            name = re.findall('<h4 class="media-heading">(.*?)</h4>', r.text)[0]
            info = re.findall("<p>(.*?)</p>", r.text)[0]

            college = info.split(" ")[0]
            classname =info.split(" ")[1]
            data = {
                "name": name,
                "college": college,
                "classname": classname
            }
            return data
        else:
            return False

