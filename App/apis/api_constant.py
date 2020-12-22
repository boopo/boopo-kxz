"""
因为历史遗留问题，返回格式有点不同,
新版正在测试。
"""


class ResponseCode:
    SUCCESS = 200
    CREATE_OK = 201
    NOT_ALLOWED = 203
    NOT_FOUND = 404
    SQL_ERROR = 500


def data_response(status=200, msg='ok', data=' '):
    return {
        'status': status,
        'msg': msg,
        'data': data
    }, status


def login_response(code=0, msg='', token='', r_code=200):
    return {
               "code": code,
               "msg": msg,
               "token": token
           }, r_code


data_error = {
    "status": 404,  # 前端问题，暂时未修改
    "msg": "抓取失败",
    "data": "Null"
}

sql_error = {
    "msg": "获取失败,数据添加或查询出现错误",
    "data": "Null"
}

book_error = {
    "status": 404,
    "msg": "图书获取失败",
    "data": {
        "all": 0,
        "bookList": []
    }
}
