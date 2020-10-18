import time
import jwt
from flask import request, g, abort

from App.apis.jwxt.cumt_id import Ids

headers = {
    "groupCode": "200069",
    "Referer": "https://findcumt.libsp.com/"
}


def encrypt(body):  # 加密算法
    token_dict = {
        'iat': time.time(),
        'data': body
    }
    headers = {
        'alg': "HS256",  # 声明所使用的算法
    }

    jwt_token = jwt.encode(token_dict, "uibDeGB3Q8FiQmD", algorithm="HS256", headers=headers).decode('ascii')

    # print(jwt_token)
    return jwt_token

def decrypt(token):  # 解密算法
    try:
        #           需要解析的 jwt        密钥                使用和加密时相同的算法
        data = jwt.decode(token, "uibDeGB3Q8FiQmD", algorithms=['HS256'])
        #  print(data)
        return (data)
    except Exception as e:
        print(e)
        return ('error')

def login_required(fun):  # 装饰器用，验证token，实现登录
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        print(token)
        if token is None:
            abort(401)
        info = decrypt(token)
        if info == 'error':
            abort(401)
        username = info['data']['username']
        password = info['data']['password']
        id = Ids(username, password)
        data = id.login()
        if data is None:
            abort(401)
        g.id = id
        return fun(*args, **kwargs)

    return wrapper

def marshal_grade(data):  # 成绩预处理
    # 凑活使用中 绩点与成绩接口不统一
    bklt = []  # 接受处理过的成绩
    kd = {"xmcj": "0"}  # 旷考手动添加成绩
    # 用flag做标记
    ps = 0  # 平时成绩
    qm = 0  # 期末
    sy = 0  # 实验
    qz = 0  # 期中
    # print(data)
    for single_data in data['items']:

        foda = {
            "courseName": single_data['kcmc'],
            "xuefen": single_data['xf'],
            "jidian": 5.0,
            "zongping": '100',
            "scoreDetail": []
        }

        if '平时' in single_data['xmblmc']:
            ps = 1
            if 'xmcj' not in single_data.keys():
                print("没有平时分")
                single_data.update(kd)

            pscj = {'name': single_data['xmblmc'], 'score': single_data['xmcj']}
        if '期中' in single_data['xmblmc']:  # 对应体育
            qz = 1
            if 'xmcj' not in single_data.keys():
                print("没有期中分")
                single_data.update(kd)
            qzcj = {'name': single_data['xmblmc'], 'score': single_data['xmcj']}

        if '实验' in single_data['xmblmc']:
            sy = 1
            if 'xmcj' not in single_data.keys():
                single_data.update(kd)

            sycj = {'name': single_data['xmblmc'], 'score': single_data['xmcj']}
            print(single_data['kcmc'])
        #   print(foda)
        if '期末' in single_data['xmblmc']:
            qm = 1
            if 'xmcj' not in single_data.keys():
                print(single_data['kcmc'], "旷考")
                single_data.update(kd)

            qmcj = {'name': single_data['xmblmc'], 'score': single_data['xmcj']}

        #  print(foda)
        if single_data['xmblmc'] == '总评':
            if 'xmcj' not in single_data.keys():
                single_data.update(kd)
            foda['zongping'] = single_data['xmcj']
            if '95' <= foda['zongping'] <= '100':
                foda['jidian'] = 5.0
                print(single_data['kcmc'])
            if '94' >= foda['zongping'] >= '90':
                foda['jidian'] = 4.5
            if '85' <= foda['zongping'] <= '89':
                foda['jidian'] = 4.0
            if '82' <= foda['zongping'] <= '84':
                foda['jidian'] = 3.5
            if '78' <= foda['zongping'] <= '81':
                foda['jidian'] = 3.0
            if '75' <= foda['zongping'] <= '77':
                foda['jidian'] = 2.8
            if '72' <= foda['zongping'] <= '74':
                foda['jidian'] = 2.5
            if '68' <= foda['zongping'] <= '71':
                foda['jidian'] = 2.0
            if '65' <= foda['zongping'] <= '67':
                foda['jidian'] = 1.5
            if '60' <= foda['zongping'] <= '64':
                foda['jidian'] = 1.0
            if '0' <= foda['zongping'] < '60':
                foda['jidian'] = 0
                if foda['zongping'] == '100':
                    foda['jidian'] = 5.0

            if foda['zongping'] == '优秀':
                foda['zongping'] = '90'
                foda['jidian'] = 4.5
            if foda['zongping'] == '良好':
                foda['zongping'] = '85'
                foda['jidian'] = 3.5
            if foda['zongping'] == '中等':
                foda['zongping'] = '75'
                foda['jidian'] = 2.5
            if foda['zongping'] == '合格' or foda['zongping'] == '及格':
                foda['zongping'] = '65'
                foda['jidian'] = 1.0
            if foda['zongping'] == '不及格':
                foda['zongping'] = '0'
                foda['jidian'] = 0

            zpcj = {'name': single_data['xmblmc'], 'score': single_data['xmcj']}
            if ps:
                foda['scoreDetail'].append(pscj)
                ps = 0
            if qz:
                foda['scoreDetail'].append(qzcj)
                qz = 0

            if sy:
                foda['scoreDetail'].append(sycj)
                sy = 0
            if qm:
                foda['scoreDetail'].append(qmcj)
                qm = 0

            foda['scoreDetail'].append(zpcj)
            ps = 0
            qz = 0
            sy = 0
            qm = 0

            bklt.append(foda)
    return bklt


def marshal_kb(data):  # 课表预处理
    del [data['xqbzxxszList']]
    del [data['jxhjkcList']]
    del [data['xqjmcMap']]
    del [data['xkkg']]
    del [data['xskbsfxstkzt']]
    del [data['kblx']]
    del [data['qsxqj']]
    del [data['xsxx']]
    del [data['sjkList']]
    del [data['xsbjList']]
    return data

def marshal_exam(data):  # 考试预处理
    exam_list = []
    # 删除无用数据
    del [data['currentPage']]
    del [data['currentResult']]
    del [data['entityOrField']]
    del [data['limit']]
    del [data['offset']]
    del [data['showCount']]
    del [data['sortOrder']]
    del [data['sorts']]
    del [data['totalPage']]
    del [data['totalResult']]
    del [data['pageNo']]
    del [data['pageSize']]
    del [data['sortName']]
    del [data['totalCount']]
    # 对单个考试信息提取
    for single_data in data['items']:
        location = {
            "local": single_data['cdbh'],
            "time": single_data['kssj'],
            "course": single_data['kcmc'],
            "type": single_data['ksmc'],
            "year": int(single_data['kssj'][0:4]),
            "month": int(single_data['kssj'][5:7]),
            "day": int(single_data['kssj'][8:10])
        }

        exam_list.append(location)
    return exam_list

def marshal_room(data):  # 空闲教室预处理
    list = []
    for single in data['items']:
        a = {"room": single['cdmc']}
        list.append(a)
    return list


def marshal_course(data):  # 上课条件数据处理
    list = []
    for single in data['items']:
        a = {
            #    "title": single['zcmc'],   存在无职称的情况
            "college": single['kkxy'],
            "class_name": single['kcmc'],
            "teacher_name": single['xm'],
            "_class": single['jxbzc'],
            "time": single['sksj'],
            "location": single['jxdd']
        }
        list.append(a)
    return list
