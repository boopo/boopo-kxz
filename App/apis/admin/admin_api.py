import json

from flask_restful import Resource, reqparse, fields, marshal_with, abort, marshal

from App.apis.admin.utils import require_permission
from App.apis.api_constant import sql_error
from App.ext import db, redis_third
from App.models import Content, User, ADMIN, SUPER_ADMIN, COOPERATIVE_USER

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


