import time
import jwt
import requests
from flask import request, g, abort

from App.apis.jwxt.utils.utils_cumt_id import Ids
from App.ext import redis_client


def marshal_grade(data):  # 成绩预处理
    # 凑活使用中 绩点与成绩接口不统一
    bklt = []  # 接受处理过的成绩
    kd = {"xmcj": "0"}  # 旷考手动添加成绩
    # 用flag做标记
    ps = 0  # 平时成绩
    qm = 0  # 期末
    sy = 0  # 实验
    qz = 0  # 期中
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
            if 'xmcj' not in single_data.keys():  # 没有平时分
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
        #   print(foda)
        if '期末' in single_data['xmblmc']:
            qm = 1
            if 'xmcj' not in single_data.keys():  # 旷考
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

            if foda['zongping'] == '免修':
                foda['zongping'] = '100'
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


def get_list(str1):
    a1 = []
    if "," in str1:
        sub_str = str1.split(",")
        for l1 in sub_str:
            if "-" in l1:
                if "单" in l1:
                    b1 = int(l1.split("-")[0])
                    b2 = int(l1.split("-")[1].replace("周(单)", ""))
                    while (b1 <= b2):
                        if b1 % 2 == 1:
                            a1.append(b1)
                        b1 = b1 + 1
                elif "双" in l1:
                    b1 = int(l1.split("-")[0])
                    b2 = int(l1.split("-")[1].replace("周(双)", ""))
                    while (b1 <= b2):
                        if b1 % 2 == 0:
                            a1.append(b1)
                        b1 = b1 + 1
                else:
                    b1 = int(l1.split("-")[0])
                    b2 = int(l1.split("-")[1].replace("周", ""))
                    while (b1 <= b2):
                        a1.append(b1)
                        b1 = b1 + 1
            else:
                a1.append(int(l1.replace("周", "")))
    elif "-" in str1:
        if "单" in str1:
            b1 = int(str1.split("-")[0])
            b2 = int(str1.split("-")[1].replace("周(单)", ""))
            while (b1 <= b2):
                if b1 % 2 == 1:
                    a1.append(b1)
                b1 = b1 + 1
        elif "双" in str1:
            b1 = int(str1.split("-")[0])
            b2 = int(str1.split("-")[1].replace("周(双)", ""))
            while (b1 <= b2):
                if b1 % 2 == 0:
                    a1.append(b1)
                b1 = b1 + 1
        else:
            b1 = int(str1.split("-")[0])
            b2 = int(str1.split("-")[1].replace("周", ""))
            while (b1 <= b2):
                a1.append(b1)
                b1 = b1 + 1
    else:
        a1.append(int(str1.replace("周", "")))
    return a1


def marshal_new_kb(data):
    l1 = data['kbList']
    f1 = []
    for l2 in l1:
        d1 = {}
        d1.update({
            "title": l2['kcmc'],
            "location": l2['cdmc'],
            "teacher": l2['xm'],
            "credit": l2['xf'],
            "weekList": get_list(l2['zcd']),
            "weekNum": int(l2['xqj']),
            "lessonNum": int(l2['jcs'].split("-")[0]),
            "durationNum": int(l2['jcs'].split("-")[1]) - int(l2['jcs'].split("-")[0]) + 1,
            "remark": ""
        })
        f1.append(d1)
    return f1


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


def marshal_make_up_gardes(data): # 补考成绩查询  包含每次
    grades_list = data['items']
    l1 = []
    for a in grades_list:
        d1 = {}
        d1.update({
            "courseName": a['kcmc'],
            "xuefen": a['xf'],
            "jidian": a['jd'],
            "zongping": a['bfzcj'],
            "type": a['ksxz'],

        })
        l1.append(d1)
    return l1