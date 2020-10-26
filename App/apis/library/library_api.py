from flask_restful import Resource, reqparse

from App.apis.api_constant import data_error
from App.apis.library.utils import get_book

parse_library = reqparse.RequestParser()
parse_library.add_argument('book', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_library.add_argument('page', type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_library.add_argument('row', type=str, help='请提交正确的参数Key', required=True, location=['args'])
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
            print(e)
            return data_error
