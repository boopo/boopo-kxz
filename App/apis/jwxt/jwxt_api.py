from flask import g
from flask_restful import reqparse, Resource

from App.apis.api_constant import data_error
from App.apis.jwxt.utils import encrypt, marshal_kb, marshal_grade, marshal_exam, marshal_room, marshal_course, \
    login_required
from App.apis.jwxt.cumt_id import Ids

parse_login = reqparse.RequestParser()
parse_login.add_argument("username", type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_login.add_argument("password", type=str, help='请提交正确的参数Key', required=True, location=['json'])

parse_info = reqparse.RequestParser()
parse_info.add_argument("xnm", type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_info.add_argument("xqm", type=str, help='请提交正确的参数Key', required=True, location=['args'])


parse_base = reqparse.RequestParser()
parse_base.add_argument("xnm", type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_base.add_argument("xqm", type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_base.add_argument("week", type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_base.add_argument("weekday", type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_base.add_argument("section", type=str, help='请提交正确的参数Key', required=True, location=['json'])

parse_room = parse_base.copy()
parse_room.add_argument('build', type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_room.add_argument('section', type=str, help='请提交正确的参数Key', required=True, location=['json'])

parse_class = parse_base.copy()
parse_class.add_argument('_id', type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_class.add_argument('teacher', type=str, help='请提交正确的参数Key', required=True, location=['json'])


login_error = {
    "code": 1,
    "data": "null",
    "msg": "登录失败,请检查你的用户名或密码！"
}


class Login(Resource):
    def post(self):
        args = parse_login.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            id = Ids(username, password)
            data = id.login()
            info = {
                "username": username,
                "password": password
            }
            token = encrypt(info)
            info = id.get_self_info()
            info.update({"token": token})
            if data:
                return {
                    "code": 0,
                    "data": info,
                    "msg": "登录成功"
                }
            else:
                return login_error
        except Exception as e:
            print(e)
            return login_error


class KB(Resource):
    @login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')

        try:
            data = g.id.get_kblist(xnm, xqm)
            pre_data = marshal_kb(data)

            if data is not None:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": pre_data
                }
        except Exception as e:
            print(e)
            return data_error


class Grades(Resource):
    @login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')

        try:
            data = g.id.get_grade(xnm, xqm)
            pre_data = marshal_grade(data)

            if data:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": pre_data
                }
        except Exception as e:
            print(e)
            return data_error


class Exams(Resource):
    @login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')

        try:
            data = g.id.get_exam(xnm, xqm)
            pre_data = marshal_exam(data)

            if data:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": pre_data
                }
        except Exception as e:
            print(e)
            return data_error


class SingleJd(Resource):
    @login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')

        try:
            data = g.id.get_single_jd(xnm, xqm)
            print(data)
            if data:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": data
                }
        except Exception as e:
            print(e)
            return data_error


class AverageJd(Resource):
    @login_required
    def get(self):
        try:
            data = g.id.get_average_jd()
            print(data)
            if data:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": data
                }
        except Exception as e:
            print(e)
            return data_error


class EmptyRoom(Resource):
    @login_required
    def post(self):
        args = parse_room.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        build = args.get('build')
        section = args.get('section')
        week = args.get('week')
        weekday = args.get('weekday')
        try:
            data = g.id.get_empty_room(xnm, xqm, build, section, week, weekday)
            msg = marshal_room(data)
            if data:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": msg
                }
        except Exception as e:
            print(e)
            return data_error


class SpecialCourse(Resource):
    @login_required
    def post(self):
        args = parse_class.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        _id = args.get('_id')
        weekday = args.get('weekday')
        week = args.get('week')
        section = args.get('section')
        teacher = args.get('teacher')
        try:
            data = g.id.get_special_course(xnm, xqm, _id, weekday, week, section, teacher)
            msg = marshal_course(data)
            if data['items']:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": msg
                }
        except Exception as e:
            print(e)
            return data_error
