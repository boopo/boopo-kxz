from flask import g
from flask_restful import Resource, reqparse

from App.apis.api_constant import data_response
from App.apis.new_login.utils.utils_cache import new_login_required
from App.apis.new_login.utils.utils_request import get_balance_charge, get_balance_history_pro

parse_charge = reqparse.RequestParser()
parse_charge.add_argument("money", type=str, help='请输入金额', required=True, location=['json'])

parse_history = reqparse.RequestParser()
parse_history.add_argument("sdate", type=str, help='请输入开始时间', required=True, location=['json'])
parse_history.add_argument("edate", type=str, help='请输入结束时间', required=True, location=['json'])
parse_history.add_argument("page", type=str, help='请输入第几页', required=True, location=['json'])
parse_history.add_argument("rows", type=str, help='请输入多少行', required=True, location=['json'])


class chargeBalance(Resource):
    @new_login_required
    def get(self):
        args = parse_charge.parse_args()
        money = args.get("money")
        try:
            if g.is_cook:
                data = get_balance_charge(g.sess_cook, g.hall_cook, money)
                return data_response(200, '请求成功', data)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            return data_response(500, e, '')


class historyBalance(Resource):
    @new_login_required
    def get(self):
        args = parse_history.parse_args()
        s_date = args.get('sdate')
        e_date = args.get('edate')
        page = args.get('page')
        rows = args.get('rows')
        try:
            if g.is_cook:
                data = get_balance_history_pro(g.sess_cook, g.hall_cook, s_date, e_date, page, rows)
                return data_response(200, '请求成功', data)
            else:
                return data_response(500, 'Cookie错误', '')
        except Exception as e:
            print(e)
            return data_response(500, e, '')
