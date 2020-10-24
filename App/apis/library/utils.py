import requests

headers = {
    "groupCode": "200069",
    "Referer": "https://findcumt.libsp.com/"
}


def get_book(keyword):  # 图书聚合查询
    url = 'https://findcumt.libsp.com/find/unify/search'  # 图书馆查询接口
    s_json = {
        "searchFieldContent": keyword,
        "rows": 5,
        "searchField": "keyWord"
    }
    r = requests.post(url, headers=headers, json=s_json)
    data = r.json()
    book_list = []
    for single in data['data']['searchResult']:
        if not single['groupECount']:
            single['groupECount'] = 0
        a = {
            "book_id": single['recordId'],
            "name": single['title'],
            "author": single['author'],
            "publisher": single['publisher'],
            "isbn": single['isbn'],
            "pcount": single['groupPhysicalCount'],
            "ecount": single['groupECount'],
            "search_code": single['callNoOne'],
            "image": get_image(single['isbn'], single['title']),
            "status_now": check_book(single['recordId'])
        }
        book_list.append(a)
    return book_list


def check_book(_id):  # 检查馆藏
    url = 'https://findcumt.libsp.com/find/physical/groupitems'
    t_json = {
        "rows": 20,
        "recordId": _id
    }
    r = requests.post(url, headers=headers, json=t_json)
    data = r.json()
    book_status_list = []
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
    return r.json()['data']
    # print(r.json()['data'])
