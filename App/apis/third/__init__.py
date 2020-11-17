from flask_restful import Api

from App.apis.third.third_api import ThirdPartyLogin

third_api = Api(prefix='/third')

third_api.add_resource(ThirdPartyLogin, '/login')
