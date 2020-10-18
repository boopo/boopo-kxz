from flask_restful import Api

from App.apis.admin.admin_api import FeedBack

admin_api = Api(prefix='/admin')


admin_api.add_resource(FeedBack, '/feedback/')