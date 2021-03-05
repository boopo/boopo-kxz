from flask_restful import Api

from App.apis.new_login.new_apis.login_api import newLogin, simpleBalance, simpleLibrary, simpleBalanceHistory

new_login_api = Api(prefix='/new')

new_login_api.add_resource(newLogin, '/login')
new_login_api.add_resource(simpleBalance, '/simpleBalance')
new_login_api.add_resource(simpleLibrary, '/simpleLibrary')
new_login_api.add_resource(simpleBalanceHistory, '/simpleHistory')

