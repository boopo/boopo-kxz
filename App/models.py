from App.ext import db

BLACK_USER = 1  # 黑名单
COMMON_USER = 2  # 普通用户
VIP_USER = 4  # 白嫖用户
PREMIUM_USER = 8  # 付费用户
COOPERATIVE_USER = 16  # 第三方合作用户
TEACHER = 32  # 老师
ADMIN = 64  # 管理员
SUPER_ADMIN = 128  # root


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(256))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    permission = db.Column(db.Integer, default=COMMON_USER)

    def check_permission(self, permission):
        if self.permission == SUPER_ADMIN:
            return True
        if (BLACK_USER & self.permission) == BLACK_USER:
            return False
        else:
            return (permission & self.permission) == permission


class Ocr(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access_token = db.Column(db.String(256))



'''
class Apk(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    version = db.Column(db.String)
    upgrade = db.Integer(db.Integer(16))
    desc = db.Column(db.String(256))
    url = db.Column(db.String(256))
'''