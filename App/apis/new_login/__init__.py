from flask_restful import Api

from App.apis.new_login.new_apis.login_api import newLogin, simpleBalance, simpleLibrary, simpleBalanceHistory
from App.apis.new_login.new_apis.new_card_api import chargeBalance, historyBalance
from App.apis.new_login.new_apis.new_lib_api import libraryList, libraryHistoryList, libraryFavorite

new_login_api = Api(prefix='/new')

new_login_api.add_resource(newLogin, '/login')
new_login_api.add_resource(simpleBalance, '/simpleBalance')
new_login_api.add_resource(simpleLibrary, '/simpleLibrary')
new_login_api.add_resource(chargeBalance, '/charge')
new_login_api.add_resource(historyBalance, '/historyBalance')
new_login_api.add_resource(simpleBalanceHistory, '/simpleHistory')
new_login_api.add_resource(libraryList, '/libraryList')
new_login_api.add_resource(libraryHistoryList, '/libraryHistoryList')
new_login_api.add_resource(libraryFavorite, '/libraryFavorite')
