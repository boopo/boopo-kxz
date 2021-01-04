def marshal_simple_balance(data):
    d1 = {
        "cardNumber": data['data']['ZH'],
        "balance": data['data']['YE']
    }
    return d1


def marshal_simple_library(data):
    d2 = {
        "curBorrowNum": data['data']['curBorrowNum']
    }
    return d2


def marshal_simple_balance_history(data):
    msg = data['data']
    l1 = []
    for a in msg:
        d1 = {
            "cardNumber": a['XGH'],
            "Type": a['JYLX'],
            "Location": a['ZDMC'],
            "name": a['SHMC'],
            "costMoney": a['JYE'],
            "balance": a['YE'],
            "time": a['JYSJ']
        }
        l1.append(d1)

    return l1


def marshal_library_list(data):
    msg = data['data']['searchResult']
    l1 = []
    for a in msg:
        d1 = {
            "title": a['title'],
            "loanData": a['loanDate'],
            "returnDate": a['normReturnDate'],
            "location": a['locationName'],
            "callNo": a['callNo']
        }
        l1.append(d1)
    return l1


def marshal_library_history_list(data):
    msg = data['data']['searchResult']
    l1 = []
    for a in msg:
        d1 = {
            "title": a['title'],
            "loanDate": a['loanDate'],
            "returnDate": a['returnDate'],
            "location": a['locationName']
        }
        l1.append(d1)
    num = data['data']['numFound']
    l2 = {
        "num": num,
        "libList": l1

    }
    return l2
