import time

import requests
from flask import request, abort, g

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


# 获取所有cookie
def get_sso_token(username):
    try:
        l1 = ['sess', 'hall', 'jwt']
        a = redis_client.hmget(name='new' + username, keys=l1)
        l2 = [
            'SESS9595b993ee90002d725a39f1284c4520=' + str(a[0], encoding='utf-8'),
            'hallticket=' + str(a[1], encoding='utf-8'),
            str(a[2], encoding='utf-8')
        ]
        return l2
    except Exception as e:
        print(e)
        return False


# 获取融合门户cookie
def get_sess_token(username):
    try:
        a = redis_client.hmget(name='new' + username, keys=['sess'])
        return 'SESS9595b993ee90002d725a39f1284c4520=' + str(a[0], encoding='utf-8')
    except Exception as e:
        print(e)
        return False


# 获取一卡通cookie
def get_hall_token(username):
    try:
        a = redis_client.hmget(name='new' + username, keys=['hall'])
        text = 'hallticket=' + str(a[0], encoding='utf-8')
        return text
    except Exception as e:
        print(e)
        return False


# 获取图书馆cookie
def get_jwt_token(username):
    try:
        a = redis_client.hmget(name='new' + username, keys=['jwt'])
        return str(a[0], encoding='utf-8')
    except Exception as e:
        print(e)
        return False


# 验证sso cookie
def check_sess_cookie(username):
    url = 'http://portal.cumt.edu.cn/portal/api/v1/api/http/8'
    headers = {
        "Cookie": get_sess_token(username)
    }
    r = requests.get(url=url, headers=headers)
    if r.text.__sizeof__() >= 1000:  # 正确 432 错误 75044
        return False
    else:
        return True


def check_hall_cookie(username):
    url = 'http://ykt.cumt.edu.cn/User/GetCardInfo'
    header = {
        "Cookie": get_hall_token(username)
    }
    r = requests.post(url=url, headers=header)
    if r.text.__sizeof__() >= 8888:  # 正确 2020 错误 53642
        return False
    else:
        return True


def check_jwt_cookie(username):
    url = 'https://findcumt.libsp.com/find/userInfo/getUserInfo'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "jwtOpacAuth": get_jwt_token(username)
    }
    r = requests.get(url=url, headers=header)
    if r.text.__sizeof__() <= 1000:  # 正确2726  错误 181
        return False
    else:
        return True


# 验证验证码
def check_captcha(username):
    url = 'http://authserver.cumt.edu.cn/authserver/checkNeedCaptcha.htl?username=' + username + '&_=' + str(
        int(time.time()))
    r = requests.get(url=url)
    if 'true' in r.text:
        return True
    else:
        return False


def new_login_required(fun):  # 装饰器用，验证token，读取缓存，验证缓存，实现登录
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        action = request.headers.get('action')
        if token is None:
            abort(401)
        info = decrypt(token)
        if info == 'error':
            abort(401)
        username = info['data']['username']
        password = info['data']['password']
        g.is_cook = False
        if action == 'card':
            if not check_hall_cookie(username):
                _id = newIds(username, password)
                _id.login()
            g.sess_cook = get_sess_token(username)
            g.hall_cook = get_hall_token(username)
            g.is_cook = True
        if action == 'book':
            if not check_jwt_cookie(username):
                _id = newIds(username, password)
                _id.login()
            g.jwt_cook = get_jwt_token(username)
            g.is_cook = True
        if action == 'index':
            if not check_sess_cookie(username):
                _id = newIds(username, password)
                _id.login()
            g.sess_cook = get_sess_token(username)
            g.is_cook = True

        return fun(*args, **kwargs)
    return wrapper
