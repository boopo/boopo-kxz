import logging
import time

import requests
from flask import request, abort, g

from App.apis.common_return import check_root
from App.apis.jwxt.utils.utils_cache import decrypt
from App.apis.new_login.utils.utils_new_id import newIds
from App.ext import redis_client

'''
# 实现cookie的整体存储，单个读取,过期自动更新
def set_sso_token(username, mapping):
    try:
        redis_client.hmset(name='new' + username, mapping=mapping)
        return True
    except Exception as e:
        print(e)
        return False
'''



class CheckAndGet():
    def __init__(self, username):
        self.username = username
    # 验证融合门户 cookie
    def check_portal_cookie(self):
        url = 'http://portal.cumt.edu.cn/portal/api/v1/api/http/8'
        header = {
            "Cookie": ''
        }
        r = requests.get(url=url, headers=header)
        if r.text.__sizeof__() >= 1000:  # 正确 432 错误 75044
            return False
        else:
            return True

    def check_jwxt_cookie(self):
        url = 'http://jwxt.cumt.edu.cn/jwglxt/xtgl/index_cxYhxxIndex.html?xt=jw'
        header = {
            "Cookie": str(redis_client.get("j"+self.username), encoding='utf-8')
        }
        r = requests.get(url=url, headers=header)
        if r.text.__sizeof__() >= 5000:  # 正确返回1336 错误返回34002
            return False
        else:
            return True

    # 验证一卡通cookie
    def check_card_cookie(self):
        if redis_client.get("y"+self.username):
            url = 'http://ykt.cumt.edu.cn/User/GetCardInfo'
            header = {
                "Cookie": str(redis_client.get("y"+self.username), encoding='utf-8')
            }
            r = requests.post(url=url, headers=header)
            if r.text.__sizeof__() >= 8888:  # 正确 2020 错误 53642
                return False
            else:
                return True
        else:
            return False

    # 验证图书馆cookie
    def check_lib_cookie(self):
        if  redis_client.get("l"+self.username):
            url = 'https://findcumt.libsp.com/find/userInfo/getUserInfo'

            jwt = str(redis_client.get("l"+self.username), encoding='utf-8')
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "jwtOpacAuth": jwt
            }
            r = requests.get(url=url, headers=header)
            if r.text.__sizeof__() <= 1000:  # 正确2726  错误 181
                return False
            else:
                return True
        else:
            logging.info("无jwt")
            return False

    # 验证验证码
    def check_captcha(self):
        url = 'http://authserver.cumt.edu.cn/authserver/checkNeedCaptcha.htl?username=' + self.username + '&_=' + str(
            int(time.time()))
        r = requests.get(url=url)
        if 'true' in r.text:
            return True
        else:
            return False

    def get_portal_cookie(self):
        cookie = str(redis_client.get(self.username), encoding='utf-8')
        return cookie

    def get_jwxt_cookie(self):
        cookie = str(redis_client.get("j"+self.username), encoding='utf-8')
        return cookie


    def get_card_cookie(self):
        cookie = str(redis_client.get("y" + self.username), encoding='utf-8')
        return cookie

    def get_lib_cookie(self):
        cookie = str(redis_client.get("l" + self.username), encoding='utf-8')
        return cookie






def new_login_required(fun):  # 装饰器用，验证token，读取缓存，验证缓存，实现登录
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        action = request.headers.get('action')
        if not decrypt(token):
            abort(401)
        info = decrypt(token)
        username = info['data']['username']
        password = info['data']['password']
        g.test = False
        g.is_cook = False
        if check_root(username, password):
            g.test = True
            return fun(*args, **kwargs)
        user = CheckAndGet(username)
        if action == 'jwxt':
            if not user.check_jwxt_cookie():
                new_user = newIds(username, password)
                new_user.login()
            g.is_cook =True
            g.jwxt_cook = user.get_jwxt_cookie()
        if action == 'index':
            if not user.check_portal_cookie():
                new_user = newIds(username, password)
                new_user.login()
            g.is_cook = True
            g.portal_cook = user.get_portal_cookie()
        if action == 'card':
            if not user.check_card_cookie():
                new_user = newIds(username, password)
                new_user.login_with_card()
            g.is_cook = True
            g.card_cook = user.get_card_cookie()
            g.portal_cook = user.get_portal_cookie()
        if action == 'book':
            if not user.check_lib_cookie():
                new_user = newIds(username, password)
                new_user.login_with_lib()
            g.is_cook = True
            g.lib_cook = user.get_lib_cookie()
        return fun(*args, **kwargs)
    return wrapper
