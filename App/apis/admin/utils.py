import time

import jwt
import requests
from flask import g, request
from flask_restful import abort

from App.apis.jwxt.utils.utils_cache import decrypt
from App.ext import redis_client
from App.models import User


def get_username():
    token = request.headers.get('token')
    if token is None:
        abort(401)
    info = decrypt(token)
    if info == 'error':
        abort(401)
    username = info['data']['username']

    user = User.query.filter(User.username.__eq__(username)).first()
    g.user = user


def require_permission(permission):
    def require_permission_wrapper(fun):
        def wrapper(*args, **kwargs):
            get_username()
            if not g.user.check_permission(permission):
                abort(403, msg='permission not allowed')
            return fun(*args, **kwargs)

        return wrapper

    return require_permission_wrapper


def set_version(mapping):
    #  redis_client.set(name=self.username, value='JSESSIONID='+l1[3], ex=43200)
    #  str(redis_client.get(username), encoding='utf-8')
    try:
        redis_client.hmset(name='apk', mapping=mapping)
        return True
    except Exception as e:
        print(e)
        return False


def get_version(key):
    try:
        l1 = ['version', 'upgrade', 'url', 'desc']
        a = redis_client.hmget(name='apk', keys=l1)
        l1 = [str(a[0], encoding='utf-8'), str(a[1], encoding='utf-8'), str(a[2], encoding='utf-8'),
              str(a[3], encoding='utf-8')]
        return l1
    except Exception as e:
        print(e)
        return False



