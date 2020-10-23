from flask_restful import Resource, reqparse

from App.apis.api_constant import data_error
from App.apis.daily.utils import pc

parse_df = reqparse.RequestParser()
parse_df.add_argument("home", type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_df.add_argument("num", type=str, help='请提交正确的参数Key', required=True, location=['args'])




class DianFei(Resource):
    def get(self):
        args = parse_df.parse_args()
        home = args.get('home')
        num = args.get('num')

        dianfei = pc(home, num)
        if dianfei:
            return {
                "status": "200",
                "msg": "ok",
                "data": dianfei
            }
        else:
            return data_error
