import logging

from flask import g
from flask_restful import Resource, reqparse

from App.apis.api_constant import login_response, data_response
from App.apis.common_return import check_root, testUser
from App.apis.jwxt.utils.utils_cache import encrypt
from App.apis.new_login.utils.utils_cache import new_login_required
from App.apis.new_login.utils.utils_data_processing import marshal_simple_balance, marshal_simple_library, \
    marshal_simple_balance_history
from App.apis.new_login.utils.utils_new_id import newIds
from App.apis.new_login.utils.utils_request import get_balance_simple, get_library_simple, get_balance_history_simple

parse_new_login = reqparse.RequestParser()
parse_new_login.add_argument("username", type=str, help='用户名不能为空!', required=True, location=['json'])
parse_new_login.add_argument("password", type=str, help='密码不能为空!', required=True, location=['json'])


class newLogin(Resource):
    def post(self):
        args = parse_new_login.parse_args()
        user_name = args.get("username")
        username = user_name.strip()
        password = args.get("password")
        if check_root(username, password):
            return testUser.newlogin_return()
        try:
            # 这里会更新验证码填充功能
            user = newIds(username, password)
            u_login = user.login()
            if u_login:
                data = user.login_with_self_info()
                data.update({"token":encrypt({"username": username, "password": password})})
                return login_response(0, '登陆成功',data)
            else:
                return login_response(1, '登录失败,请检查用户名或密码', 'null', 200)

        except Exception as e:
            logging.info(e)
            return login_response(1, e, 'null', 404)


class simpleBalance(Resource):
    @new_login_required
    def get(self):
        try:
            if g.test:
                return testUser.simpleBalance_return()
            if g.is_cook:
                data = get_balance_simple(g.portal_cook)
                msg = marshal_simple_balance(data)
                return data_response(200, '请求成功', msg)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')


class simpleLibrary(Resource):
    @new_login_required
    def get(self):
        try:
            if g.test:
                return testUser.simplelibrary_return()
            if g.is_cook:
                data = get_library_simple(g.portal_cook)
                msg = marshal_simple_library(data)
                return data_response(200, '请求成功', msg)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')


class simpleBalanceHistory(Resource):
    @new_login_required
    def get(self):
        try:
            if g.test:
                return testUser.simplebalancehistory_return()
            if g.is_cook:
                data = get_balance_history_simple(g.portal_cook)
                msg = marshal_simple_balance_history(data)
                return data_response(200, '请求成功', msg)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')
