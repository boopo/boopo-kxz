import redis
from flask import Flask
from flask_cors import CORS

from App._settings import envs
from App.apis import init_api
from App.ext import init_ext, db

from App.views import init_view


def create_app(env):
    app = Flask(__name__)
    # 跨域设置
    CORS(app, supports_credentials=True)
    # 初始化配置
    app.config.from_object(envs.get(env))
    # 初始化API
    init_api(app)
    # 初始化View
    init_view(app)
    # 初始化第三方扩展
    init_ext(app)

    return app
