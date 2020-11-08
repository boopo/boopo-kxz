import json

from flask_restful import Resource, reqparse, fields, marshal_with, abort, marshal

from App.apis.admin.utils import require_permission
from App.apis.api_constant import sql_error
from App.ext import db
from App.models import Content, User, ADMIN, SUPER_ADMIN

parse_fb = reqparse.RequestParser()
parse_fb.add_argument("data", type=str, help='请输入反馈内容', required=True, location=['json'])

parse_user = reqparse.RequestParser()
parse_user.add_argument("username", type=str, help='请输入学号', required=True, location=['args'])

parse_root = reqparse.RequestParser()
parse_root.add_argument("username", type=str, help='请输入学号', required=True, location=['json'])
parse_root.add_argument("permission", type=str, help='请输入权限', required=True, location=['json'])

content_fields = {
    "id": fields.Integer,
    "data": fields.String
}

single_content_fields = {
    "stauts": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(content_fields)

}

multi_content_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(content_fields))
}

user_fields = {
    "username": fields.String,
    "permission": fields.Integer
}
multi_user_fields = {
    "status": fields.Integer,
    "msg": fields.Integer,
    "data": fields.List(fields.Nested(user_fields))
}


class FeedBacks(Resource):
    def post(self):
        args = parse_fb.parse_args()
        data = args.get('data')
        fb = Content()
        fb.data = data

        try:
            db.session.add(fb)
            db.session.commit()
            msg = {
                "status": 201,
                "msg": "create ok!",
                "data": data
            }
            return msg
        except Exception as e:
            print(e)
            return sql_error

    @require_permission(ADMIN)
    def get(self):
        try:
            content_list = Content.query.all()
            if not content_list:
                abort(404)

            msg = {
                "status": 200,
                "msg": "ok",
                "data": content_list
            }
            return marshal(msg, multi_content_fields)
        except Exception as e:
            print(e)
            return sql_error


class FeedBack(Resource):
    @require_permission(ADMIN)
    def get(self, id):
        try:
            fd = Content.query.get(id)
            data = {
                "status": 200,
                "msg": "ok",
                "data": fd
            }
            return marshal(data, single_content_fields)
        except Exception as e:
            print(e)
            return sql_error

    @require_permission(ADMIN)
    def delete(self, id):
        try:
            fd = Content.query.get(id)
            db.session.delete(fd)
            db.session.commit()
            data = {
                "status": 204,
                "msg": "delete ok",
                "data": id
            }
            return data

        except Exception as e:
            print(e)
            return sql_error


class Amount(Resource):
    @require_permission(ADMIN)
    def get(self):
        try:
            user = User.query.all()
            num = User.query.count()
            if not user:
                abort(401)
            data = {
                "status": 200,
                "msg": num,
                "data": user
            }
            return marshal(data, multi_user_fields)
        except Exception as e:
            print(e)
            return sql_error


class UserId(Resource):
    def get(self):
        try:
            args = parse_user.parse_args()
            username = args.get('username')
            user = User.query.filter(User.username.__eq__(username)).first()

            if user:
                data = {
                    "status": 200,
                    "msg": "ok",
                    "data": {
                        "rank": user.id
                    }
                }
                return data
            else:
                return {
                    "status": 200,
                    "msg": "ok",
                    "data": {
                        "rank": 9999
                    }
                }

        except Exception as e:
            print(e)
            return sql_error


class RootResource(Resource):
    @require_permission(SUPER_ADMIN)
    def post(self):
        args = parse_root.parse_args()
        username = args.get('username')
        permission = int(args.get('permission'))
        try:
            user = User.query.filter(User.username.__eq__(username)).first()
            user.permission = permission
            db.session.add(user)
            db.session.commit()
            return {
                "status": 201,
                "msg": "权限已更改",
                "data": username
            }
        except Exception as e:
            print(e)
            return sql_error


class MigrateResource(Resource):
    def get(self):
        l1 = ['08193109', '08192988', '04171180', '08183007', '20175556', '20175543', '12201328', '04191449', '04202107', '12202105', '04181334', '05201424', '08192942', '08205203', '08206412', '01190076', '08193106', '04191533', '08192788', '08203411', '08182994', '17195021', '06181987', '08183098', '05191575', '17195409', '12203739', '15194764', '17194986', '06182166', '15194763', '02190792', '08192926', '06172276', '06182137', '07203707', '09204147', '08183059', '01205008', '08182932', '12201330', '01170291', '08192818', '04181420', '11194056', '05191570', '03190886', '08192907', '04205003', '09193471', '03191024', '07205402', '14174312', '09203614', '06172001', '05181678', '02203710', '05204407', '05191769', '04171174', '16194876', '17195131', '17195081', '08192850', '12202101', '04201322', '11193930', '04201509', '08192783', '02180705', '02180315', '14194305', '08192985', '08192962', '06171991', '11204103', '12203230', '08193079', '08193092', '04191206', '08203711', '05206117', '05191759', '12204202', '08193100', '03190841', '03204307', '14174484', '08192916', '17185222', '04171484', '05191653', '06192145', '08193032', '10193657', ' 08192984', '08202101', '02190701', '11193932', '08206406', '05191672', '08193023', '17184998', '04191383', '04191458', '11193899', '02190604', '11193901', '11193900', '04201321', '04171294', '06192072', '16194874', '08182754', '16194872', '08192932', '17184996', '06182256', '05191571', '11193929', '06182080', '20195507', '12202201', '08206106', '20195511', '09203703', '17201314', '11184036', '12203721', '17185359', '08205306', '05181621', '17195322', '03191082', '10193641', '16184871', '04191463', '11193961', '02190498', '07182444', '08205402', '07182331', '01170264', '08192948', '06192202', '16194783', '15194768', '08192744', '17185406', '16184835', '08193011', '08183088', '02190621', '09193131', '12203728', '02190740', '16194793', '16194790', '03191055', '05191578', '08192947', '01170048', '16184800', '01190075', '16194851', '02190385', '03190884', '09193434', '01190089', '15174726', '17195445', '06192241', '01190004', '17195480', '17195377', '01190280', '08192928', '16194918', '06182147', '16194862', '16184876', '01201427', '01203605', '08193085', '17195255', '08192722', '12201407', '08206103', '08204113', '01201407', '16194791', '04171392', '05191582', '04202201', '09204307', '08193107', '17202301', '17195249', '15194660', '08192861', '17201411', '08192986', '03191142', '17205202', '08193022', '17201413', '06192206', '08192767', '08182995', '06192256', '05181821', '17195204', '12203719', '02190309', '02190590', '12203240', '09193283', '11193927', '09193412', '01203702', '12203705', '17205103', '08206522', '17195327', '06172148', '17195233', '08192796', '05201327', '15194766', '08193077', '05202304', '05181730', '01190142', '17203408', '01190282', '17204404', '16194795', '09201315', '05201312', '03201509', '02190383', '12203725', '01190278', '01180261', '17195340', '04171175', '06172218', '17203204', '02190712', '09183607', '02190708', '06182088', '09193312', '15194605']

        for a in l1:
            user = User()
            user.username = a
            user.permission = 2
            db.session.add(user)
            db.session.commit()
        return {
            "msg": "ok"
        }
