from flask_restful import Api

from App.apis.daily.daily_api import DianFei

daily_api = Api(prefix='/daily')

daily_api.add_resource(DianFei, '/df')