import re
import time

import requests
from bs4 import BeautifulSoup


def get_kblist(xnm, xqm, cook):
    # 课表查询
    if xqm == '3':
        xqm = '16'  # 第三学期
    if xqm == '1':
        xqm = '3'  # 第一学期
    if xqm == '2':
        xqm = '12'  # 第二学期
    url = 'http://jwxt.cumt.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151'
    form_data = {
        'xnm': xnm,
        'xqm': xqm,
    }
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook,
    }
    a = requests.post(url=url, data=form_data, headers=headers)
    return a.json()


def get_grade(xnm, xqm, cook):
    # 成绩查询
    if xnm == '0':  # 全部学年
        xnm = ''
    if xqm == '2':
        xqm = '12'  # 第二学期
    if xqm == '3':
        xqm = '16'  # 第三学期
    if xqm == '0':
        xqm = ''  # 全部
    if xqm == '1':
        xqm = '3'  # 第一学期
    url = 'http://jwxt.cumt.edu.cn/jwglxt/cjcx/cjcx_cxXsKccjList.html?doType=query&gnmkdm=N305005'
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }
    form_data = {
        'xnm': xnm,
        'xqm': xqm,
        '_search': 'false',
        'nd': int(time.time()),
        'queryModel.showCount': '300',
        'queryModel.currentPage': '1',
        'queryModel.sortName': 'xnmmc',
        'queryModel.sortOrder': 'asc',
        'time': '1'
    }
    # print(form_data)
    a = requests.post(url=url, headers=headers, data=form_data).json()
    return a


def get_average_jd(username, cook):
    su = username
    url = 'http://jwxt.cumt.edu.cn/jwglxt/xsxy/xsxyqk_cxXsxyqkIndex.html?gnmkdm=N105515&layout=default&su=' + su

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }

    a = requests.get(url=url, headers=headers)
    grade = re.findall('平均学分绩点</a>（GPA）：<font size="2px" style="color: red;">(.*?)</font>', a.text)
    return grade[0]


def get_exam(xnm, xqm, cook):
    # 考试查询
    if xqm == '1':  # 第一学期
        xqm = '3'
    if xqm == '2':  # 第二学期
        xqm = '12'
    if xqm == '0':  # 全部学期
        xqm = ''
    url = 'http://jwxt.cumt.edu.cn/jwglxt/kwgl/kscx_cxXsksxxIndex.html?doType=query&gnmkdm=N358105'
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }
    form_data = {
        'xnm': xnm,
        'xqm': xqm,
        '_search': 'false',
        'nd': int(time.time()),
        'queryModel.showCount': '50',
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc',
        'time': '1'
    }

    #    print(form_data)
    a = requests.post(url=url, data=form_data, headers=headers)
    #   print(a.text)
    return a.json()


def get_single_jd(username, xnm, xqm, cook):
    if xqm == '1':  # 第一学期
        xqm = '3'
    if xqm == '2':  # 第二学期
        xqm = '12'
    if xqm == '0':  # 全部学期
        xqm = ''
    url = 'http://jwxt.cumt.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N100801'

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }

    form_data = {
        'xh_id': username,
        'xnm': xnm,
        'xqm': xqm,
        '_search': 'false',
        'nd': int(time.time()),
        'queryModel.showCount': '300',
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc',
        'time': '1'
    }
    a = requests.post(url=url, data=form_data, headers=headers).json()
    return a


def get_self_info(cook):  # 后期会更换这个函数，先顶一下。。。。。
    url = 'http://jwxt.cumt.edu.cn/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default'
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }
    form_data = {
        'gndm': 'N100801'
    }

    a = requests.post(url=url, data=form_data, headers=headers)
    a.encoding = a.apparent_encoding
    soup = BeautifulSoup(a.text, 'html5lib')
    x = soup.find_all('p', class_='form-control-static')
    ss = []
    data = []
    for a in x:
        data.append(a.string)
    #  格式是固定的
    ss.append(data[1])  # 姓名
    ss.append(data[24][7:-4])  # 学院
    ss.append(data[26][7:-4])  # 年级
    ss.append(data[28][7:-4])  # 班级
    return ss


def get_empty_room(xnm, xqm, build, section, week, weekday, cook):
    if xqm == '1':  # 第一学期
        xqm = '3'
    if xqm == '2':  # 第二学期
        xqm = '12'
    if xqm == '0':  # 全部学期
        xqm = ''
    url = 'http://jwxt.cumt.edu.cn/jwglxt/cdjy/cdjy_cxKxcdlb.html?doType=query&gnmkdm=N2155'
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }
    form_data = {
        "fwzt": "cx",
        "xqh_id": "2",
        "xnm": xnm,
        "xqm": xqm,
        "cdlb_id": "021",
        "lh": build,  # 如博学楼
        "jyfs": "0",
        "zcd": week,  # 第几周
        "xqj": weekday,  # 星期几 多个用 1，2，3，4.。
        "jcd": section,  # 第几节课
        "_search": "false",
        "nd": int(time.time()),
        "queryModel.showCount": "300",
        "queryModel.currentPage": "1",
        "queryModel.sortName": "cdbh",
        "queryModel.sortOrder": "asc"
    }
    a = requests.post(url=url, data=form_data, headers=headers).json()
    return a


def get_special_course(xnm, xqm, _id, weekday, week, section, teacher, cook):
    if xqm == '1':  # 第一学期
        xqm = '3'
    if xqm == '2':  # 第二学期
        xqm = '12'
    if xqm == '0':  # 全部学期
        xqm = ''
    url = 'http://jwxt.cumt.edu.cn/jwglxt/design/funcData_cxFuncDataList.html?func_widget_guid=DA1B5BB30E1F4CB99D1F6F526537777B&gnmkdm=N219904'
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }

    form_data = {
        "xnm": xnm,
        "xqm": xqm,
        "kkbm_id": _id,  # 08计算机学院  全部为空
        "xqj": weekday,  # 星期几
        "qsjsz": week,  # 起始结束周 如1-4
        "skjc": section,  # 上课节次 如 1-6
        "js": teacher,  # 教师 没有可返回空
        "_search": "false",
        "nd": int(time.time()),
        "queryModel.showCount": "15",
        "queryModel.currentPage": "1",
        "queryModel.sortName": "",
        "queryModel.sortOrder": "asc"
    }

    if _id == '0':
        form_data.pop("kkbm_id")
    #    print("全部学院")
    #    print(form_data)
    if teacher == '0':
        form_data.pop("js")
    a = requests.post(url=url, data=form_data, headers=headers).json()
    # print(a)
    return a

def get_make_up_grades(xnm, xqm, cook):
    # 考试查询（含补考 但只有总成绩）
    if xnm == '0':  # 全部学年
        xnm = ''
    if xqm == '1':  # 第一学期
        xqm = '3'
    if xqm == '2':  # 第二学期
        xqm = '12'
    if xqm == '0':  # 全部学期
        xqm = ''
    url = "http://jwxt.cumt.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N100801"
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cook
    }
    form_data = {
        'xnm': xnm,
        'xqm': xqm,
        '_search': 'false',
        'nd': int(time.time()),
        'queryModel.showCount': '500',
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc',
        'time': '1'
    }

    a = requests.post(url=url, data=form_data, headers = headers)
    return a.json()
