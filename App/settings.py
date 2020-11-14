
SecretKey = 'uibDeGB3Q8FiQmD'

def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE')
    driver = dbinfo.get('DRIVER')
    user = dbinfo.get('USER')
    password = dbinfo.get('PASSWORD')
    host = dbinfo.get('HOST')
    port = dbinfo.get('PORT')
    name = dbinfo.get('NAME')
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456-abc",
        "HOST": "sh-cynosdbmysql-grp-db1zer1y.sql.tencentcdb.com",
        "PORT": 28737,
        "NAME": "kxz"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    REDIS_URL = "redis://:123456-abc@202.119.206.98:6379/0"

class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456-abc",
        "HOST": "sh-cynosdbmysql-grp-db1zer1y.sql.tencentcdb.com",
        "PORT": 28737,
        "NAME": "kxz"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

    REDIS_URL = "redis://:123456-abc@202.119.206.98:6379/0"


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456-abc",
        "HOST": "sh-cynosdbmysql-grp-db1zer1y.sql.tencentcdb.com",
        "PORT": 28737,
        "NAME": "kxz"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

   # REDIS_URL = "redis://@localhost:6379/0"
    REDIS_URL = "redis://:123456-abc@202.119.206.98:6379/0"


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456-abc",
        "HOST": "sh-cynosdbmysql-grp-db1zer1y.sql.tencentcdb.com",
        "PORT": 28737,
        "NAME": "kxz"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

    REDIS_URL = "redis://:123456-abc@202.119.206.98:6379/0"


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
