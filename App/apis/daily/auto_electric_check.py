import re

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
    "X-Requested-With": "XMLHttpRequest"
}


def df_pc(home, num):  # 爬电费
    host = "http://www.houqinbao.com/hydropower/index.php?rebind=1&m=PayWeChat&c=Index&a=bingding&token=&openid" \
           "=oUiRowd11jcJJHzVjZHgbb7OyWqE&schoolcode=13579&payopenid= "
    # home = '梅2楼'
    # num = 'B4222'
    r = requests.get(host)
    cook = r.cookies  # 获取返回的cookiejar对象
    tst = requests.utils.dict_from_cookiejar(cook)  # 将cookiejar转换为字典形式的数据
    cookie = tst['PHPSESSID']
    headers = {
        'Cookie': cookie,
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {'flatname': home, 'roomname': num}

    try:
        response = requests.post \
            ("http://www.houqinbao.com/hydropower/index.php?m=PayWeChat&c=IndexKd&a=find&schoolcode=13579"
             , headers=headers, data=data)
        df = re.findall("dushu\":(.*?),", response.text)
        return df[0]
    except:
        return "null"


# 此Suids与ids类似，只是一个登录教务系统，一个登录公寓管理(vpn)
class SuIds():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

    def login(self):
        self.err = []
        r = self.session.get(
            url='http://ids.cumt.edu.cn/authserver/login?service=http%3A%2F%2Fgy.cumt.edu.cn%2Fepstar%2Flogin%2Findex.jsp',
            headers=headers)
        # print('第一次GET', r.cookies)
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
            url='http://ids.cumt.edu.cn/authserver/login?service=http%3A%2F%2Fgy.cumt.edu.cn%2Fepstar%2Flogin%2Findex.jsp',
            data=From_Data, headers=headers, allow_redirects=False)
        # print("111111", self.session.cookies)

        self.err.append(q.status_code)
        # q.encoding = q.apparent_encoding

        if q.status_code == 302:
            self.cookies = q.cookies
            #      print(q.cookies)
            # print('第二次POST', q.cookies)
            text = q.headers['Location']
            # print(text)
            s = self.session.get(url=text)
            # print("self..cookie", self.session.cookies)
            _cookies = self.session.cookies
            aa = []
            for single in _cookies:
                aa.append(single.value)
            # print("宿舍专用cookie", aa[0])
            # print('第三次GET', s.cookies)
            token = 'JSESSIONID=' + aa[0]
            # 从下面开始登录公寓管理网站，并利用宿舍楼和楼号查询电费
            s_url = 'http://gy.cumt.edu.cn/epstar/app/getxml.jsp'
            s_headers = {
                "Cookie": token,
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "http://gy.cumt.edu.cn/epstar/web/applications/SWMS/SS/XSSSXX/ssxx.jsp?XSLBDM=",
                "Host": "gy.cumt.edu.cn"
            }
            s_body = {
                "_KEY": "bWFpbm9iaj1TV01TL1NTR0xaWFQvUlpHTC9WX1NTX1NTWFhTVCZlbmNGaWVsZHM9WFZsOVRVMTlUVTFoWVUxUTZYJmVuY0ZpbHRlcj1YVmw5VFUxOVRVMWhZVTFRNk1UMHhYJmVuY09yZGVyQnk9WFZsOVRVMTlUVTFoWVUxUTZYJkNoZWNrRlA9bm8mdW5kZWZpbmVk"
            }
            r = requests.post(url=s_url, headers=s_headers, data=s_body)
            r.encoding = r.apparent_encoding
            home = re.findall("<SSL_displayvalue>(.*?)</SSL_displayvalue>", r.text)
            num = re.findall('<FJH>(.*?)</FJH>', r.text)  # 获取宿舍楼和宿舍号
            data = df_pc(home[0][9:-3], num[0][9:-3])
            return data
        if q.status_code == 200:
            soup_obj = BeautifulSoup(q.text, "html5lib")
            tips = soup_obj.find_all(id="msg")
            span = tips[0].string
            print(span)
            if span == "您提供的用户名或者密码有误。":
                return False
        else:
            return False
