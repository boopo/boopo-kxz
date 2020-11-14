import time
import re
import requests
from bs4 import BeautifulSoup

from App.ext import redis_client, db
from App.models import User

session = requests.session()

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}

# 目前Ids仅用于登录获取 cookie，其他函数已搁置（有点慢。。。。。）
class Ids():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

    def login(self):
        self.err = []
        r = self.session.get(
            url='http://ids.cumt.edu.cn/authserver/login?service = http%3A%2F%2Fmy.cumt.edu.cn%2Flogin.portal',
            headers=headers)
        # print('第一次GET',r.status_code)
        text = r.text
        soup = BeautifulSoup(text, 'html5lib')
        lt = soup.find('input', {'name': 'lt'})['value']
        execution = soup.find('input', {'name': 'execution'})['value']
        From_Data = {  # 表单
            'username': self.username,
            'password': self.password,
            'lt': lt,
            'execution': execution,
            '_eventId': 'submit',
            'rmShown': '1',
            'signln': ''
        }
        self.err.append(From_Data)
        q = self.session.post(
            url='http://ids.cumt.edu.cn/authserver/login?service = http%3A%2F%2Fmy.cumt.edu.cn%2Flogin.portal',
            data=From_Data, headers=headers, allow_redirects=False)
        # print(q.status_code)
        self.err.append(q.status_code)
        if q.status_code == 302:
            self.cookies = q.cookies
            #    print('第二次POST',q.cookies)
            text = q.headers['Location']
            s = self.session.get(url=text)
            #    print('第三次GET',s.status_code)

            a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
            _data = {
                    'xnm': '2020',
                    'xqm': '1',
            }
            coo = self.session.cookies
            l1 = []
            for single in coo:
                l1.append(single.value)
            try:
                redis_client.set(name=self.username, value='JSESSIONID='+l1[3], ex=43200)
                print("redis正常", self.username, l1[3])
                if User.query.filter(User.username.__eq__(self.username)).first() is None:
                    user = User()
                    user.username = self.username
                    user.permission = 2
                    db.session.add(user)
                    db.session.commit()
                    print("新用户", self.username)
            except Exception as e:
                print("redis异常", e)
            return True
        if q.status_code == 200:
            soup_obj = BeautifulSoup(q.text, "html5lib")
            tips = soup_obj.find_all(id="msg")
            span = tips[0].string
            #    print(span)  # 打印错误原因
            return False

    '''       if span == "您提供的用户名或者密码有误。":
                return False
        else:
            return False
    '''

    def get_kblist(self, xnm, xqm):
        # 课表查询
        if xqm == '3':
            xqm = '16'  # 第三学期
        if xqm == '1':
            xqm = '3'  # 第一学期
        if xqm == '2':
            xqm = '12'  # 第二学期

        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
        form_data = {
            'xnm': xnm,
            'xqm': xqm,
        }
        #    print('课表第一次GET', a.status_code)
        a = self.session.post('http://jwxt.cumt.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151', data=form_data)
        #    print('课表第二次POST',a.status_code)
        return a.json()

    def get_grade(self, xnm, xqm):
        # 成绩查询

        if xqm == '2':
            xqm = '12'  # 第二学期
        if xqm == '3':
            xqm = '16'  # 第三学期
        if xqm == '0':
            xqm = ''  # 全部
        if xqm == '1':
            xqm = '3'  # 第一学期
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
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
        a = self.session.post('http://jwxt.cumt.edu.cn/jwglxt/cjcx/cjcx_cxXsKccjList.html?gnmkdm=N305007',
                              data=form_data).json()
        return a

    def get_average_jd(self):
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
        #    print('绩点第一次GET', a.cookies)
        su = self.username
        a = self.session.get(
            'http://jwxt.cumt.edu.cn/jwglxt/xsxy/xsxyqk_cxXsxyqkIndex.html?gnmkdm=N105515&layout=default&su=' + su)
        #    print("绩点第二次GET")
        grade = re.findall('平均学分绩点</a>（GPA）：<font size="2px" style="color: red;">(.*?)</font>', a.text)
        #    print(type(grade))
        return grade[0]

    def get_exam(self, xnm, xqm):
        # 考试查询
        if xqm == '1':  # 第一学期
            xqm = '3'
        if xqm == '2':  # 第二学期
            xqm = '12'
        if xqm == '0':  # 全部学期
            xqm = ''
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
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
        a = self.session.post(
            'http://jwxt.cumt.edu.cn/jwglxt/kwgl/kscx_cxXsksxxIndex.html?doType=query&gnmkdm=N358105',
            data=form_data)
        #   print(a.text)
        return a.json()

    def get_single_jd(self, xnm, xqm):
        if xqm == '1':  # 第一学期
            xqm = '3'
        if xqm == '2':  # 第二学期
            xqm = '12'
        if xqm == '0':  # 全部学期
            xqm = ''
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
        form_data = {
            'xh_id': self.username,
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
        a = self.session.post('http://jwxt.cumt.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N100801',
                              data=form_data).json()
        return a

    def get_self_info(self):  # 只爬到一个html，emmm。。。
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
        form_data = {
            'gndm': 'N100801'
        }

        a = self.session.post(
            'http://jwxt.cumt.edu.cn/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default',
            data=form_data)
        a.encoding = a.apparent_encoding
        # r = re.findall('<p class="form-control-static">(.*?)</p>',a.text) 只可返回姓名
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

    def get_empty_room(self, xnm, xqm, build, section, week, weekday):
        if xqm == '1':  # 第一学期
            xqm = '3'
        if xqm == '2':  # 第二学期
            xqm = '12'
        if xqm == '0':  # 全部学期
            xqm = ''
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
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
        a = self.session.post('http://jwxt.cumt.edu.cn/jwglxt/cdjy/cdjy_cxKxcdlb.html?doType=query&gnmkdm=N2155',
                              data=form_data).json()
        return a

    def get_special_course(self, xnm, xqm, _id, weekday, week, section, teacher):
        if xqm == '1':  # 第一学期
            xqm = '3'
        if xqm == '2':  # 第二学期
            xqm = '12'
        if xqm == '0':  # 全部学期
            xqm = ''
        a = self.session.get('http://jwxt.cumt.edu.cn/sso/jzIdsFivelogin')
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
        a = self.session.post(
            'http://jwxt.cumt.edu.cn/jwglxt/design/funcData_cxFuncDataList.html?func_widget_guid=DA1B5BB30E1F4CB99D1F6F526537777B&gnmkdm=N219904',
            data=form_data).json()
        # print(a)
        return a
