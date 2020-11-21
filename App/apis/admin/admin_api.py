
from flask_restful import Resource, reqparse, fields, abort, marshal

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

parse_paginate = reqparse.RequestParser()
parse_paginate.add_argument("page", type=str, help='请输入页码', required=True, location=['args'])
parse_paginate.add_argument("perPage", type=str, help='请输入页面大小', required=True, location=['args'])

content_fields = {
    "id": fields.Integer,
    "data": fields.String
}

single_content_fields = {
    "msg": fields.String,
    "data": fields.Nested(content_fields)

}

multi_content_fields = {
    "num": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(content_fields))
}

user_fields = {
    "username": fields.String,
    "permission": fields.Integer
}
multi_user_fields = {
    "num": fields.Integer,
    "msg": fields.String,
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
            num = Content.query.count()
            if not content_list:
                abort(404)

            msg = {
                "num": num,
                "msg": "ok",
                "data": content_list,
            }
            return marshal(msg, multi_content_fields)
        except Exception as e:
            print(e)
            return sql_error, 500


class FeedBack(Resource):
    @require_permission(ADMIN)
    def get(self, id):
        try:
            fd = Content.query.get(id)
            data = {
                "msg": "ok",
                "data": fd
            }
            return marshal(data, single_content_fields)
        except Exception as e:
            print(e)
            return sql_error, 500

    @require_permission(ADMIN)
    def delete(self, id):
        try:
            fd = Content.query.get(id)
            db.session.delete(fd)
            db.session.commit()
            data = {
                "msg": "delete ok",
                "data": id
            }
            return data, 204

        except Exception as e:
            print(e)
            return sql_error, 500


class PageFeedBacks(Resource):
    @require_permission(ADMIN)
    def get(self):
        try:
            args = parse_paginate.parse_args()
            page = int(args.get("page"))
            per_page = int(args.get("perPage"))
            feed_list = Content.query.offset(per_page * (page - 1)).limit(per_page)
            feed_num = Content.query.count()
            msg = {
                "num": feed_num,
                "msg": "ok",
                "data": feed_list
            }
            return marshal(msg, multi_content_fields)
        except Exception as e:
            print(e)
            return sql_error, 500


class UserNumber(Resource):
    @require_permission(ADMIN)
    def get(self):
        try:
            num = User.query.count()
            return {
                "msg": "ok",
                "data": num
            }
        except Exception as e:
            return {
                       "msg": "error",
                       "data": "数据查询失败，请重试"
                   }, 500


class Amount(Resource):
    @require_permission(ADMIN)
    def get(self):
        try:
            user = User.query.all()
            num = User.query.count()
            if not user:
                abort(401)
            data = {
                "num": num,
                "msg": "ok",
                "data": user
            }
            return marshal(data, multi_user_fields)
        except Exception as e:
            print(e)
            return sql_error, 500


class PageAmount(Resource):
    @require_permission(ADMIN)
    def get(self):
        try:
            args = parse_paginate.parse_args()
            page = int(args.get("page"))
            per_page = int(args.get("perPage"))
            user_list = User.query.offset(per_page * (page - 1)).limit(per_page)
            user_num = User.query.count()
            msg = {
                "num": user_num,
                "msg": "ok",
                "data": user_list
            }
            return marshal(msg, multi_user_fields)

        except Exception as e:
            print(e)
            return sql_error, 500


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
            return sql_error, 500


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
                       "msg": "权限已更改",
                       "data": username
                   }, 201
        except Exception as e:
            print(e)
            return sql_error, 500

