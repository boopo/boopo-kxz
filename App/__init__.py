from flask import Flask
from App.apis import init_api
from App.ext import init_ext,db
from App.views import init_view


def create_app(env):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # 初始化API
    init_api(app)
    # 初始化View
    init_view(app)
    # 初始化第三方扩展
    init_ext(app)




    return app