import logging

from flask_restful import Resource, reqparse

from App.apis.api_constant import book_error
from App.apis.library.utils import get_book, check_book, get_image

parse_library = reqparse.RequestParser()
parse_library.add_argument('book', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_library.add_argument('page', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_library.add_argument('row', type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_shelf = reqparse.RequestParser()
parse_shelf.add_argument('id', type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_image = reqparse.RequestParser()
parse_image.add_argument('isbn', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_image.add_argument('title', type=str, help='请提交正确的参数Key', required=True, location=['args'])


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
