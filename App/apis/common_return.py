# 测试账号 格式化返回


def check_root(username, password):
    if username == "12345678" and password == '12345678':
        return True

'''
以下为 矿小助的测试账号
      格式化数据返回
'''

class testUser:
    @staticmethod
    def kb_return():
        data = {
    "status": 200,
    "msg": "抓取成功",
    "data": {
        "kbList": [
            {
                "cd_id": "sgw0000698",
                "cdmc": "博3-B103",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-2节",
                "jcor": "1-4",
                "jcs": "1-2",
                "jgh_id": "040273",
                "jgpxzd": "1",
                "jxb_id": "A7DE2277E587002CE053C0A86D5C3E90",
                "jxbmc": "电工技术与电子技术A(2)-0005",
                "jxbsftkbj": "1",
                "kch_id": "36FBE9C1C9A4005CE053C0A86662005C",
                "kclb": "A",
                "kcmc": "电工技术与电子技术A(2)",
                "kcxszc": "讲课:56",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "3",
                "oldzc": "1007",
                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,
                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "3",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0,

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "芦楠楠",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "1",
                "xqjmc": "星期一",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-4周,6-10周",
                "zcmc": "讲师",
                "zhxs": "6",
                "zxs": "56",
                "zyfxmc": "无方向",
                "zzrl": "76"
            },
            {
                "cd_id": "sgw0001000",
                "cdmc": "计-25机房",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-4节",
                "jcor": "1-4",
                "jcs": "1-4",
                "jgh_id": "040257",
                "jgpxzd": "1",
                "jxb_id": "A6D3BEAD9A790324E053C0A86D5C397C",
                "jxbmc": "程序设计综合实践-0007",
                "jxbsftkbj": "0",
                "kch_id": "P08135",
                "kclb": "C",
                "kcmc": "程序设计综合实践",
                "kcxszc": "实践:3",
                "kcxz": "实践",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "15",
                "oldzc": "516096",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "9",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0,

                },
                "xf": "3",
                "xkbz": "无",
                "xm": "李鸣",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "1",
                "xqjmc": "星期一",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "03",
                "xslxbj": "●",
                "year": "2021",
                "zcd": "14-19周",
                "zcmc": "副教授",
                "zhxs": "8",
                "zxs": "48",
                "zyfxmc": "无方向",
                "zzrl": "68"
            },
            {
                "cd_id": "sgw0001051",
                "cdmc": "博1-B502",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "5-6节",
                "jcor": "5-6",
                "jcs": "5-6",
                "jgh_id": "100217",
                "jgpxzd": "1",
                "jxb_id": "A947046FFA470186E053C0A86D5D7FD4",
                "jxbmc": "线性代数(16版，-0042",
                "jxbsftkbj": "1",
                "kch_id": "M10811",
                "kclb": "A",
                "kcmc": "线性代数(16版，",
                "kcxszc": "讲课:38,实验:2",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "48",
                "oldzc": "4047",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "8",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.5",
                "xkbz": "无",
                "xm": "王志俊",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "1",
                "xqjmc": "星期一",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-4周,7-12周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "40",
                "zyfxmc": "无方向",
                "zzrl": "110"
            },
            {
                "cd_id": "sgw0001051",
                "cdmc": "博1-B502",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "5-6节",
                "jcor": "5-6",
                "jcs": "5-6",
                "jgh_id": "100112",
                "jgpxzd": "1",
                "jxb_id": "A947046FFA470186E053C0A86D5D7FD4",
                "jxbmc": "线性代数(16版，-0042",
                "jxbsftkbj": "1",
                "kch_id": "M10811",
                "kclb": "A",
                "kcmc": "线性代数(16版，",
                "kcxszc": "讲课:38,实验:2",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "48",
                "oldzc": "32",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "8",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": ""

                },
                "xf": "2.5",
                "xkbz": "无",
                "xm": "魏琦瑛",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "1",
                "xqjmc": "星期一",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "6周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "40",
                "zyfxmc": "无方向",
                "zzrl": "110"
            },
            {
                "cd_id": "sgw0001227",
                "cdmc": "博1-A102",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "5-6节",
                "jcor": "5-6",
                "jcs": "5-6",
                "jgh_id": "5D5A38AD24C0036AE053C0A86D5CB36B",
                "jgpxzd": "1",
                "jxb_id": "A815BE126652024AE053C0A86D5C87BA",
                "jxbmc": "形势与政策-0006",
                "jxbsftkbj": "0",
                "kch_id": "36E99854DEA00350E053C0A866620350",
                "kclb": "A",
                "kcmc": "形势与政策",
                "kcxszc": "讲课:32",
                "kcxz": "必修",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "48",
                "oldzc": "520192",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "2",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": ""

                },
                "xf": "2",
                "xkbz": "无",
                "xm": "孙凌杉",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "1",
                "xqjmc": "星期一",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "13-19周",
                "zhxs": "4",
                "zxs": "32",
                "zyfxmc": "无方向",
                "zzrl": "169"
            },
            {
                "cd_id": "sgw0000458",
                "cdmc": "博1-C101",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "7-8节",
                "jcor": "7-8",
                "jcs": "7-8",
                "jgh_id": "4FBB16D2100203D8E053C0A8666203D8",
                "jgpxzd": "1",
                "jxb_id": "A8A31A0C08880358E053C0A86D5C0A28",
                "jxbmc": "毛泽东思想和中国特色社会主义理论体系概论-0017",
                "jxbsftkbj": "0",
                "kch_id": "6ABAFD3AD719028AE053C0A86D5DA458",
                "kclb": "A",
                "kcmc": "毛泽东思想和中国特色社会主义理论体系概论",
                "kcxszc": "讲课:48",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "192",
                "oldzc": "32750",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "5",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "3",
                "xkbz": "无",
                "xm": "高建明",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "1",
                "xqjmc": "星期一",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "2-4周,6-15周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "48",
                "zyfxmc": "无方向",
                "zzrl": "144"
            },
            {
                "cd_id": "sgw0000698",
                "cdmc": "博3-B103",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-2节",
                "jcor": "1-2",
                "jcs": "1-2",
                "jgh_id": "040273",
                "jgpxzd": "1",
                "jxb_id": "A7DE2277E587002CE053C0A86D5C3E90",
                "jxbmc": "电工技术与电子技术A(2)-0005",
                "jxbsftkbj": "1",
                "kch_id": "36FBE9C1C9A4005CE053C0A86662005C",
                "kclb": "A",
                "kcmc": "电工技术与电子技术A(2)",
                "kcxszc": "讲课:56",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "3",
                "oldzc": "1007",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "3",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "芦楠楠",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-4周,6-10周",
                "zcmc": "讲师",
                "zhxs": "6",
                "zxs": "56",
                "zyfxmc": "无方向",
                "zzrl": "76"
            },
            {
                "cd_id": "sgw0000653",
                "cdmc": "博5-C302",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "3-4节",
                "jcor": "3-4",
                "jcs": "3-4",
                "jgh_id": "120150",
                "jgpxzd": "1",
                "jxb_id": "A7E3E68B386702B4E053C0A86D5D0F0D",
                "jxbmc": "2-综合英语（3）-0077",
                "jxbsftkbj": "0",
                "kch_id": "P12403",
                "kclb": "B",
                "kcmc": "综合英语（3）",
                "kcxszc": "讲课:32",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "12",
                "oldzc": "495",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "11",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "韦炜",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-4周,6-9周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "36",
                "zyfxmc": "无方向",
                "zzrl": "65"
            },
            {
                "cd_id": "sgw0000166",
                "cdmc": "博5-B206",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "3-4节",
                "jcor": "3-4",
                "jcs": "3-4",
                "jgh_id": "120119",
                "jgpxzd": "1",
                "jxb_id": "A7EB3E36F3200358E053C0A86D5C0C2F",
                "jxbmc": "2-英语实践（3）-0072",
                "jxbsftkbj": "0",
                "kch_id": "P12411",
                "kclb": "B",
                "kcmc": "英语实践（3）",
                "kcxszc": "实践:32",
                "kcxz": "实践",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "12",
                "oldzc": "523264",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },
                "rk": "12",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {
                   "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "1.0",
                "xkbz": "无",
                "xm": "苗媛",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "03",
                "xslxbj": "●",
                "year": "2021",
                "zcd": "11-19周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "36",
                "zyfxmc": "无方向",
                "zzrl": "65"
            },
            {
                "cd_id": "sgw0001151",
                "cdmc": "博4-A101",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "5-6节",
                "jcor": "5-6",
                "jcs": "5-6",
                "jgh_id": "080080",
                "jgpxzd": "1",
                "jxb_id": "A6D4EF6E4ECB010CE053C0A86D5DA2DF",
                "jxbmc": "计算机组成原理-0006",
                "jxbsftkbj": "0",
                "kch_id": "M08202",
                "kclb": "A",
                "kcmc": "计算机组成原理",
                "kcxszc": "讲课:40",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "48",
                "oldzc": "523776",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "7",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.5",
                "xkbz": "无",
                "xm": "王莉2",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "10-19周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "40",
                "zyfxmc": "无方向",
                "zzrl": "83"
            },
            {
                "cd_id": "sgw0000685",
                "cdmc": "图-107",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "301279",
                "jgpxzd": "1",
                "jxb_id": "A7388D46EE0C007AE053C0A86D5C3A1E",
                "jxbmc": "文献检索与利用-0001",
                "jxbsftkbj": "1",
                "kch_id": "4198EC21753D0158E053C0A866620158",
                "kclb": "一般课程",
                "kcmc": "文献检索与利用",
                "kcxszc": "讲课:16,实验:16",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "7",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "4",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "武保民",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周",
                "zcmc": "副研究馆员",
                "zhxs": "2",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000685",
                "cdmc": "图-107",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "301066",
                "jgpxzd": "1",
                "jxb_id": "A7388D46EE0C007AE053C0A86D5C3A1E",
                "jxbmc": "文献检索与利用-0001",
                "jxbsftkbj": "1",
                "kch_id": "4198EC21753D0158E053C0A866620158",
                "kclb": "一般课程",
                "kcmc": "文献检索与利用",
                "kcxszc": "讲课:16,实验:16",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "616",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "4",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0,

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "汪媛",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "4-6周(双),7周,10周",
                "zcmc": "副研究馆员",
                "zhxs": "2",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000685",
                "cdmc": "图-107",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "302345",
                "jgpxzd": "1",
                "jxb_id": "A7388D46EE0C007AE053C0A86D5C3A1E",
                "jxbmc": "文献检索与利用-0001",
                "jxbsftkbj": "1",
                "kch_id": "4198EC21753D0158E053C0A866620158",
                "kclb": "一般课程",
                "kcmc": "文献检索与利用",
                "kcxszc": "讲课:16,实验:16",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "384",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "4",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "王玲玲",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "8-9周",
                "zcmc": "馆员",
                "zhxs": "2",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000152",
                "cdmc": "博4-C307",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "070055",
                "jgpxzd": "1",
                "jxb_id": "A4DCD3D7AE28028AE053C0A86D5D7033",
                "jxbmc": "生态文化影视鉴赏-0002",
                "jxbsftkbj": "1",
                "kch_id": "Q07411",
                "kclb": "一般课程",
                "kcmc": "生态文化影视鉴赏",
                "kcxszc": "讲课:32",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "261120",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "13",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2",
                "xkbz": "无",
                "xm": "程伟",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "2",
                "xqjmc": "星期二",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "11-18周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "32",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000458",
                "cdmc": "博1-C101",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-2节",
                "jcor": "1-2",
                "jcs": "1-2",
                "jgh_id": "100196",
                "jgpxzd": "1",
                "jxb_id": "A7395D746B2202B0E053C0A86D5C9396",
                "jxbmc": "大学物理B（2）-0010",
                "jxbsftkbj": "0",
                "kch_id": "G10904",
                "kclb": "A",
                "kcmc": "大学物理B（2）",
                "kcxszc": "讲课:56",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "3",
                "oldzc": "32751",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "6",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0,

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "唐芙蓉",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "3",
                "xqjmc": "星期三",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-4周,6-15周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "60",
                "zyfxmc": "无方向",
                "zzrl": "121"
            },
            {
                "cd_id": "sgw0001227",
                "cdmc": "博1-A102",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "3-4节",
                "jcor": "3-4",
                "jcs": "3-4",
                "jgh_id": "5D5A38AD24C0036AE053C0A86D5CB36B",
                "jgpxzd": "1",
                "jxb_id": "A815BE126652024AE053C0A86D5C87BA",
                "jxbmc": "形势与政策-0006",
                "jxbsftkbj": "0",
                "kch_id": "36E99854DEA00350E053C0A866620350",
                "kclb": "A",
                "kcmc": "形势与政策",
                "kcxszc": "讲课:32",
                "kcxz": "必修",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "12",
                "oldzc": "523264",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "2",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2",
                "xkbz": "无",
                "xm": "孙凌杉",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "3",
                "xqjmc": "星期三",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "11-19周",
                "zhxs": "4",
                "zxs": "32",
                "zyfxmc": "无方向",
                "zzrl": "169"
            },
            {
                "cd_id": "sgw0000925",
                "cdmc": "博2-B201",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "040273",
                "jgpxzd": "1",
                "jxb_id": "A7DE2277E587002CE053C0A86D5C3E90",
                "jxbmc": "电工技术与电子技术A(2)-0005",
                "jxbsftkbj": "1",
                "kch_id": "36FBE9C1C9A4005CE053C0A86662005C",
                "kclb": "A",
                "kcmc": "电工技术与电子技术A(2)",
                "kcxszc": "讲课:56",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "2048",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "3",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "芦楠楠",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "3",
                "xqjmc": "星期三",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "12周",
                "zcmc": "讲师",
                "zhxs": "6",
                "zxs": "56",
                "zyfxmc": "无方向",
                "zzrl": "76"
            },
            {
                "cd_id": "sgw0000524",
                "cdmc": "博1-B503",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-2节",
                "jcor": "1-4",
                "jcs": "1-2",
                "jgh_id": "100217",
                "jgpxzd": "1",
                "jxb_id": "A947046FFA470186E053C0A86D5D7FD4",
                "jxbmc": "线性代数(16版，-0042",
                "jxbsftkbj": "1",
                "kch_id": "M10811",
                "kclb": "A",
                "kcmc": "线性代数(16版，",
                "kcxszc": "讲课:38,实验:2",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "3",
                "oldzc": "2023",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "8",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.5",
                "xkbz": "无",
                "xm": "王志俊",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周,6-11周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "40",
                "zyfxmc": "无方向",
                "zzrl": "110"
            },
            {
                "cd_id": "sgw0001000",
                "cdmc": "计-25机房",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-4节",
                "jcor": "1-4",
                "jcs": "1-4",
                "jgh_id": "040257",
                "jgpxzd": "1",
                "jxb_id": "A6D3BEAD9A790324E053C0A86D5C397C",
                "jxbmc": "程序设计综合实践-0007",
                "jxbsftkbj": "0",
                "kch_id": "P08135",
                "kclb": "C",
                "kcmc": "程序设计综合实践",
                "kcxszc": "实践:3",
                "kcxz": "实践",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "15",
                "oldzc": "516096",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "9",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "3",
                "xkbz": "无",
                "xm": "李鸣",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "03",
                "xslxbj": "●",
                "year": "2021",
                "zcd": "14-19周",
                "zcmc": "副教授",
                "zhxs": "8",
                "zxs": "48",
                "zyfxmc": "无方向",
                "zzrl": "68"
            },
            {
                "cd_id": "sgw0000698",
                "cdmc": "博3-B103",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "3-4节",
                "jcor": "1-4",
                "jcs": "3-4",
                "jgh_id": "040273",
                "jgpxzd": "1",
                "jxb_id": "A7DE2277E587002CE053C0A86D5C3E90",
                "jxbmc": "电工技术与电子技术A(2)-0005",
                "jxbsftkbj": "1",
                "kch_id": "36FBE9C1C9A4005CE053C0A86662005C",
                "kclb": "A",
                "kcmc": "电工技术与电子技术A(2)",
                "kcxszc": "讲课:56",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "12",
                "oldzc": "999",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "3",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "芦楠楠",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周,6-10周",
                "zcmc": "讲师",
                "zhxs": "6",
                "zxs": "56",
                "zyfxmc": "无方向",
                "zzrl": "76"
            },
            {
                "cd_id": "49350D138FFD03FEE053C0A8666203FE",
                "cdmc": "体育场",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "5-6节",
                "jcor": "5-6",
                "jcs": "5-6",
                "jgh_id": "130055",
                "jgpxzd": "1",
                "jxb_id": "A8CE767603CF00D8E053C0A86D5DB1BA",
                "jxbmc": "羽毛球(3)-0010",
                "jxbsftkbj": "0",
                "kch_id": "13053",
                "kclb": "一般课程",
                "kcmc": "羽毛球(3)",
                "kcxszc": "讲课:24",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "48",
                "oldzc": "16359",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "1",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "0.5",
                "xkbz": "无",
                "xm": "张晓侠",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周,6-14周",
                "zcmc": "副教授",
                "zhxs": "2",
                "zxs": "24",
                "zyfxmc": "无方向",
                "zzrl": "42"
            },
            {
                "cd_id": "sgw0000458",
                "cdmc": "博1-C101",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "7-8节",
                "jcor": "7-8",
                "jcs": "7-8",
                "jgh_id": "4FBB16D2100203D8E053C0A8666203D8",
                "jgpxzd": "1",
                "jxb_id": "A8A31A0C08880358E053C0A86D5C0A28",
                "jxbmc": "毛泽东思想和中国特色社会主义理论体系概论-0017",
                "jxbsftkbj": "0",
                "kch_id": "6ABAFD3AD719028AE053C0A86D5DA458",
                "kclb": "A",
                "kcmc": "毛泽东思想和中国特色社会主义理论体系概论",
                "kcxszc": "讲课:48",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "192",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "5",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": ""

                },
                "xf": "3",
                "xkbz": "无",
                "xm": "高建明",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "2-3周,6-14周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "48",
                "zyfxmc": "无方向",
                "zzrl": "144"
            },
            {
                "cd_id": "sgw0000685",
                "cdmc": "图-107",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "301279",
                "jgpxzd": "1",
                "jxb_id": "A7388D46EE0C007AE053C0A86D5C3A1E",
                "jxbmc": "文献检索与利用-0001",
                "jxbsftkbj": "1",
                "kch_id": "4198EC21753D0158E053C0A866620158",
                "kclb": "一般课程",
                "kcmc": "文献检索与利用",
                "kcxszc": "讲课:16,实验:16",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "7",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "4",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "武保民",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周",
                "zcmc": "副研究馆员",
                "zhxs": "2",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000685",
                "cdmc": "图-107",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "301066",
                "jgpxzd": "1",
                "jxb_id": "A7388D46EE0C007AE053C0A86D5C3A1E",
                "jxbmc": "文献检索与利用-0001",
                "jxbsftkbj": "1",
                "kch_id": "4198EC21753D0158E053C0A866620158",
                "kclb": "一般课程",
                "kcmc": "文献检索与利用",
                "kcxszc": "讲课:16,实验:16",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "288",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "4",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0
                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "汪媛",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "6周,9周",
                "zcmc": "副研究馆员",
                "zhxs": "2",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000685",
                "cdmc": "图-107",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "302345",
                "jgpxzd": "1",
                "jxb_id": "A7388D46EE0C007AE053C0A86D5C3A1E",
                "jxbmc": "文献检索与利用-0001",
                "jxbsftkbj": "1",
                "kch_id": "4198EC21753D0158E053C0A866620158",
                "kclb": "一般课程",
                "kcmc": "文献检索与利用",
                "kcxszc": "讲课:16,实验:16",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "192",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "4",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0,

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "王玲玲",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "7-8周",
                "zcmc": "馆员",
                "zhxs": "2",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000152",
                "cdmc": "博4-C307",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "070055",
                "jgpxzd": "1",
                "jxb_id": "A4DCD3D7AE28028AE053C0A86D5D7033",
                "jxbmc": "生态文化影视鉴赏-0002",
                "jxbsftkbj": "1",
                "kch_id": "Q07411",
                "kclb": "一般课程",
                "kcmc": "生态文化影视鉴赏",
                "kcxszc": "讲课:32",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "244736",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "13",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2",
                "xkbz": "无",
                "xm": "程伟",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "11-14周,16-18周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "32",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000152",
                "cdmc": "博4-C307",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "9-10节",
                "jcor": "9-10",
                "jcs": "9-10",
                "jgh_id": "070054",
                "jgpxzd": "1",
                "jxb_id": "A4DCD3D7AE28028AE053C0A86D5D7033",
                "jxbmc": "生态文化影视鉴赏-0002",
                "jxbsftkbj": "1",
                "kch_id": "Q07411",
                "kclb": "一般课程",
                "kcmc": "生态文化影视鉴赏",
                "kcxszc": "讲课:32",
                "kcxz": "公选",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "768",
                "oldzc": "16384",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "13",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2",
                "xkbz": "无",
                "xm": "孟庆俊",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "4",
                "xqjmc": "星期四",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "15周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "32",
                "zyfxmc": "无方向",
                "zzrl": "60"
            },
            {
                "cd_id": "sgw0000653",
                "cdmc": "博5-C302",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-2节",
                "jcor": "1-2",
                "jcs": "1-2",
                "jgh_id": "120150",
                "jgpxzd": "1",
                "jxb_id": "A7E3E68B386702B4E053C0A86D5D0F0D",
                "jxbmc": "2-综合英语（3）-0077",
                "jxbsftkbj": "0",
                "kch_id": "P12403",
                "kclb": "B",
                "kcmc": "综合英语（3）",
                "kcxszc": "讲课:32",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "3",
                "oldzc": "503",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,
                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "11",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.0",
                "xkbz": "无",
                "xm": "韦炜",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "5",
                "xqjmc": "星期五",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周,5-9周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "36",
                "zyfxmc": "无方向",
                "zzrl": "65"
            },
            {
                "cd_id": "sgw0000166",
                "cdmc": "博5-B206",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-2节",
                "jcor": "1-2",
                "jcs": "1-2",
                "jgh_id": "120119",
                "jgpxzd": "1",
                "jxb_id": "A7EB3E36F3200358E053C0A86D5C0C2F",
                "jxbmc": "2-英语实践（3）-0072",
                "jxbsftkbj": "0",
                "kch_id": "P12411",
                "kclb": "B",
                "kcmc": "英语实践（3）",
                "kcxszc": "实践:32",
                "kcxz": "实践",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "3",
                "oldzc": "195584",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "12",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "1.0",
                "xkbz": "无",
                "xm": "苗媛",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "5",
                "xqjmc": "星期五",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "03",
                "xslxbj": "●",
                "year": "2021",
                "zcd": "11-16周,18周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "36",
                "zyfxmc": "无方向",
                "zzrl": "65"
            },
            {
                "cd_id": "sgw0000458",
                "cdmc": "博1-C101",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "3-4节",
                "jcor": "3-4",
                "jcs": "3-4",
                "jgh_id": "100196",
                "jgpxzd": "1",
                "jxb_id": "A7395D746B2202B0E053C0A86D5C9396",
                "jxbmc": "大学物理B（2）-0010",
                "jxbsftkbj": "0",
                "kch_id": "G10904",
                "kclb": "A",
                "kcmc": "大学物理B（2）",
                "kcxszc": "讲课:56",
                "kcxz": "必修",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "12",
                "oldzc": "32759",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "6",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "唐芙蓉",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "5",
                "xqjmc": "星期五",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "1-3周,5-15周",
                "zcmc": "副教授",
                "zhxs": "4",
                "zxs": "60",
                "zyfxmc": "无方向",
                "zzrl": "121"
            },
            {
                "cd_id": "sgw0001151",
                "cdmc": "博4-A101",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "5-6节",
                "jcor": "5-6",
                "jcs": "5-6",
                "jgh_id": "080080",
                "jgpxzd": "1",
                "jxb_id": "A6D4EF6E4ECB010CE053C0A86D5DA2DF",
                "jxbmc": "计算机组成原理-0006",
                "jxbsftkbj": "0",
                "kch_id": "M08202",
                "kclb": "A",
                "kcmc": "计算机组成原理",
                "kcxszc": "讲课:40",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "48",
                "oldzc": "458496",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "7",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0

                },
                "xf": "2.5",
                "xkbz": "无",
                "xm": "王莉2",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "5",
                "xqjmc": "星期五",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "9-16周,18-19周",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "40",
                "zyfxmc": "无方向",
                "zzrl": "83"
            },
            {
                "cd_id": "sgw0000665",
                "cdmc": "计-37机房",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "1-4节",
                "jcor": "1-4",
                "jcs": "1-4",
                "jgh_id": "080080",
                "jgpxzd": "1",
                "jxb_id": "A6D3E8117092020AE053C0A86D5D3CD2",
                "jxbmc": "计算机组成原理实验-0007",
                "jxbsftkbj": "0",
                "kch_id": "P08236",
                "kclb": "A",
                "kcmc": "计算机组成原理实验",
                "kcxszc": "实验:16",
                "kcxz": "实践",
                "khfsmc": "考查",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "15",
                "oldzc": "169984",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "10",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": ""

                },
                "xf": "0.5",
                "xkbz": "无",
                "xm": "王莉2",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "6",
                "xqjmc": "星期六",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "02",
                "xslxbj": "○",
                "year": "2021",
                "zcd": "12-13周,16-18周(双)",
                "zcmc": "讲师",
                "zhxs": "4",
                "zxs": "16",
                "zyfxmc": "无方向",
                "zzrl": "56"
            },
            {
                "cd_id": "sgw0000698",
                "cdmc": "博3-B103",
                "cxbj": "0",
                "date": "二○二一年三月六日",
                "dateDigit": "2021年3月6日",
                "dateDigitSeparator": "2021-3-6",
                "day": "6",
                "jc": "3-4节",
                "jcor": "1-4",
                "jcs": "3-4",
                "jgh_id": "040273",
                "jgpxzd": "1",
                "jxb_id": "A7DE2277E587002CE053C0A86D5C3E90",
                "jxbmc": "电工技术与电子技术A(2)-0005",
                "jxbsftkbj": "1",
                "kch_id": "36FBE9C1C9A4005CE053C0A86662005C",
                "kclb": "A",
                "kcmc": "电工技术与电子技术A(2)",
                "kcxszc": "讲课:56",
                "kcxz": "学科",
                "khfsmc": "考试",
                "kkzt": "1",
                "listnav": "false",
                "localeKey": "zh_CN",
                "month": "3",
                "oldjc": "12",
                "oldzc": "512",

                "pkbj": "1",
                "queryModel": {
                    "currentPage": 1,
                    "currentResult": 0,

                    "limit": 15,
                    "offset": 0,
                    "pageNo": 0,
                    "pageSize": 15,
                    "showCount": 10,
                    "sorts": [],
                    "totalCount": 0,
                    "totalPage": 0,
                    "totalResult": 0
                },

                "rk": "3",
                "rsdzjs": 0,
                "skfsmc": "面授讲课",
                "sxbj": "1",
                "totalResult": "0",
                "userModel": {

                    "roleCount": 0,
                    "roleKeys": "",
                    "roleValues": "",
                    "status": 0,

                },
                "xf": "3.5",
                "xkbz": "无",
                "xm": "芦楠楠",
                "xnm": "2020",
                "xqdm": "0",
                "xqh1": "2,",
                "xqh_id": "2",
                "xqj": "6",
                "xqjmc": "星期六",
                "xqm": "3",
                "xqmc": "南湖校区",
                "xsdm": "01",
                "xslxbj": "★",
                "year": "2021",
                "zcd": "10周",
                "zcmc": "讲师",
                "zhxs": "6",
                "zxs": "56",
                "zyfxmc": "无方向",
                "zzrl": "76"
            }
        ],
        "zckbsfxssj": "1",
        "sfxsd": "1",
        "xnxqsfkz": "false"
    }
}

        return data

    @staticmethod
    def grades_return():
        data ={
    "status": 200,
    "msg": "请求成功",
    "data": [
        {
            "courseName": "电工技术与电子技术A(1)",
            "xuefen": "2.5",
            "jidian": "4.5",
            "zongping": "92",
            "scoreDetail": [
                {
                    "name": "平时(50%)",
                    "score": "95.5"
                },
                {
                    "name": "期末(50%)",
                    "score": "89"
                },
                {
                    "name": "总评",
                    "score": "92"
                }
            ]
        },
        {
            "courseName": "电工技术与电子技术实验A(1)",
            "xuefen": "0.5",
            "jidian": "4.5",
            "zongping": "91",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "91"
                },
                {
                    "name": "总评",
                    "score": "91"
                }
            ]
        },
        {
            "courseName": "离散数学",
            "xuefen": "3",
            "jidian": "5.0",
            "zongping": "95",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "92"
                },
                {
                    "name": "期末(70%)",
                    "score": "96"
                },
                {
                    "name": "总评",
                    "score": "95"
                }
            ]
        },
        {
            "courseName": "数据结构",
            "xuefen": "3",
            "jidian": "4.0",
            "zongping": "87",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "90"
                },
                {
                    "name": "期末(70%)",
                    "score": "86"
                },
                {
                    "name": "总评",
                    "score": "87"
                }
            ]
        },
        {
            "courseName": "数据结构实验",
            "xuefen": "0.5",
            "jidian": "5.0",
            "zongping": "100",
            "scoreDetail": [
                {
                    "name": "平时(50%)",
                    "score": "100"
                },
                {
                    "name": "期末(50%)",
                    "score": "100"
                },
                {
                    "name": "总评",
                    "score": "100"
                }
            ]
        },
        {
            "courseName": "高等数学A（3）(16版，",
            "xuefen": "3",
            "jidian": "3.0",
            "zongping": "80",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "97"
                },
                {
                    "name": "期末(70%)",
                    "score": "73"
                },
                {
                    "name": "总评",
                    "score": "80"
                }
            ]
        },
        {
            "courseName": "认识实习",
            "xuefen": "1",
            "jidian": "2.5",
            "zongping": "72",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "中等"
                },
                {
                    "name": "总评",
                    "score": "72"
                }
            ]
        },
        {
            "courseName": "高等数学A（4）(16版，",
            "xuefen": "3",
            "jidian": "1.5",
            "zongping": "67",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "80"
                },
                {
                    "name": "期末(70%)",
                    "score": "62"
                },
                {
                    "name": "总评",
                    "score": "67"
                }
            ]
        },
        {
            "courseName": "英语实践（2）",
            "xuefen": "0.5",
            "jidian": "4.5",
            "zongping": "90",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "96"
                },
                {
                    "name": "期末(60%)",
                    "score": "92"
                },
                {
                    "name": "总评",
                    "score": "优秀"
                }
            ]
        },
        {
            "courseName": "大学物理B（1）(16版，",
            "xuefen": "3.5",
            "jidian": "4.5",
            "zongping": "94",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "100"
                },
                {
                    "name": "期末(70%)",
                    "score": "91"
                },
                {
                    "name": "总评",
                    "score": "94"
                }
            ]
        },
        {
            "courseName": "物理实验（1）",
            "xuefen": "1.0",
            "jidian": "4.0",
            "zongping": "87",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "86.7"
                },
                {
                    "name": "总评",
                    "score": "87"
                }
            ]
        },
        {
            "courseName": "创业基础",
            "xuefen": "2.0",
            "jidian": "4.0",
            "zongping": "89",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "99.4"
                },
                {
                    "name": "期末(70%)",
                    "score": "85"
                },
                {
                    "name": "总评",
                    "score": "89"
                }
            ]
        },
        {
            "courseName": "园林艺术概论",
            "xuefen": "2.0",
            "jidian": "4.0",
            "zongping": "87",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "99.4"
                },
                {
                    "name": "期末(70%)",
                    "score": "81"
                },
                {
                    "name": "总评",
                    "score": "87"
                }
            ]
        },
        {
            "courseName": "综合英语（2）(16版，",
            "xuefen": "2.0",
            "jidian": "2.8",
            "zongping": "76",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "97.3"
                },
                {
                    "name": "期末(60%)",
                    "score": "61"
                },
                {
                    "name": "总评",
                    "score": "76"
                }
            ]
        },
        {
            "courseName": "英语口语（2）(16版，",
            "xuefen": "0.5",
            "jidian": "5.0",
            "zongping": "98",
            "scoreDetail": [
                {
                    "name": "平时(50%)",
                    "score": "99"
                },
                {
                    "name": "期末(50%)",
                    "score": "96"
                },
                {
                    "name": "总评",
                    "score": "98"
                }
            ]
        },
        {
            "courseName": "越野行走(2)",
            "xuefen": "0.5",
            "jidian": "4.0",
            "zongping": "88",
            "scoreDetail": [
                {
                    "name": "期中(40%)",
                    "score": "85"
                },
                {
                    "name": "期末(60%)",
                    "score": "90"
                },
                {
                    "name": "总评",
                    "score": "88"
                }
            ]
        },
        {
            "courseName": "大学生涯导论",
            "xuefen": "0.5",
            "jidian": "5.0",
            "zongping": "95",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "100"
                },
                {
                    "name": "期末(70%)",
                    "score": "93"
                },
                {
                    "name": "总评",
                    "score": "95"
                }
            ]
        },
        {
            "courseName": "英语实践（1）",
            "xuefen": "0.5",
            "jidian": "4.5",
            "zongping": "90",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "96"
                },
                {
                    "name": "期末(60%)",
                    "score": "93"
                },
                {
                    "name": "总评",
                    "score": "优秀"
                }
            ]
        },
        {
            "courseName": "信息学科概论",
            "xuefen": "2",
            "jidian": "4.5",
            "zongping": "92",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "83"
                },
                {
                    "name": "期末(70%)",
                    "score": "96"
                },
                {
                    "name": "总评",
                    "score": "92"
                }
            ]
        },
        {
            "courseName": "综合英语（1）(16版，",
            "xuefen": "2.0",
            "jidian": "3.0",
            "zongping": "79",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "97.1"
                },
                {
                    "name": "期末(60%)",
                    "score": "67"
                },
                {
                    "name": "总评",
                    "score": "79"
                }
            ]
        },
        {
            "courseName": "高级语言程序设计",
            "xuefen": "3.5",
            "jidian": "3.5",
            "zongping": "83",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "99"
                },
                {
                    "name": "期末(70%)",
                    "score": "76"
                },
                {
                    "name": "总评",
                    "score": "83"
                }
            ]
        },
        {
            "courseName": "高级语言程序设计实验",
            "xuefen": "1.0",
            "jidian": "4.0",
            "zongping": "89",
            "scoreDetail": [
                {
                    "name": "平时(70%)",
                    "score": "93"
                },
                {
                    "name": "期末(30%)",
                    "score": "80"
                },
                {
                    "name": "总评",
                    "score": "89"
                }
            ]
        },
        {
            "courseName": "计算机基础训练",
            "xuefen": "0.5",
            "jidian": "4.5",
            "zongping": "94",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "93.6"
                },
                {
                    "name": "总评",
                    "score": "94"
                }
            ]
        },
        {
            "courseName": "英语口语（1）(16版，",
            "xuefen": "0.5",
            "jidian": "4.0",
            "zongping": "85",
            "scoreDetail": [
                {
                    "name": "平时(50%)",
                    "score": "82"
                },
                {
                    "name": "期末(50%)",
                    "score": "87"
                },
                {
                    "name": "总评",
                    "score": "85"
                }
            ]
        },
        {
            "courseName": "军事训练",
            "xuefen": "2.0",
            "jidian": "3.5",
            "zongping": "85",
            "scoreDetail": [
                {
                    "name": "平时(0%)",
                    "score": "84"
                },
                {
                    "name": "期末(100%)",
                    "score": "良好"
                },
                {
                    "name": "总评",
                    "score": "良好"
                }
            ]
        },
        {
            "courseName": "高等数学A（1）(16版，",
            "xuefen": "2",
            "jidian": "2.5",
            "zongping": "73",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "100"
                },
                {
                    "name": "期末(70%)",
                    "score": "62"
                },
                {
                    "name": "总评",
                    "score": "73"
                }
            ]
        },
        {
            "courseName": "高等数学A（2）(16版，",
            "xuefen": "3",
            "jidian": "2.5",
            "zongping": "72",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "100"
                },
                {
                    "name": "期末(60%)",
                    "score": "54"
                },
                {
                    "name": "总评",
                    "score": "72"
                }
            ]
        },
        {
            "courseName": "中国近现代史纲要",
            "xuefen": "3.0",
            "jidian": "4.0",
            "zongping": "86",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "89"
                },
                {
                    "name": "期末(60%)",
                    "score": "84"
                },
                {
                    "name": "总评",
                    "score": "86"
                }
            ]
        },
        {
            "courseName": "思想道德修养与法律基础",
            "xuefen": "3.0",
            "jidian": "3.5",
            "zongping": "82",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "90.5"
                },
                {
                    "name": "期末(60%)",
                    "score": "77"
                },
                {
                    "name": "总评",
                    "score": "82"
                }
            ]
        },
        {
            "courseName": "军事理论",
            "xuefen": "2.0",
            "jidian": "4.0",
            "zongping": "86",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "86"
                },
                {
                    "name": "期末(70%)",
                    "score": "86"
                },
                {
                    "name": "总评",
                    "score": "86"
                }
            ]
        },
        {
            "courseName": "大学生心理健康教育",
            "xuefen": "0.5",
            "jidian": "3.5",
            "zongping": "84",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "86"
                },
                {
                    "name": "期末(70%)",
                    "score": "83"
                },
                {
                    "name": "总评",
                    "score": "84"
                }
            ]
        },
        {
            "courseName": "网球(1)",
            "xuefen": "0.5",
            "jidian": "3.0",
            "zongping": "78",
            "scoreDetail": [
                {
                    "name": "期中(40%)",
                    "score": "73"
                },
                {
                    "name": "期末(60%)",
                    "score": "82"
                },
                {
                    "name": "总评",
                    "score": "78"
                }
            ]
        },
        {
            "courseName": "生态文化影视鉴赏",
            "xuefen": "2",
            "jidian": "4.0",
            "zongping": "89",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "87"
                },
                {
                    "name": "期末(70%)",
                    "score": "90"
                },
                {
                    "name": "总评",
                    "score": "89"
                }
            ]
        },
        {
            "courseName": "电工技术与电子技术实验A(2)",
            "xuefen": "1.0",
            "jidian": "4.0",
            "zongping": "86",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "86"
                },
                {
                    "name": "总评",
                    "score": "86"
                }
            ]
        },
        {
            "courseName": "程序设计综合实践",
            "xuefen": "3",
            "jidian": "4.5",
            "zongping": "91",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "91.2"
                },
                {
                    "name": "总评",
                    "score": "91"
                }
            ]
        },
        {
            "courseName": "计算机组成原理实验",
            "xuefen": "0.5",
            "jidian": "3.0",
            "zongping": "81",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "86"
                },
                {
                    "name": "期末(70%)",
                    "score": "79"
                },
                {
                    "name": "总评",
                    "score": "81"
                }
            ]
        },
        {
            "courseName": "计算机组成原理",
            "xuefen": "2.5",
            "jidian": "4.0",
            "zongping": "85",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "90"
                },
                {
                    "name": "期末(70%)",
                    "score": "83"
                },
                {
                    "name": "总评",
                    "score": "85"
                }
            ]
        },
        {
            "courseName": "文献检索与利用",
            "xuefen": "2.0",
            "jidian": "5.0",
            "zongping": "97",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "100"
                },
                {
                    "name": "期末(70%)",
                    "score": "95"
                },
                {
                    "name": "总评",
                    "score": "97"
                }
            ]
        },
        {
            "courseName": "大学物理B（2）",
            "xuefen": "3.5",
            "jidian": "4.5",
            "zongping": "90",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "98"
                },
                {
                    "name": "期末(70%)",
                    "score": "86"
                },
                {
                    "name": "总评",
                    "score": "90"
                }
            ]
        },
        {
            "courseName": "物理实验（2）",
            "xuefen": "1.0",
            "jidian": "3.5",
            "zongping": "82",
            "scoreDetail": [
                {
                    "name": "期末(100%)",
                    "score": "82"
                },
                {
                    "name": "总评",
                    "score": "82"
                }
            ]
        },
        {
            "courseName": "电工技术与电子技术A(2)",
            "xuefen": "3.5",
            "jidian": "2.8",
            "zongping": "75",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "89.6"
                },
                {
                    "name": "期末(60%)",
                    "score": "66"
                },
                {
                    "name": "总评",
                    "score": "75"
                }
            ]
        },
        {
            "courseName": "综合英语（3）",
            "xuefen": "2.0",
            "jidian": "4.0",
            "zongping": "85",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "96"
                },
                {
                    "name": "期末(60%)",
                    "score": "77"
                },
                {
                    "name": "总评",
                    "score": "85"
                }
            ]
        },
        {
            "courseName": "英语实践（3）",
            "xuefen": "1.0",
            "jidian": "3.5",
            "zongping": "85",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "93"
                },
                {
                    "name": "期末(60%)",
                    "score": "66"
                },
                {
                    "name": "总评",
                    "score": "良好"
                }
            ]
        },
        {
            "courseName": "形势与政策",
            "xuefen": "2.0",
            "jidian": "4.5",
            "zongping": "91",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "80"
                },
                {
                    "name": "期末(70%)",
                    "score": "95"
                },
                {
                    "name": "总评",
                    "score": "91"
                }
            ]
        },
        {
            "courseName": "毛泽东思想和中国特色社会主义理论体系概论",
            "xuefen": "3.0",
            "jidian": "3.0",
            "zongping": "80",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "88.4"
                },
                {
                    "name": "期末(60%)",
                    "score": "74"
                },
                {
                    "name": "总评",
                    "score": "80"
                }
            ]
        },
        {
            "courseName": "羽毛球(3)",
            "xuefen": "0.5",
            "jidian": "3.0",
            "zongping": "81",
            "scoreDetail": [
                {
                    "name": "平时(40%)",
                    "score": "92.5"
                },
                {
                    "name": "期末(60%)",
                    "score": "73.2"
                },
                {
                    "name": "总评",
                    "score": "81"
                }
            ]
        },
        {
            "courseName": "线性代数(16版，",
            "xuefen": "2.5",
            "jidian": "2.8",
            "zongping": "77",
            "scoreDetail": [
                {
                    "name": "平时(30%)",
                    "score": "96"
                },
                {
                    "name": "期末(70%)",
                    "score": "69"
                },
                {
                    "name": "总评",
                    "score": "77"
                }
            ]
        }
    ]
}
        return data

    @staticmethod
    def exams_return():
        data = {
            "status": 200,
            "msg": "抓取成功",
            "data": [
                {
                    "local": "博1-A102",
                    "time": "2019-11-02(19:00-20:40)",
                    "course": "高等数学A（1）(16版，",
                    "type": "2019-2020-1正常考试",
                    "year": 2021,
                    "month": 7,
                    "day": 2
                },
                {
                    "local": "博2-A302",
                    "time": "2019-11-18(19:00-20:40)",
                    "course": "信息学科概论",
                    "type": "2019-2020-1正常考试",
                    "year": 2021,
                    "month": 11,
                    "day": 18
                },
                {
                    "local": "计-9机房",
                    "time": "2019-11-27(10:15-11:55)",
                    "course": "计算机基础训练",
                    "type": "2020-2021-1正常考试",
                    "year": 2021,
                    "month": 11,
                    "day": 27
                }
            ]
        }
        return data

    @staticmethod
    def autodianfei_return():
        data = {
            "status": 200,
            "msg": "抓取成功",
            "data": {
                "home": "梅2楼",
                "num": "B4202",
                "balance": 176.5
            }
        }
        return data

    @staticmethod
    def newlogin_return():
        data = {
            "code": 0,
            "data": {
                "name": "游客",
                "college": "计算机科学与技术学院",
                "classname": "xx-xx班",
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTUxMTA0NTIuNDAyNjg2NCwiZGF0YSI6eyJ1c2VybmFtZSI6IjEyMzQ1Njc4IiwicGFzc3dvcmQiOiIxMjM0NTY3OCJ9fQ.EEOr8vWHQWH-Y3OdhKW9fCTIyPEvTOwIfDxNAgyttOI"
            },
            "msg": "登录成功"
        }
        return data

    @staticmethod
    def simpleBalance_return():
        data = {
                "status": 200,
                "msg": "请求成功",
                "data": {
                    "cardNumber": "119192",
                    "balance": "8385"
               }
        }
        return data

    @staticmethod
    def simplelibrary_return():
        data = {
                "status": 200,
                "msg": "请求成功",
                "data": [
                    {
                        "title": "Linux网络服务与Shell脚本攻略.云计算工程师系列",
                        "loanData": "2020-12-17",
                        "returnDate": "2021-01-16",
                        "location": "南湖自然科学图书阅览室",
                        "callNo": "TP316.85/X-694"
                    },
                    {
                        "title": "精通Python网络爬虫:核心技术、框架与项目实战:core technology、frame and practices",
                        "loanData": "2020-12-17",
                        "returnDate": "2021-01-16",
                        "location": "南湖自然科学图书阅览室",
                        "callNo": "TP311.561/W-846"
                    }
                ]
        }
        return data

    @staticmethod
    def simplebalancehistory_return():
        data = {
            "status": 200,
            "msg": "请求成功",
            "data": {
                "num": 10,
                "libList": [
                    {
                        "title": "新编C++语言习题与解析",
                        "loanDate": "2020-09-07",
                        "returnDate": "2020-10-05",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "Docker容器技术与高可用实战",
                        "loanDate": "2020-09-07",
                        "returnDate": "2020-09-29",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "JavaScript测试驱动开发",
                        "loanDate": "2020-09-07",
                        "returnDate": "2020-09-29",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "HTML5与CSS3从入门到精通",
                        "loanDate": "2019-11-10",
                        "returnDate": "2019-12-08",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "C和C++代码精粹",
                        "loanDate": "2019-11-10",
                        "returnDate": "2019-12-08",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "“笨办法”学Python",
                        "loanDate": "2019-10-26",
                        "returnDate": "2019-11-10",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "Python程序设计基础",
                        "loanDate": "2019-10-26",
                        "returnDate": "2019-11-10",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "Python机器学习实践：测试驱动的开发方法",
                        "loanDate": "2019-10-26",
                        "returnDate": "2019-11-10",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "Python开发案例教程",
                        "loanDate": "2019-09-16",
                        "returnDate": "2019-10-12",
                        "location": "南湖自然科学图书阅览室"
                    },
                    {
                        "title": "数据馆员的Python简明手册",
                        "loanDate": "2019-09-16",
                        "returnDate": "2019-10-12",
                        "location": "南湖自然科学图书阅览室"
                    }
                ]
            }
        }
        return data

    @staticmethod
    def makeup_return():
        data = [{'courseName': 'Web应用开发技术B', 'xuefen': '2', 'jidian': '4.50', 'zongping': '94', 'type': '正常考试'}, {'courseName': '数字信号处理', 'xuefen': '3', 'jidian': '2.50', 'zongping': '73', 'type': '重修'}, {'courseName': '近距离无线通信技术', 'xuefen': '2.0', 'jidian': '2.00', 'zongping': '69', 'type': '正常考试'}, {'courseName': '通信原理', 'xuefen': '3.5', 'jidian': '1.00', 'zongping': '64', 'type': '重修'}, {'courseName': '无线通信基础', 'xuefen': '2', 'jidian': '1.00', 'zongping': '60', 'type': '补考一'}, {'courseName': '专业实习实训（生产实习）', 'xuefen': '4', 'jidian': '2.50', 'zongping': '72', 'type': '正常考试'}, {'courseName': '电子信息学科前沿讲座', 'xuefen': '1', 'jidian': '3.00', 'zongping': '80', 'type': '正常考试'}, {'courseName': '微机原理与应用B', 'xuefen': '2.5', 'jidian': '2.80', 'zongping': '75', 'type': '重修'}, {'courseName': '瑜伽(3)', 'xuefen': '0.5', 'jidian': '2.80', 'zongping': '77', 'type': '正常考试'}]

        return data





