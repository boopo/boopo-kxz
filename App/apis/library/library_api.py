import logging

from flask import g
from flask_restful import Resource, reqparse

from App.apis.api_constant import book_error, data_response
from App.apis.library.utils.utils_request import get_book, check_book, get_image
from App.apis.new_login.utils.utils_cache import new_login_required
from App.apis.new_login.utils.utils_data_processing import marshal_library_history_list, marshal_library_list
from App.apis.new_login.utils.utils_request import get_library_history_list, get_library_favorite, get_library_list

parse_library = reqparse.RequestParser()
parse_library.add_argument('book', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_library.add_argument('page', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_library.add_argument('row', type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_shelf = reqparse.RequestParser()
parse_shelf.add_argument('id', type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_image = reqparse.RequestParser()
parse_image.add_argument('isbn', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_image.add_argument('title', type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_list = reqparse.RequestParser()
parse_list.add_argument("page", type=str, help='请输入页码', required=True, location=['json'])
parse_list.add_argument("rows", type=str, help='请输入大小', required=True, location=['json'])


class Library(Resource):
    def get(self):
        args = parse_library.parse_args()
        book_name = args.get('book')
        page = args.get('page')
        row = args.get('row')
        try:
            data = get_book(book_name, page, row)
            if data:
                return {
                    "status": 200,
                    "msg": "抓取成功",
                    "data": data
                }
        except Exception as e:
            logging.info(e)
            return book_error


class OnShelf(Resource):
    def get(self):
        args = parse_shelf.parse_args()
        id = args.get('id')
        try:
            data = check_book(id)
            return {
                "status": 200,
                "msg": "抓取成功",
                "data": data
            }
        except Exception as e:
            logging.info(e)
            return book_error


class BookImage(Resource):
    def get(self):
        args = parse_image.parse_args()
        isbn = args.get('isbn')
        title = args.get('title')
        data = get_image(isbn, title)
        try:
            return {
                "status": 200,
                "msg": "抓取成功",
                "data": data
            }
        except Exception as e:
            logging.info(e)
            return book_error


class libraryList(Resource):
    @new_login_required
    def get(self):
        args = parse_list.parse_args()
        page = args.get('page')
        rows = args.get('rows')
        try:
            if g.is_cook:
                data = get_library_list(g.lib_cook, page, rows)
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
                data = get_library_history_list(g.lib_cook, page, rows)
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
                data = get_library_favorite(g.lib_cook, page, rows)
                return data_response(200, '请求成功', data)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            logging.info(e)
            return data_response(500, e, '')


