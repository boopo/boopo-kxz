import requests
'''
此文件包含融合门户的所有请求函数，带上cookie就可以使用
'''

url_balance = 'http://portal.cumt.edu.cn/ykt/balance'  # 校园卡余额(未跳转)
url_balance_re1 = 'http://ykt.cumt.edu.cn:8088/ias/prelogin?sysid=FWDT'  # 一卡通跳转1
url_balance_re2 = 'http://ykt.cumt.edu.cn/cassyno/index'  # 一卡通跳转2
url_balance_history = 'http://ykt.cumt.edu.cn/Report/GetPersonTrjn'  # 一卡通流水按时间查询
url_balance2 = 'http://portal.cumt.edu.cn/ykt/flow?flow_num=20'  # 校园卡按逆序查询(未跳转)
url_balance_charge = 'http://ykt.cumt.edu.cn/User/Account_Pay'  # 校园卡充值(慎用！！！)
url_library = 'http://portal.cumt.edu.cn/portal/api/v1/api/http/40'  # 图书简单信息(未跳转)
url_library_re = 'http://121.248.104.188:8080/CASSSO/login.jsp'  # 图书馆认证跳转
url_library_Loan = 'https://findcumt.libsp.com/find/loanInfo/loanList'  # 图书馆当前借阅信息
url_library_loan_history = 'https://findcumt.libsp.com/find/loanInfo/loanHistoryList'  # 图书馆历史借阅信息
url_library_favorite = 'https://findcumt.libsp.com/find/favorites/recordList'  # 图书馆收藏列表


def header_normal_generator(cookie):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie
    }
    return header


def get_balance_simple(cookie):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie
    }
    r = requests.get(url=url_balance, headers=header)
    if r.json():
        return r.json()
    else:
        return False


def get_balance_history_simple(cookie):
    r = requests.get(url=url_balance2, headers=header_normal_generator(cookie))
    if r.json():
        return r.json()
    else:
        return False


def get_user_card_number(cookie):
    r = get_balance_simple(cookie)
    if r:
        account = r['data']['ZH']
        return account
    else:
        return False


def get_balance_history_pro(cookie, hall_cookie, sdata, edate, page='1',
                            rows='15'):
    account = get_user_card_number(cookie)
    form_balance = {
        "sdate": sdata,
        "edate": edate,
        "account": account,
        "page": page,
        "rows": rows
    }
    r2 = requests.post(url=url_balance_history, headers=header_normal_generator(hall_cookie), data=form_balance)
    return r2.json()


def get_library_simple(cookie):
    r = requests.get(url=url_library, headers=header_normal_generator(cookie))
    if r.json():
        return r.json()
    else:
        return False


# account为卡号， tranamt单位为分，也就是100为1元
def get_balance_charge(cookie, hall_cookie, tranamt):
    account = get_user_card_number(cookie)
    # 以下为本次表单提交
    header = {
        "Referer": "http://ykt.cumt.edu.cn/Page/Page",
        "Cookie": hall_cookie
    }
    form_charge = {
        "account": account,
        "acctype": "23%23%23",
        "tranamt": tranamt,
        "qpwd": "",
        "paymethod": "2",
        "paytype": "%E4%BD%BF%E7%94%A8%E7%BB%91%E5%AE%9A%E7%9A%84%E9%BB%98%E8%AE%A4%E8%B4%A6%E5%8F%B7",
        "client_type": "web"
    }
    r3 = requests.post(url=url_balance_charge, headers=header, data=form_charge)
    if r3.text != '':
        return r3.json()
    else:
        return False


def header_jwt_generator(jwt):
    heeder = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 FireFox / 29.0",
        "X-Requested-With": "XMLHttpRequest",
        "jwtOpacAuth": jwt,
        "Referer": "https://findcumt.libsp.com/",
        "Connection": "close"
    }
    return heeder


def get_library_list(jwt_cookie, page='1', rows='20'):  # page 页吗 rows 每页行数
    form = {
        "page": page,
        "rows": rows
    }
    r = requests.post(url=url_library_Loan, headers=header_jwt_generator(jwt_cookie), json=form, verify=False)
    return r.json()


def get_library_history_list(jwt_cookie, page='1', rows='20'):
    form = {
        "page": page,
        "rows": rows
    }
    r = requests.post(url=url_library_loan_history, headers=header_jwt_generator(jwt_cookie), json=form, verify=False)
    return r.json()


def get_library_favorite(jwt_cookie, page='1', rows='10'):
    form = {
        "favoritesId": "",
        "page": page,
        "rows": rows,
        "searchField": "title",
        "searchFieldContent": ""
    }
    r = requests.post(url=url_library_favorite, headers=header_jwt_generator(jwt_cookie), json=form, verify=False)
    return r.json()
