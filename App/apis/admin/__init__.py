from flask_restful import Api

from App.apis.admin.admin_api import FeedBacks, FeedBack, Amount, UserId

admin_api = Api(prefix='/admin')


admin_api.add_resource(FeedBacks, '/feedback')
admin_api.add_resource(FeedBack, '/feedback/<int:id>')
admin_api.add_resource(Amount, '/amount')
admin_api.add_resource(UserId, '/user')
