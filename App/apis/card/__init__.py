from flask_restful import Api

from App.apis.card.card_api import chargeBalance, historyBalance

card_api = Api(prefix='/card')


card_api.add_resource(chargeBalance, '/charge')
card_api.add_resource(historyBalance, '/historyBalance')