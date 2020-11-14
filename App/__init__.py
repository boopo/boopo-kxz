import redis
from flask import Flask
from App.apis import init_api
from App.ext import init_ext, db
from App._settings import envs
from App.views import init_view


def create_app(env):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))
    # 初始化API
    init_api(app)
    # 初始化View
    init_view(app)
    # 初始化第三方扩展
    init_ext(app)

    return app
