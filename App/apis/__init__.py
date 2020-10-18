
from App.apis.admin import admin_api
from App.apis.daily import daily_api
from App.apis.jwxt import jwxt_api
from App.apis.library import library_api


def init_api(app):
    admin_api.init_app(app)
    daily_api.init_app(app)
    jwxt_api.init_app(app)
    library_api.init_app(app)

