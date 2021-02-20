import logging

from flask import g
from flask_restful import Resource, reqparse

from App.apis.api_constant import data_response
from App.apis.new_login.utils.utils_cache import new_login_required
from App.apis.new_login.utils.utils_data_processing import marshal_library_list, marshal_library_history_list
from App.apis.new_login.utils.utils_request import get_library_list, get_library_history_list, get_library_favorite

parse_list = reqparse.RequestParser()
parse_list.add_argument("page", type=str, help='请输入页码', required=True, location=['json'])
parse_list.add_argument("rows", type=str, help='请输入大小', required=True, location=['json'])


class libraryList(Resource):
    @new_login_required
    def get(self):
        args = parse_list.parse_args()
        page = args.get('page')
        rows = args.get('rows')
        try:
            if g.is_cook:
                data = get_library_list(g.jwt_cook, page, rows)
                msg = marshal_library_list(data)
                return data_response(200, '请求成功', msg)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')


class libraryHistoryList(Resource):
    @new_login_required
    def get(self):
        args = parse_list.parse_args()
        page = args.get('page')
        rows = args.get('rows')
        try:
            if g.is_cook:
                data = get_library_history_list(g.jwt_cook, page, rows)
                msg = marshal_library_history_list(data)
                return data_response(200, '请求成功', msg)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')


class libraryFavorite(Resource):
    @new_login_required
    def get(self):
        args = parse_list.parse_args()
        page = args.get('page')
        rows = args.get('rows')
        try:
            if g.is_cook:
                data = get_library_favorite(g.jwt_cook, page, rows)
                return data_response(200, '请求成功', data)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')
