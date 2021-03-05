import logging

from flask import g
from flask_restful import Resource, reqparse

from App.apis.api_constant import data_error, data_response
from App.apis.common_return import testUser
from App.apis.daily.utils import pc, get_home_image, get_multiple_sd_news, get_single_sd_news, get_multiple_rw_news, \
     get_multiple_xs_news, get_single_xs_news, get_multiple_xx_news

parse_df = reqparse.RequestParser()
parse_df.add_argument("home", type=str, help='请提交正确的参数Key', required=True, location=['args'])
parse_df.add_argument("num", type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_page = reqparse.RequestParser()
parse_page.add_argument("page", type=str, help='请提交正确的参数Key', required=True, location=['args'])

parse_url = reqparse.RequestParser()
parse_url.add_argument("url", type=str, help='请提交正确的参数Key', required=True, location=['args'])


class DianFei(Resource):
    def get(self):
        args = parse_df.parse_args()
        home = args.get('home')
        num = args.get('num')

        data = pc(home, num)
        if data:
            return data_response(200, "ok", data)
        else:
            return data_response(404, "抓取失败", "null")



class HomeImage(Resource):
    def get(self):
        try:
            data = get_home_image()
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")


class SdNews(Resource):
    def get(self):
        args = parse_page.parse_args()
        page = args.get('page')
        try:
            data = get_multiple_sd_news(page)
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")


class SdNew(Resource):
    def get(self):
        args = parse_url.parse_args()
        page = args.get('url')
        try:
            data = get_single_sd_news(page)
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")


class RwNews(Resource):
    def get(self):
        args = parse_page.parse_args()
        page = args.get('page')
        try:
            data = get_multiple_rw_news(page)
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")


class XsNews(Resource):
    def get(self):
        args = parse_page.parse_args()
        page = args.get('page')
        try:
            data = get_multiple_xs_news(page)
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")


class XsNew(Resource):
    def get(self):
        args = parse_url.parse_args()
        page = args.get('url')
        try:
            data = get_single_xs_news(page)
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")


class XxNews(Resource):
    def get(self):
        args = parse_page.parse_args()
        page = args.get('page')
        try:
            data = get_multiple_xx_news(page)
            if data:
                return data_response(200, "ok", data)
        except Exception as e:
            logging.info(e)
            return data_response(404, "抓取失败", "null")
