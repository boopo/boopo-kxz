from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()

redis_client = FlaskRedis()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)

