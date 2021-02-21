import json
import logging

from flask import current_app
from flask_restful import Resource, reqparse, fields, abort, marshal

from App._settings import BaiduClientId, BaiduClientSecret
from App.apis.admin.utils import require_permission, set_version, get_version
from App.apis.api_constant import sql_error
from App.apis.jwxt.utils.utils_cache import encrypt
from App.celery import new_login, new_id_login
from App.ext import db
from App.models import Content, User, ADMIN, SUPER_ADMIN
from App.utils.captcha import Captcha


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

parse_version = reqparse.RequestParser()
parse_version.add_argument("version", type=str, help='请输入版本号', required=True, location=['json'])
parse_version.add_argument("url", type=str, help='请输入url', required=True, location=['json'])
parse_version.add_argument("description", type=str, help='请输入描述', required=True, location=['json'])
parse_version.add_argument("isForceUpgrade", type=str, help='请输入描述', required=True, location=['json'])

parse_update = reqparse.RequestParser()
parse_update.add_argument("version", type=str, help='请输入版本号', required=True, location=['args'])

parse_self_kb = reqparse.RequestParser()
parse_self_kb.add_argument("data", type=str, help="自定义课表", required=True, location=['json'])

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
            logging.info(e)
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
            logging.info(e)
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
            logging.info(e)
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
            logging.info(e)
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
            logging.info(e)
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
            logging.info(e)
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
            logging.info(e)
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
            logging.info(e)
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
            logging.info("权限"+e)
            return sql_error, 500


class VersionResource(Resource):
    @require_permission(SUPER_ADMIN)
    def post(self):
        try:
            args = parse_version.parse_args()
            version = args.get("version")
            upgrade = args.get("isForceUpgrade")
            desc = args.get("description")
            url = args.get("url")
            l1 = {
                "version": version,
                "upgrade": upgrade,
                "url": url,
                "desc": desc
            }
            if set_version(l1):
                return {
                    "status": 200,
                    "msg": "ok",
                    "data": url
                }
            else:
                return sql_error
        except Exception as e:
            logging.info("version"+e)
            return sql_error, 500

    def get(self):
        args = parse_update.parse_args()
        version = args.get('version')
        try:
            isForce = False
            check = False
            data = get_version(version)
            if 'True' in data[1]:
                isForce = True
            if version != data[0]:
                check = True
            return {
                "status": 200,
                "check": check,
                "isForceUpgrade": isForce,
                "description": data[3],
                "apkUrl": data[2]
            }
        except Exception as e:
            return {
                "status": 404,
                "check": False,
                "isForceUpgrade": False,
                "description": "找不到资源",
                "apkUrl": ""
            }

class TestResource(Resource):
    def get(self):
        args = parse_self_kb.parse_args()
        current_app.logger.info("日志测试")
        #a = new_login.delay()
        b = new_id_login.delay("08193109","k1333csn")
        return {
            "data": encrypt({"username": "08193109", "password": "k1333csn"})
        }