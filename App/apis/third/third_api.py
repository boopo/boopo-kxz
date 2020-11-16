from flask_restful import reqparse, Resource

from App.apis.third.third_utils import token_generator, ThirdIds
from App.ext import redis_third

parse_third = reqparse.RequestParser()
parse_third.add_argument("username", type=str, help='请输入学号', required=True, location=['json'])
parse_third.add_argument("password", type=str, help='请输入学号', required=True, location=['json'])


class ThirdPartyLogin(Resource):
    def post(self):
        try:
            args = parse_third.parse_args()
            username = args.get('username')
            password = args.get('password')
            id = ThirdIds(username, password)
            if id.login():
                _token = token_generator(username, password)
                redis_third.set(name=username, value=_token)
                return {
                    "status": 200,
                    "msg": "ok",
                    "data": _token
                }
            else:
                return {
                    "status": 401,
                    "msg": "用户名或密码错误",
                    "data": "null"
                }
        except Exception as e:
            print(e)
        return {
            "status": 404,
            "msg": "未知错误",
            "data": "null"
        }
