from flask_restful import Resource, reqparse, fields, marshal_with, abort, marshal

from App.apis.api_constant import sql_error
from App.ext import db
from App.models import Content

parse_fb = reqparse.RequestParser()
parse_fb.add_argument("data", type=str, help='请提交正确的参数Key', required=True, location=['json'])

content_fields = {
    "id": fields.Integer,
    "data": fields.String
}
multi_content_fields = {
    "status": fields.String,
    "msg": fields.String,
    "data": fields.List(fields.Nested(content_fields))
}


class FeedBack(Resource):
    def post(self):
        parse = parse_fb.parse_args()
        data = parse.get('data')
        fb = Content()
        fb.data = data

        try:
            db.session.add(fb)
            db.session.commit()
            msg = {
                "status": "201",
                "msg": "create ok!",
                "data": data
            }
            return msg
        except Exception as e:
            print(e)
            return sql_error

    @marshal_with(multi_content_fields)
    def get(self):
        try:
            content_list = Content.query.all()
            if not content_list:
                abort(404)

            msg = {
                "status": "200",
                "msg": "ok",
                "data": content_list
            }
            return msg
        except Exception as e:
            print(e)
            return sql_error