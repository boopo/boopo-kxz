import logging

from flask import g
from flask_restful import reqparse, Resource


from App.apis.api_constant import data_error, data_response
from App.apis.common_return import  testUser
from App.apis.jwxt.utils.utils_data_processing import marshal_grade, marshal_exam, marshal_room, \
    marshal_course, marshal_kb, marshal_make_up_gardes
from App.apis.jwxt.utils.utils_request import get_kblist, get_grade, get_exam, get_single_jd, get_average_jd, \
    get_empty_room, get_special_course, get_make_up_grades
from App.apis.new_login.utils.utils_cache import new_login_required

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
parse_class.add_argument('id', type=str, help='请提交正确的参数Key', required=True, location=['json'])
parse_class.add_argument('teacher', type=str, help='请提交正确的参数Key', required=True, location=['json'])


login_error = {
    "code": 1,
    "data": "null",
    "msg": "登录失败,请检查你的用户名或密码！"
}


# class Login(Resource):
#     def post(self):
#         args = parse_login.parse_args()
#         username = args.get("username")
#         password = args.get("password")
#         if check_root(username, password):
#             return testUser.login_return()
#         # 验证码识别
#         try:
#             if check_captcha(username):
#                 id_pro = Ids(username, password)
#                 if id_pro.login_pro():
#
#                     info_pro = {
#                         "username": username,
#                         "password": password
#                     }
#                     token = encrypt(info_pro)
#                     l1_pro = id_pro.get_self_info()
#                     d1_pro = {
#                         "name": l1_pro[0],
#                         "college": l1_pro[1],
#                         "classname": l1_pro[3],
#                         "token": token
#                     }
#                     info_pro.update({"token": token})
#                     return {
#                             "code": 0,
#                             "data": d1_pro,
#                             "msg": "登录成功"
#                         }
#                 else:
#                     return {
#                         "code": 1,
#                         "data": "",
#                         "msg": "请重试"
#                     }
#
#             id = Ids(username, password)
#             data = id.login()
#             info = {
#                 "username": username,
#                 "password": password
#              }
#             token = encrypt(info)
#             l1 = id.get_self_info()
#             d1 = {
#                 "name": l1[0],
#                 "college": l1[1],
#                 "classname": l1[3],
#                 "token": token
#             }
#             info.update({"token": token})
#             if data:
#                 return {
#                     "code": 0,
#                     "data": d1,
#                     "msg": "登录成功"
#                 }
#             else:
#                 return login_error
#         except Exception as e:
#             logging.info(e)
#             return login_error


class KB(Resource):
    @new_login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        if g.test:
            return testUser.kb_return()
        try:
            if g.is_cook:
                data = get_kblist(xnm, xqm, g.jwxt_cook)
                msg = marshal_kb(data)
                if data:
                    return data_response(200, "抓取成功", data)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error


class Grades(Resource):
    @new_login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        if g.test:
            return testUser.grades_return()
        try:
            if g.is_cook:
                data = get_grade(xnm, xqm, g.jwxt_cook)
                pre_data = marshal_grade(data)
                if data:
                    return data_response(200, '请求成功', pre_data)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error

class MakeUpGrades(Resource):
    @new_login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        if g.test:
            return testUser.makeup_return()
        try:
            if g.is_cook:
                data = get_make_up_grades(xnm, xqm, g.jwxt_cook)
                pre_data = marshal_make_up_gardes(data)
                if data:
                    return data_response(200, '请求成功', pre_data)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error


class Exams(Resource):
    @new_login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        if g.test:
            return testUser.exams_return()
        try:
            if g.is_cook:
                data = get_exam(xnm, xqm, g.jwxt_cook)
                pre_data = marshal_exam(data)
                if data:
                    return data_response(200, '请求成功', pre_data)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error


class SingleJd(Resource):
    @new_login_required
    def get(self):
        args = parse_info.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')

        try:
            if g.is_cook:
                data = get_single_jd('08183007', xnm, xqm, g.jwxt_cook)

                if data:
                    return data_response(200, '请求成功', data)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error


class AverageJd(Resource):
    @new_login_required
    def get(self):
        try:
            if g.is_cook:
                data = get_average_jd('08183007', g.jwxt_cook)
                if data:
                    return data_response(200, '请求成功', data)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error


class EmptyRoom(Resource):
    @new_login_required
    def post(self):
        args = parse_room.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        build = args.get('build')
        section = args.get('section')
        week = args.get('week')
        weekday = args.get('weekday')
        try:
            if g.is_cook:
                data = get_empty_room(xnm, xqm, build, section, week, weekday, g.jwxt_cook)
                msg = marshal_room(data)
                if data:
                    return data_response(200, '请求成功', msg)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error


class SpecialCourse(Resource):
    @new_login_required
    def post(self):
        args = parse_class.parse_args()
        xnm = args.get('xnm')
        xqm = args.get('xqm')
        _id = args.get('id')
        weekday = args.get('weekday')
        week = args.get('week')
        section = args.get('section')
        teacher = args.get('teacher')
        try:
            if g.is_cook:
                data = get_special_course(xnm, xqm, _id, weekday, week, section, teacher, g.jwxt_cook)
                msg = marshal_course(data)
                if data['items']:
                    return data_response(200, '请求成功', msg)
            else:
                return data_error
        except Exception as e:
            logging.info(e)
            return data_error
