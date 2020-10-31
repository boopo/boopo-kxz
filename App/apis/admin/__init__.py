from flask_restful import Api

from App.apis.admin.admin_api import FeedBacks, FeedBack

admin_api = Api(prefix='/admin')


admin_api.add_resource(FeedBacks, '/feedback')
admin_api.add_resource(FeedBack, '/feedback/<int:id>')
