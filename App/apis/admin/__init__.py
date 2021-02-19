from flask_restful import Api

from App.apis.admin.admin_api import FeedBacks, FeedBack, Amount, UserId, RootResource, UserNumber, PageFeedBacks, \
    PageAmount, VersionResource, TestResource

admin_api = Api(prefix='/admin')


admin_api.add_resource(FeedBacks, '/feedback')               # 意见反馈
admin_api.add_resource(FeedBack, '/feedback/<int:id>')       # 单条反馈
admin_api.add_resource(Amount, '/amount')                    # 总用户信息
admin_api.add_resource(UserId, '/user_id')                   # 查询用户id
admin_api.add_resource(RootResource, '/permission')          # 修改用户权限
admin_api.add_resource(UserNumber, '/user_number')           # 查询用户总数
admin_api.add_resource(PageFeedBacks, '/page_feedback')      # 分页意见反馈
admin_api.add_resource(PageAmount, '/page_amount')           # 分页用户信息
admin_api.add_resource(VersionResource, '/version')

admin_api.add_resource(TestResource,'/test')