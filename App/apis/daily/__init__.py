from flask_restful import Api

from App.apis.daily.daily_api import DianFei, HomeImage, SdNews, SdNew, RwNews, XsNews, XsNew, XxNews

daily_api = Api(prefix='/daily')

daily_api.add_resource(DianFei, '/df')
daily_api.add_resource(HomeImage, '/home_image')
daily_api.add_resource(SdNews, '/sd_news')
daily_api.add_resource(SdNew, '/sd_new')
daily_api.add_resource(RwNews, '/rw_news')
daily_api.add_resource(XsNews, '/xs_news')
daily_api.add_resource(XsNew, '/xs_new')
daily_api.add_resource(XxNews, '/xx_news')