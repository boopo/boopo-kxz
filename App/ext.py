from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

migrate = Migrate()

redis_client = FlaskRedis()

redis_third = FlaskRedis()

redis_third.config_prefix = 'REDIS01'

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    redis_third.init_app(app)

