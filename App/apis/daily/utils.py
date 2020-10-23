

import requests
import re




def pc(home,num):
    host = "http://www.houqinbao.com/hydropower/index.php?rebind=1&m=PayWeChat&c=Index&a=bingding&token=&openid=oUiRowd11jcJJHzVjZHgbb7OyWqE&schoolcode=13579&payopenid="
    # home = '梅2楼'
    # num = 'B4222'
    r = requests.get(host)
    cook = r.cookies                                 #获取返回的cookiejar对象
    tst = requests.utils.dict_from_cookiejar(cook)   #将cookiejar转换为字典形式的数据
    cookie = tst['PHPSESSID']
    headers = {
        'Cookie': cookie,
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {'flatname': home, 'roomname': num}

    try:
        response = requests.post("http://www.houqinbao.com/hydropower/index.php?m=PayWeChat&c=IndexKd&a=find&schoolcode=13579",headers=headers, data=data)
        df = re.findall("dushu\":(.*?),", response.text )
        return df[0]
    except:
        return "null"