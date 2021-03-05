import logging
import re
import time

import jwt
import requests
from flask import request, abort, g

from App.apis.common_return import check_root
from App.apis.jwxt.utils.utils_cumt_id import Ids
from App.ext import redis_client
from App._settings import SecretKey


def encrypt(body):  # 加密算法
    token_dict = {
        'iat': time.time(),
        'data': body
    }
    headers = {
        'alg': "HS256",  # 声明所使用的算法
    }

    jwt_token = jwt.encode(token_dict, SecretKey, algorithm="HS256", headers=headers).decode('ascii')
    return jwt_token


def decrypt(token):  # 解密算法
    if token is None:
        return False
    try:
        data = jwt.decode(token, SecretKey, algorithms=['HS256'])
        return data
    except Exception as e:
        logging.info(e)
        return False


def login_required(fun):  # 装饰器用，验证token，读取缓存，验证缓存，实现登录
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        if token is None:
            abort(401)
        info = decrypt(token)
        if info == 'error':
            abort(401)
        username = info['data']['username']
        password = info['data']['password']
        g.test = False
        if check_root(username, password):
            g.test = True
            return fun(*args, **kwargs)
        if check_cook(username):  # 如果有cookie，且cookie可用，则直接返回cookie
            g.cook = str(redis_client.get(username), encoding='utf-8')
            g.is_cook = True
            # print("cookie使用完成", username)
            return fun(*args, **kwargs)
        else:
            id = Ids(username, password)  # cookie不行，直接重新登录，获取cookie，然后返回cookie
            data = id.login()
            if data is None:
                abort(401)
            g.cook = str(redis_client.get(username), encoding='utf-8')
            g.is_cook = True
            # print("登录操作", username)
            return fun(*args, **kwargs)
    return wrapper


def check_cook(username):  # cookie可以返回True，不行返回False
    if redis_client.get(username):  # 有cookie
        # print("存在cookie", username)
        if get_test(username):  # 验证cookie是否可用
            # print("cookie可用", username)
            return True
        else:
            # print("cookie过期,重新登录", username)
            return False
    else:
        return False


def get_test(username):  # 验证cookie是否可用
    url = 'http://jwxt.cumt.edu.cn/jwglxt/xtgl/index_cxYhxxIndex.html?xt=jw'
    headers = {
        "Cookie": redis_client.get(username)
    }
    r = requests.get(url=url, headers=headers)
    if r.text.__sizeof__() >= 5000:  # 正确返回1336 错误返回34002
        return False
    else:
        return True


def check_captcha(username):
    url = 'http://ids.cumt.edu.cn/authserver/needCaptcha.html?username=' + username + '&_=' + str(int(time.time()))

    r = requests.get(url=url)
    if 'true' in r.text:
        return True
    else:
        return False
