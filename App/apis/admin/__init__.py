from flask_restful import Api

from App.apis.admin.admin_api import FeedBacks, FeedBack, Amount, UserId, RootResource, ThirdPartyLogin

admin_api = Api(prefix='/admin')


admin_api.add_resource(FeedBacks, '/feedback')
admin_api.add_resource(FeedBack, '/feedback/<int:id>')
admin_api.add_resource(Amount, '/amount')
admin_api.add_resource(UserId, '/user_id')
admin_api.add_resource(RootResource, '/permission')
admin_api.add_resource(ThirdPartyLogin, '/third_login')
