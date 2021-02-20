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
    def login_return():
        # /jwxt/login
        data = {
            "code": 0,
            "data": {
                "name": "测试用户",
                "college": "计算机科学与技术学院",
                "classname": "xx-xx班",
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTM4MDc0MzMuOTI0MzEzOCwiZGF0YSI6eyJ1c2VybmFtZSI6IjEyMzQ1Njc4IiwicGFzc3dvcmQiOiIxMjM0NTY3OCJ9fQ.1g8ZxM-xPZxsXv-pwAP3-Ju8G5psoQtZHY1B-2GYyR8"
            },
            "msg": "登录成功"
        }
        return data

    @staticmethod
    def kb_return():
        data = {
         "msg": "抓取成功",
         "data": [
        {
            "title": "电工技术与电子技术A(2)",
            "location": "博3-B103",
            "teacher": "芦楠楠",
            "credit": "3.5",
            "weekList": [
                1,
                2,
                3,
                4,
                6,
                7,
                8,
                9,
                10
            ],
            "weekNum": 1,
            "lessonNum": 1,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "程序设计综合实践",
            "location": "计-25机房",
            "teacher": "李鸣",
            "credit": "3",
            "weekList": [
                14,
                15,
                16,
                17,
                18,
                19
            ],
            "weekNum": 1,
            "lessonNum": 1,
            "durationNum": 4,
            "remark": ""
        },
        {
            "title": "线性代数(16版，",
            "location": "博1-B502",
            "teacher": "王志俊",
            "credit": "2.5",
            "weekList": [
                1,
                2,
                3,
                4,
                7,
                8,
                9,
                10,
                11,
                12
            ],
            "weekNum": 1,
            "lessonNum": 5,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "线性代数(16版，",
            "location": "博1-B502",
            "teacher": "魏琦瑛",
            "credit": "2.5",
            "weekList": [
                6
            ],
            "weekNum": 1,
            "lessonNum": 5,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "形势与政策",
            "location": "博1-A102",
            "teacher": "孙凌杉",
            "credit": "2",
            "weekList": [
                13,
                14,
                15,
                16,
                17,
                18,
                19
            ],
            "weekNum": 1,
            "lessonNum": 5,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "毛泽东思想和中国特色社会主义理论体系概论",
            "location": "博1-C101",
            "teacher": "高建明",
            "credit": "3",
            "weekList": [
                2,
                3,
                4,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15
            ],
            "weekNum": 1,
            "lessonNum": 7,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "电工技术与电子技术A(2)",
            "location": "博3-B103",
            "teacher": "芦楠楠",
            "credit": "3.5",
            "weekList": [
                1,
                2,
                3,
                4,
                6,
                7,
                8,
                9,
                10
            ],
            "weekNum": 2,
            "lessonNum": 1,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "综合英语（3）",
            "location": "博5-C302",
            "teacher": "韦炜",
            "credit": "2.0",
            "weekList": [
                1,
                2,
                3,
                4,
                6,
                7,
                8,
                9
            ],
            "weekNum": 2,
            "lessonNum": 3,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "英语实践（3）",
            "location": "博5-B206",
            "teacher": "苗媛",
            "credit": "1.0",
            "weekList": [
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19
            ],
            "weekNum": 2,
            "lessonNum": 3,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "计算机组成原理",
            "location": "博4-A101",
            "teacher": "王莉2",
            "credit": "2.5",
            "weekList": [
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19
            ],
            "weekNum": 2,
            "lessonNum": 5,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "文献检索与利用",
            "location": "图-107",
            "teacher": "武保民",
            "credit": "2.0",
            "weekList": [
                1,
                2,
                3
            ],
            "weekNum": 2,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "文献检索与利用",
            "location": "图-107",
            "teacher": "汪媛",
            "credit": "2.0",
            "weekList": [
                4,
                6,
                7,
                10
            ],
            "weekNum": 2,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "文献检索与利用",
            "location": "图-107",
            "teacher": "王玲玲",
            "credit": "2.0",
            "weekList": [
                8,
                9
            ],
            "weekNum": 2,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "生态文化影视鉴赏",
            "location": "博4-C307",
            "teacher": "程伟",
            "credit": "2",
            "weekList": [
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18
            ],
            "weekNum": 2,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "大学物理B（2）",
            "location": "博1-C101",
            "teacher": "唐芙蓉",
            "credit": "3.5",
            "weekList": [
                1,
                2,
                3,
                4,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15
            ],
            "weekNum": 3,
            "lessonNum": 1,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "形势与政策",
            "location": "博1-A102",
            "teacher": "孙凌杉",
            "credit": "2",
            "weekList": [
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19
            ],
            "weekNum": 3,
            "lessonNum": 3,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "电工技术与电子技术A(2)",
            "location": "博2-B201",
            "teacher": "芦楠楠",
            "credit": "3.5",
            "weekList": [
                12
            ],
            "weekNum": 3,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "线性代数(16版，",
            "location": "博1-B503",
            "teacher": "王志俊",
            "credit": "2.5",
            "weekList": [
                1,
                2,
                3,
                6,
                7,
                8,
                9,
                10,
                11
            ],
            "weekNum": 4,
            "lessonNum": 1,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "程序设计综合实践",
            "location": "计-25机房",
            "teacher": "李鸣",
            "credit": "3",
            "weekList": [
                14,
                15,
                16,
                17,
                18,
                19
            ],
            "weekNum": 4,
            "lessonNum": 1,
            "durationNum": 4,
            "remark": ""
        },
        {
            "title": "电工技术与电子技术A(2)",
            "location": "博3-B103",
            "teacher": "芦楠楠",
            "credit": "3.5",
            "weekList": [
                1,
                2,
                3,
                6,
                7,
                8,
                9,
                10
            ],
            "weekNum": 4,
            "lessonNum": 3,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "羽毛球(3)",
            "location": "体育场",
            "teacher": "张晓侠",
            "credit": "0.5",
            "weekList": [
                1,
                2,
                3,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14
            ],
            "weekNum": 4,
            "lessonNum": 5,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "毛泽东思想和中国特色社会主义理论体系概论",
            "location": "博1-C101",
            "teacher": "高建明",
            "credit": "3",
            "weekList": [
                2,
                3,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14
            ],
            "weekNum": 4,
            "lessonNum": 7,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "文献检索与利用",
            "location": "图-107",
            "teacher": "武保民",
            "credit": "2.0",
            "weekList": [
                1,
                2,
                3
            ],
            "weekNum": 4,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "文献检索与利用",
            "location": "图-107",
            "teacher": "汪媛",
            "credit": "2.0",
            "weekList": [
                6,
                9
            ],
            "weekNum": 4,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "文献检索与利用",
            "location": "图-107",
            "teacher": "王玲玲",
            "credit": "2.0",
            "weekList": [
                7,
                8
            ],
            "weekNum": 4,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "生态文化影视鉴赏",
            "location": "博4-C307",
            "teacher": "程伟",
            "credit": "2",
            "weekList": [
                11,
                12,
                13,
                14,
                16,
                17,
                18
            ],
            "weekNum": 4,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "生态文化影视鉴赏",
            "location": "博4-C307",
            "teacher": "孟庆俊",
            "credit": "2",
            "weekList": [
                15
            ],
            "weekNum": 4,
            "lessonNum": 9,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "综合英语（3）",
            "location": "博5-C302",
            "teacher": "韦炜",
            "credit": "2.0",
            "weekList": [
                1,
                2,
                3,
                5,
                6,
                7,
                8,
                9
            ],
            "weekNum": 5,
            "lessonNum": 1,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "英语实践（3）",
            "location": "博5-B206",
            "teacher": "苗媛",
            "credit": "1.0",
            "weekList": [
                11,
                12,
                13,
                14,
                15,
                16,
                18
            ],
            "weekNum": 5,
            "lessonNum": 1,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "大学物理B（2）",
            "location": "博1-C101",
            "teacher": "唐芙蓉",
            "credit": "3.5",
            "weekList": [
                1,
                2,
                3,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15
            ],
            "weekNum": 5,
            "lessonNum": 3,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "计算机组成原理",
            "location": "博4-A101",
            "teacher": "王莉2",
            "credit": "2.5",
            "weekList": [
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                18,
                19
            ],
            "weekNum": 5,
            "lessonNum": 5,
            "durationNum": 2,
            "remark": ""
        },
        {
            "title": "计算机组成原理实验",
            "location": "计-37机房",
            "teacher": "王莉2",
            "credit": "0.5",
            "weekList": [
                12,
                13,
                16,
                18
            ],
            "weekNum": 6,
            "lessonNum": 1,
            "durationNum": 4,
            "remark": ""
        },
        {
            "title": "电工技术与电子技术A(2)",
            "location": "博3-B103",
            "teacher": "芦楠楠",
            "credit": "3.5",
            "weekList": [
                10
            ],
            "weekNum": 6,
            "lessonNum": 3,
            "durationNum": 2,
            "remark": ""
        }
    ]
        }
        return data

    @staticmethod
    def grades_return():
        data =   {
         "status": 200,
         "msg": "抓取成功",
         "data": [
        {
            "courseName": "英语实践（1）",
            "xuefen": "0.5",
            "zongping": "优秀",
            "jidian": 5.0,
            "scoreDetail": [
                {
                    "平时(40%)": "96"
                },
                {
                    "期末(60%)": "93"
                },
                {
                    "总评": "优秀"
                }
            ]
        },
        {
            "courseName": "大学物理B（2）",
            "xuefen": "3.5",
            "jidian": 4.5,
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
                 "courseName": "综合英语（3）",
                 "xuefen": "2.0",
                 "jidian": 4.0,
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
        "msg": "登陆成功",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTM4MDc0MzMuOTI0MzEzOCwiZGF0YSI6eyJ1c2VybmFtZSI6IjEyMzQ1Njc4IiwicGFzc3dvcmQiOiIxMjM0NTY3OCJ9fQ.1g8ZxM-xPZxsXv-pwAP3-Ju8G5psoQtZHY1B-2GYyR8"
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



