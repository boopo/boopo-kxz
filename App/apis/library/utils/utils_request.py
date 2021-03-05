import requests

from App.ext import redis_client, redis_third

headers = {
    "groupCode": "200069",
    "Referer": "https://findcumt.libsp.com/"
}


def get_book(keyword, page, row):  # 图书聚合查询
    url = 'https://findcumt.libsp.com/find/unify/search'  # 图书馆查询接口
    s_json = {
        "searchFieldContent": keyword,
        "rows": row,
        "page": page,
        "searchField": "keyWord"
    }
    r = requests.post(url, headers=headers, json=s_json)
    data = r.json()
    book_list = []
    for single in data['data']['searchResult']:
        if not single['onShelfCountI']:
            onshelf = False
        else:
            onshelf = True
        if not single['groupECount']:
            single['groupECount'] = 0
        if not single['groupPhysicalCount']:
            single['groupPhysicalCount'] = 0
        if not single['isbn']:
            single['isbn'] = ''

        a = {
            "bookId": single['recordId'],
            "name": single['title'],
            "author": single['author'],
            "publisher": single['publisher'],
            "isbn": single['isbn'],
            "pcount": single['groupPhysicalCount'],
            "ecount": single['groupECount'],
            "searchCode": single['callNoOne'],
            #http://127.0.0.1:5000/lib/image?isbn=7-222-02563-4&title=平凡的世界
            #https://api.kxz.atcumt.com/lib'
            "image": get_image_pro(single['isbn'],single['title']),
            "statusNow": 'https://api.kxz.atcumt.com/lib/status?id='+str(single['recordId']),
            "status": onshelf
        }
        book_list.append(a)
        l1 = {
            "all": data['data']['numFound'],
            "bookList": book_list
        }
    return l1


def check_book(_id):  # 检查馆藏
    url = 'https://findcumt.libsp.com/find/physical/groupitems'
    t_json = {
        "rows": 20,
        "recordId": _id
    }
    r = requests.post(url, headers=headers, json=t_json)
    data = r.json()
    book_status_list = []
    # print(data['data'])
    for single in data['data']:
        book_code = single['barcode']
        location = single['locationName']
        current = single['processType']
        a = {"bookcode": book_code, "location": location, "current": current}
        book_status_list.append(a)
    return book_status_list
    # print(book_status_list)


def get_image(isbn, title):  # 获取图书封面
    url = 'https://findcumt.libsp.com/find/book/getDuxiuImageUrl'
    params = {
        "isbn": isbn,
        "title": title
    }
    r = requests.get(url=url, params=params)
    if not r.json()['data']:
        return 'null'
    else:
        return r.json()['data']

def get_image_pro(isbn, title):
    if redis_client.get(isbn+title):
        return str(redis_third.get(isbn+title), encoding='utf-8')
        #return str(redis_client.get(isbn+title), encoding='utf-8')
    else:
        url =get_image(isbn, title)
        redis_third.set(name=isbn+title,value=url)
        #redis_client.set(name=isbn+title,value=url)
        return url

