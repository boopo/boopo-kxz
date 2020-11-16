import jwt
from flask import g, request
from flask_restful import abort

from App.apis.jwxt.utils.utils_cache import decrypt
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



