from flask_restful import reqparse, Resource

from App.apis.third.third_utils import token_generator, ThirdIds, t_check_captcha
from App.ext import redis_third

parse_third = reqparse.RequestParser()
parse_third.add_argument("username", type=str, help='请输入学号', required=True, location=['json'])
parse_third.add_argument("password", type=str, help='请输入密码', required=True, location=['json'])

parse_captcha = parse_third.copy()
parse_captcha.add_argument("")

class ThirdPartyLogin(Resource):
    def post(self):
        try:
            args = parse_third.parse_args()
            username = args.get('username')
            password = args.get('password')
            if t_check_captcha(username):
                return {
                    "msg": "需要验证码",
                    "data": ''
                }, 403
            id = ThirdIds(username, password)
            if id.login():
                _token = token_generator(username, password)
                redis_third.set(name=username, value=_token)
                l1 = id.get_self_info()
                d1 = {
                    "name": l1[0],
                    "college": l1[1],
                    "classname": l1[3],
                    "token": _token
                }
                return {
                    "msg": "登陆成功",
                    "data": d1
                }
            else:
                return {
                    "msg": "用户名或密码错误",
                    "data": ""
                }, 401
        except Exception as e:
            print(e)
        return {
                "msg": "认证失败，请重试",
                "data": ""
        }, 500

'''
class LoginCaptcha(Resource):
    def get(self):
        try:
            args = parse_captcha.parse_args()
            username = args.get('username')
            password = args.get('password')
            captcha = args.get('captcha')
            return {
                "msg": "test"
            }
        except Exception as e:
            print(e)
            return {
               "msg": "error"
            }
'''