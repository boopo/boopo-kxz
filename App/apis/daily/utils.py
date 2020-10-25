import requests
import re
from bs4 import BeautifulSoup
headers = {

    "Host": "www.cumt.edu.cn",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"

}


def pc(home, num):
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

def get_home_image():  # 获取矿大官网首页轮播图
    url = "http://www.cumt.edu.cn"
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    parse = re.findall('src:"(.*?)",', r.text)
    l1 = []
    for single in parse:
        l1.append({"image-url": "http://www.cumt.edu.cn" + single})
    return l1


def get_multiple_sd_news(page=''):  # 视点新闻列表
    url = "http://www.cumt.edu.cn/19673/list" + page + ".htm"
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html5lib')
    rs = soup.find('ul', class_='news_list list2')
    l1 = []
    for single in rs.find_all('li'):
        l1.append({
            "title": single.a.text,
            "link": "http://www.cumt.edu.cn" + single.span.a['href'],
            "time": single.span.next_sibling.next_sibling.text
        })
    return l1


def get_single_sd_news(url):  # 单个视点新闻详情
    _headers = {

        "Host": "xwzx.cumt.edu.cn",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"

    }
    url = url
    r = requests.get(url=url, headers=_headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html5lib')
    rs = soup.find_all('p', style="text-indent:2em;text-align:left;font-size:16px;")  # 查询文章
    detail = soup.find('div', class_='news_xx')  # 查询作者，时间，浏览次数
    detail_detail = detail.find_all('span')  # 同一标签先所有子标签，
    foot = soup.find('p', class_='arti_metas')  # 同上
    foot_detail = foot.find_all('span')

    dd = []  # detail_detail 存储 作者 时间 浏览次数
    fd = []  # foot_detail  存储 来源 审核 编辑
    content = []  # 存储文章
    for single in detail_detail:  # 遍历
        dd.append(single.text)
    for single in foot_detail:
        fd.append(single.text)
    for single in rs:
        content.append(single.text)
    # json 序列化
    ls = {
        "title": soup.title.text,
        "header": {
            "author": dd[1],
            "time": dd[3]
        },
        "about": fd,
        "content": content

    }
    return ls


def get_multiple_xs_news(page=''):  # 学术聚焦列表
    url = "http://www.cumt.edu.cn/19674/list" + page + ".htm"
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html5lib')
    rs = soup.find('ul', class_="news_list list2")
    rs_detail = rs.find_all('li')
    rd = []
    for single in rs_detail:
        rd.append({
            "title": single.span.a['title'],
            "link": "http://www.cumt.edu.cn" + single.span.a['href'],
            "time": single.span.next_sibling.next_sibling.text
        })
    return rd


def get_single_xs_news(url):  # 单个学术学术聚焦详情
    __headers = {
        "Host": "xwzx.cumt.edu.cn",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"

    }
    r = requests.get(url=url, headers=__headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html5lib")
    # rs_img = soup.find('p', style="text-align:center;")
    # 图片不用了，这里有两张，一个原图一个预览图
    rs = soup.find(attrs={'name': re.compile('description')})
    l1 = {
        "title": soup.title.text,
        "content": rs['content']
    }
    return l1

def get_multiple_xx_news(page=''):  # 信息公告列表
    page = page
    url = "http://www.cumt.edu.cn/19678/list" + page + ".htm"
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html5lib')
    rs = soup.find_all('span', class_="news_title")
    l1 = []
    for single in rs:
        l1.append({
            "title": single.a.text,
            "link": "http://www.cumt.edu.cn" + single.a['href']
        })
    return l1

def get_single_rw_news(url):  # 单个人文讲堂详情
    url = url
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html5lib")

    rs = soup.find('div', class_='wp_articlecontent')
    rs_detail = rs.find_all('p')
    rd = []
    for single in rs_detail:
        txt = single.text
        txt = "".join(txt.split())
        if txt != '':  # if not 不行...
            rd.append(txt)
    return rd



def get_multiple_rw_news(page=''):  # 人文讲堂聚合查询
    url = "http://www.cumt.edu.cn/19677/list" + page + ".htm"
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html5lib')
    rs = soup.find('ul', class_="news_list list2")
    l1 = []
    for single in rs.find_all('li'):
        l1.append({
            "title": single.span.a['title'],
            "time": single.span.next_sibling.next_sibling.text,
            "detail": get_single_rw_news("http://www.cumt.edu.cn" + single.span.a['href'])  # 在次查询单个人文讲堂信息
        })
    return l1


