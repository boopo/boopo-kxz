SecretKey = 'jwt 密钥'

ThirdSecretKey = '单点登录 jwt 密钥'


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
        "USER": "你的用户名",
        "PASSWORD": "你的密码",
        "HOST": "你的ip地址",
        "PORT": '你的端口号',
        "NAME": "你的库名"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

    REDIS_URL = ""
    # REDIS_URL = ""
    REDIS01_URL = ""


# 读   REDIS_URL = ""

class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "",
        "PORT": '',
        "NAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

    REDIS_URL = ""
    REDIS01_URL = ""


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "",
        "PORT": '',
        "NAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

    REDIS_URL = ""
    REDIS01_URL = ""


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "",
        "PORT": '',
        "NAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

    REDIS_URL = ""
    REDIS01_URL = ""


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
