






/**
 * @api {Get} /daily/df
 * @apiGroup 电费查询
 *
 * @apiParam {String} home 宿舍楼  (梅2楼)
 * @apiParam {String} num  门号    (B4202)
 *
 *
 *@apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/df?home=梅2楼&num=B4202
 *
 *
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回数据
 *
 * @apiError {String}  status  404
 * @apiError {String} msg      抓取失败
 * @apiError {Integer} data 返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
 *
 * {
 *   "status": "200",
 *   "msg": "ok"
 *   "data": "227.43"
 * }
 *@apiErrorExample   {json} Response-Example
 *
 *{
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
  }
 *
 */


/**
 * @apiGroup 课表查询
 * @api {Get} /jwxt/kb
 *
 * @apiHeader {String} token 用户授权token
 * @apiParam {String} xnm 年份 如2019
 * @apiParam {String} xqm  学期 如 第一学期：1 第二学期：2
 *
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/jwxt/kb?xnm=2020&xqm=1
 *
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
 * {
 *   "status": 200,
    "msg": "抓取成功",
    "data": {
        "kblx": 7,
        "qsxqj": "1",
        "xqbzxxszList": [],
        "xsxx": {
            "BJMC": "数据科学与大数据技术2019-02班",
            "XNMC": "2019-2020",
            "KXKXXQ": "('3')",
            "XKKGXQ": "1~('3')",
            "XKKG": "1",
            "XH_ID": "08193109",
            "XH": "08193109",
            "XQMMC": "1",
            "XM": "吕迎朝",
            "XQM": "3",
            "XNM": "2019",
            "KCMS": 16
        },
 * }
 *
 * @apiErrorExample   {json} Response-Example
 *
 *{
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 */



/**
 * @apiGroup 成绩查询
 * @api {Get} /jwxt/grade
 *
 * @apiHeader {String} token 用户授权token
 * @apiParam {String} xnm 年份 如2019
 * @apiParam {String} xqm  学期 如 第一学期：1 第二学期：2 全年：0
 *
 *
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/jwxt/grade?xnm=2018&xqm=0
 *
 *
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 *
 * @apiSuccessExample  {json} Response-Example
 *
 *   {
    "status": 200,
    "msg": "抓取成功",
    "data": [
        {
            "courseName": "大学生涯导论",
            "xuefen": "0.5",
            "zongping": "95",
            "jidian": 5.0,
            "scoreDetail": [
                {
                    "平时(30%)": "100"
                },
                {
                    "期末(70%)": "93"
                },
                {
                    "总评": "95"
                }
            ]
        },
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

 * }
 *
 *
 * @apiErrorExample   {json} Response-Example
 *
 *{
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */












/**
 * @api {Get} /jwxt/alljd
 * @apiGroup 所有绩点查询
 * @apiHeader {String} token 用户授权token
 * @apiParam {String} xnm 年份 如2019
 * @apiParam {String} xqm  学期 如 第一学期：1 第二学期：2 全年学期 0
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/jwxt/alljd?xnm=2019&xqm=1
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
 * {
 *   "status": 200,
    "msg": "抓取成功",
    "data": {
        "currentPage": 1,
        "currentResult": 0,
        "entityOrField": false,
        "items": [
            {
                "bfzcj": 84,
                "bh": "191085002",
                "bh_id": "A21D3D0AB3AB0176E053C0A86D5DBDD9",
                "bj": "数据科学与大数据技术2019-02班",
                "cj": "84",
                "cjsfzf": "否",
                "date": "二○二○年十月四日",
                "dateDigit": "2020年10月4日",
                "dateDigitSeparator": "2020-10-4",
                "day": "4",
                "jd": "3.50",
                "jg_id": "08",
                "jgmc": "计算机科学与技术学院",
                "jgpxzd": "1",
                "jsxm": "卓婷婷",
                "jxb_id": "8B1C09AB21BA03B2E053C0A86D5D7E88",
                "jxbmc": "大学生心理健康教育-0017",
                "kcbj": "主修",
                "kch": "G30103",
                "kch_id": "36D607EF6DC200D4E053C0A8666200D4",
                "kclbmc": "C",
                "kcmc": "大学生心理健康教育",
                "kcxzdm": "30",
 * }
 *
 *
 * @apiErrorExample   {json} Response-Example
 *{
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */

/**
 * @api {Get} /jwxt/avejd
 * @apiGroup 总加权绩点查询
 * @apiHeader {String} token 用户授权token
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/jwxt/avejd
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
 * {
 *  "status": 200,
    "msg": "抓取成功",
    "data": "3.65"
 * }
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */

/**
 * @api {Post} /jwxt/login
 * @apiGroup A登录
 *
 * @apiParam {String} username 学号
 * @apiParam {String} password 密码
 * @apiParamExample {json} Request-Example
 * {
 *     "username":"08193109",
 *     "password":"xxxxxxxx"
 * }
 * @apiSuccess {String} code       0
 * @apiSuccess {String} msg       登录成功
 * @apiSuccess {string} token     生成token
 * @apiSuccess {string} name      姓名
 * @apiSuccess {string} college   学院
 * @apiSuccess {string} classname    班级
 * @apiError {String}  code         1
 * @apiError {String}  msg        登录失败
 *
 *
 * @apiSuccessExample  {json} Response-Example
{
    "code": 0,
    "data": {
        "name": "吕迎朝",
        "college": "计算机科学与技术学院",
        "classname": "数据科学与大数据技术2019-02班",
        "token": "eyJ0eXAiOiJKV1QiLChbOiJIUzI1NiJ9.eyJpYXQiOjE2MDM5ODQ3NDcuNDU3NjkwiZGF0YSI6eyJ1c2VybmFSI6IjAMTkzMTA5IiwicGFzc3dvcmQiOiIwMzAwMTQifX0.KHahG0anf70pP9QPs2iNGLLVT5NgS_zL5aFaIIXH_FM"
    },
    "msg": "登录成功"
}
 * @apiErrorExample   {json} Response-Example
 *{
    "code": 1,
    "msg": "登录失败,请检查你的用户名或密码！"
   }
 *
 */



/**
 * @api {Get} /jwxt/exam
 * @apiGroup 考试查询
 * @apiHeader {String} token 用户授权token
 * @apiParam {String} xnm 年份 如2019
 * @apiParam {String} xqm  学期 如 第一学期：1 第二学期：2
 * @apiParamExample {json} Request-Example
 * http://127.0.0.1:5000/jwxt/exam?xnm=2019&xqm=1
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    抓取成功
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
{
    "status": 200,
    "msg": "抓取成功",
    "data": [
        {
            "local": "博1-A102",
            "time": "2019-11-02(19:00-20:40)",
            "course": "高等数学A（1）(16版，",
            "type": "2019-2020-1正常考试",
            "year": 2019,
            "month": 11,
            "day": 2
        },
        {
            "local": "博2-A302",
            "time": "2019-11-18(19:00-20:40)",
            "course": "信息学科概论",
            "type": "2019-2020-1正常考试",
            "year": 2019,
            "month": 11,
            "day": 18
        },
        {
            "local": "计-9机房",
            "time": "2019-11-27(10:15-11:55)",
            "course": "计算机基础训练",
            "type": "2019-2020-1正常考试",
            "year": 2019,
            "month": 11,
            "day": 27
        }
    ]
}
 * @apiErrorExample   {json} Response-Example
* {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 */


/**
 * @api {Get} /lib/book
 * @apiGroup 图书查询
 *
 * @apiParam {String} book 书名(如三体)
 * @apiParam {String} page 第几页
 * @apiParam {String} row 一页显示多少行
 *
 * @apiParamExample {json} Request-Example
 * http://139.155.245.66:5000/lib/book?book=三体&page=1&row=5
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    抓取成功
 * @apiSuccess {string} data   返回列表
 * @apiSuccess {string} pcount   物理馆藏
 * @apiSuccess {string} ecount   电子馆藏
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
{
    "status": 200,
    "msg": "抓取成功",
    "data": {
        "all": 1601,
        "bookList": [
            {
                "book_id": 253498,
                "name": "论三位一体.世纪人文系列丛书",
                "author": "[古罗马] 奥古斯丁著",
                "publisher": "上海人民出版社",
                "isbn": "7-208-05282-4",
                "pcount": 3,
                "ecount": 1,
                "search_code": "B972/A-361",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C01300810",
                        "location": "南湖密集书库-南湖密集书库Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01300808",
                        "location": "文昌校区-文昌社科书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01300809",
                        "location": "南湖密集书库-南湖密集书库Ⅰ",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 211210,
                "name": "考研英语三位一体作文法.考研英语口袋系列 ",
                "author": "吴玮翔编著  ",
                "publisher": "东南大学出版社",
                "isbn": "7-81089-633-4",
                "pcount": 5,
                "ecount": 1,
                "search_code": "H315/W-866",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C01137499",
                        "location": "文昌校区-文昌社科书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01137500",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01137502",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01137503",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01137501",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 729598,
                "name": "真三轴条件下受载煤体损伤与瓦斯渗流耦合机理研究",
                "author": "刘佳佳著",
                "publisher": "煤炭工业出版社",
                "isbn": "978-7-5020-6433-4",
                "pcount": 2,
                "ecount": 0,
                "search_code": "TD712/L-421",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C02344535",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02344536",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 667413,
                "name": "金融地理学视角下的金融一体化研究:以长三角核心城市群为例.21世纪海上丝绸之路智库丛书",
                "author": "周迪著",
                "publisher": "科学出版社",
                "isbn": "978-7-03-052125-5",
                "pcount": 3,
                "ecount": 0,
                "search_code": "F832.75/Z-249",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C02300304",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02300305",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02300306",
                        "location": "文昌校区-文昌社科书阅览室",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 263099,
                "name": "煤层体三维模型和动态显示研究",
                "author": "史明寅著",
                "publisher": "中国矿业大学",
                "isbn": null,
                "pcount": 1,
                "ecount": 0,
                "search_code": "#/P628/S-537",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "X2293",
                        "location": "南湖校区-知学空间(硕博论文)",
                        "current": "在架"
                    }
                ],
                "status": false
            },
            {
                "book_id": 339998,
                "name": "UG NX三维造型设计教程与实例精讲.CAX一体化解决方案系列丛书",
                "author": "李锦标等编著",
                "publisher": "机械工业出版社",
                "isbn": "978-7-111-28932-6",
                "pcount": 4,
                "ecount": 1,
                "search_code": "TB472-39/L-412.3",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C01546420",
                        "location": "文昌校区-文昌科技书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01546417",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01546418",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01546419",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 583795,
                "name": "粤港澳增长三角次区域经济一体化研究",
                "author": "康学芹著",
                "publisher": "中国社会科学出版社",
                "isbn": "978-7-5161-4031-4",
                "pcount": 3,
                "ecount": 1,
                "search_code": "F127.65/K-888",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C02109130",
                        "location": "文昌校区-文昌社科书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02109128",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02109129",
                        "location": "南湖校区-南湖社科图书阅览室Ⅰ",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 674955,
                "name": "道路三维集成CAD与BIM一体化技术.上册",
                "author": "娄峰, 王绥庆等编著",
                "publisher": "人民交通出版社股份有限公司",
                "isbn": "978-7-114-14040-2",
                "pcount": 3,
                "ecount": 0,
                "search_code": "U412.6/L-316/1",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C02309810",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02309809",
                        "location": "南湖校区-南湖自然科学图书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C02309811",
                        "location": "文昌校区-文昌科技书阅览室",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 245068,
                "name": "小西北经济问题研究:地区经济一体化·产业集群·三农问题",
                "author": "聂华林, 高凯山, 拜琦瑞编著",
                "publisher": "中国社会科学出版社",
                "isbn": "7-5004-5563-1",
                "pcount": 3,
                "ecount": 1,
                "search_code": "F127.4/N-383",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "C01280575",
                        "location": "文昌校区-文昌社科书阅览室",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01280576",
                        "location": "南湖密集书库-南湖密集书库Ⅱ",
                        "current": "在架"
                    },
                    {
                        "bookcode": "C01280577",
                        "location": "南湖密集书库-南湖密集书库Ⅱ",
                        "current": "在架"
                    }
                ],
                "status": true
            },
            {
                "book_id": 706908,
                "name": "基于智能体的三维疏散软件的设计与实现",
                "author": "黄元凯著",
                "publisher": "中国矿业大学",
                "isbn": null,
                "pcount": 1,
                "ecount": 0,
                "search_code": "#/TU998.1/H-922",
                "image": null,
                "status_now": [
                    {
                        "bookcode": "XS31329",
                        "location": "南湖校区-知学空间(硕博论文)",
                        "current": "在架"
                    }
                ],
                "status": false
            }
        ]
    }
}
 * @apiErrorExample   {json} Response-Example
* {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 */



/**
 * @api {Post} /jwxt/classroom
 * @apiGroup 空闲教室查询
 *
 * @apiParam {String} xnm       学年
 * @apiParam {String} xqm       学期
 * @apiParam {String} build     位置 如博3
 * @apiParam {String} section   第几节课 ，按2的幂次相加区别，请直接看写在前面
 * @apiParam {String} week      第几周， 按2的幂次相加区别，具体请见写在前面
 * @apiParam {String} weekday   星期几：多个用 1，2，3，4表示
 * @apiParamExample {json} Request-Example
 * {
    "xnm" : "2020",
    "xqm" : "3",
    "build" : "博3",
    "section" : "3",
    "week" : "32",
    "weekday" : "3,4"

}
 * @apiSuccess {String} status       200
 * @apiSuccess {String} msg       抓取成功
 * @apiSuccess {string} data      返回列表
 *
 *
 *@apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
{
    "status": 200,
    "msg": "抓取成功",
    "data": [
        {"room": "博3-A203"},
        {"room": "博3-A501"},
        {"room": "博3-B102"},
        {"room": "博3-B203"},
        {"room": "博3-B301"},
        {"room": "博3-B401"}
    ]
}
 * @apiErrorExample   {json} Response-Example
* {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 */


/**
 * @api {Post} /jwxt/course
 * @apiGroup 根据条件查询上课情况
 *
 * @apiParam {String} xnm       学年
 * @apiParam {String} xqm       学期
 * @apiParam {String} _id       学院代码， 具体请见写在前面
 * @apiParam {String} section   节次 如 1-7
 * @apiParam {String} week      周次 如 1-4
 * @apiParam {String} weekday   星期几
 * @apiParamExample {json} Request-Example
 {
    "xnm":"2020",
    "xqm":"3",
    "_id":"0",
    "weekday":"1",
    "week":"1-7",
    "section":"1-4",
    "teacher":"0"
}
 * @apiSuccess {String} status       200
 * @apiSuccess {String} msg       抓取成功
 * @apiSuccess {string} data      返回列表
 *
 *@apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 *
 * @apiSuccessExample  {json} Response-Example
{
    "status": 200,
    "msg": "抓取成功",
    "data": [
        {
            "college": "力学与土木工程学院",
            "class_name": "工程力学B(1)",
            "teacher_name": "罗宁",
            "_class": "土木工程2019-09班;土木工程2019-10班",
            "time": "星期一第1-2节{1周};星期一第1-2节{2-4周,6-11周};星期三第3-4节{1周};星期三第3-4节{2-4周,6-11周};星期四第3-4节{1周};星期四第3-4节{2-3周,6-10周}",
            "location": "博3-A501;博5-B207;博3-A501;博5-B207;博3-A501;博5-B207"
        },
        {
            "college": "经济管理学院",
            "class_name": "国际商务",
            "teacher_name": "牛芳",
            "_class": "国际经济与贸易2019-01班;国际经济与贸易2019-02班",
            "time": "星期一第1-2节{1-2周};星期一第1-2节{3-4周,6-9周};星期二第3-4节{1-2周};星期二第3-4节{3-4周,6-9周};星期五第7-8节{1周};星期五第7-8节{2-3周,5-9周}",
            "location": "博4-B404;博2-B201;博4-B404;博2-B401;博4-B404;博1-B202"
        },
        {
            "college": "经济管理学院",
            "class_name": "经济论文写作",
            "teacher_name": "卜华",
            "_class": "会计学2018-01班;会计学2018-02班;会计学2018-03班;会计学2018-04班",
            "time": "星期一第1-2节{1-4周,6-7周};星期三第3-4节{1-2周,6周};星期五第5-6节{1-3周,5-6周};星期六第9-10节{3-5周(单)}",
            "location": "博4-A203;博4-A202;博3-A202;博4-A202"
        },
        ]}
 * @apiErrorExample   {json} Response-Example
* {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 */

/**
 * @api {Get} /daily/au_df
 * @apiGroup 自动电费查询
 * @apiHeader {String} token 用户授权token
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
 * {
 *  "status": 200,
    "msg": "抓取成功",
    "data":
            {
                "home":"梅2楼",
                "num":"B4202",
                "balance":176.5
            }
 * }
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */


/**
 * @api {Get} /daily/home_image
 * @apiGroup Z首页轮播图
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/home_image
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
 * {
    "status": 200,
    "msg": "ok",
    "data": [
        {
            "image-url": "http://www.cumt.edu.cn/_upload/article/images/6e/9b/40047ff14838aea1355117147eb6/b4175c83-919c-487a-be25-e485a873c18c.jpeg"
        },
        {
            "image-url": "http://www.cumt.edu.cn/_upload/article/images/65/a7/748a3f114d2bbb8fe1dd038d088d/6d3d93c2-fde9-41e3-a825-65241378ca57.jpg"
        },
        {
            "image-url": "http://www.cumt.edu.cn/_upload/article/images/c8/ee/26b7e17d4840b6f378b31531751e/2777b695-68de-42dc-8ae3-463527d8d13b.jpg"
        },
        {
            "image-url": "http://www.cumt.edu.cn/_upload/article/images/e9/47/292d616c41ac8cfbf058095f8627/a7aac6cc-f76f-4415-a7b6-37fd10ebacb5.jpg"
        },
        {
            "image-url": "http://www.cumt.edu.cn/_upload/article/images/88/57/b5af5bb2487a87cc87a8e8565735/54fd901c-24de-441f-a16f-d59ea83db6a4.jpg"
        },
        {
            "image-url": "http://www.cumt.edu.cn/_upload/article/images/77/36/8e002d744efa988e4e71b6a03a17/4c5fb7e0-9ac1-4c44-9d02-849a71e45f7b.jpg"
        }
    ]
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */



/**
 * @api {Get} /daily/sd_news
 * @apiGroup Z1视点新闻列表
 * @apiParam {String} page 页数
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/sd_news?page=1
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
 {
    "status": 200,
    "msg": "ok",
    "data": [
        {
            "title": "我校干部师生广泛热议习近平总书记在纪念中国人民志愿军抗美援朝出国作战70周年大会上的重要讲话",
            "link": "http://www.cumt.edu.cnhttp://xwzx.cumt.edu.cn/d5/7f/c513a578943/page.htm",
            "time": "2020-10-23"
        },
        {
            "title": "第八届“传承弘扬徐州历史文化 展示新时代大学生风采”活动在我校开幕 ",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=579438",
            "time": "2020-10-28"
        },
        {
            "title": "中煤科工集团重庆研究院相关负责人来校交流",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=579534",
            "time": "2020-10-28"
        },
        {
            "title": "我校参加江海英才高校联盟成立大会",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=579430",
            "time": "2020-10-28"
        },
        {
            "title": "徐州市委统战部来我校开展高校统战工作调研",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=579428",
            "time": "2020-10-28"
        },
        {
            "title": "第八届江苏高校辅导员素质能力大赛复赛在我校举行",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=579319",
            "time": "2020-10-27"
        },
        {
            "title": "我校召开2020年各类资产盘点工作布置会",
            "link": "http://www.cumt.edu.cnhttp://xwzx.cumt.edu.cn/d5/74/c513a578932/page.psp",
            "time": "2020-10-26"
        },
        {
            "title": "上海校友会企业家与高端人才代表返徐助力学校与地方发展",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=579136",
            "time": "2020-10-26"
        },
        {
            "title": "我校为离退休教职工举行重阳节集体祝寿活动",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=578987",
            "time": "2020-10-24"
        },
        {
            "title": "我校召开会议传达首届全国教材工作会议精神",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=578949",
            "time": "2020-10-23"
        },
        {
            "title": "我校入选“国家知识产权示范高校”",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=578921",
            "time": "2020-10-23"
        },
        {
            "title": "我校召开课程思政建设工作会",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=578742",
            "time": "2020-10-21"
        },
        {
            "title": "全国政协共青团、青联界别调研组来我校调研",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=578737",
            "time": "2020-10-21"
        },
        {
            "title": "神宝能源公司、大雁集团公司与我校进行合作办学座谈",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19673&articleId=578850",
            "time": "2020-10-21"
        }
    ]
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */

/**
 * @api {Get} /daily/sd_new
 * @apiGroup Z2视点新闻详细
 * @apiParam {String} url 从新闻列表里获取的url
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/sd_new?url=http://www.cumt.edu.cn/_redirect?siteId=44%26columnId=19673%26articleId=578944
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
{
    "status": 200,
    "msg": "ok",
    "data": {
        "title": "我校干部师生广泛热议习近平总书记在纪念中国人民志愿军抗美援朝出国作战70周年大会上的重要讲话",
        "header": {
            "author": "刘勇",
            "time": "2020-10-23"
        },
        "about": [
            "新闻来源：党委宣传部组稿",
            "摄影：",
            "责任编辑：刘尧",
            "审核:黄军利"
        ],
        "content": [
            "10月23日上午，纪念中国人民志愿军抗美援朝出国作战70周年大会在北京人民大会堂隆重举行。中共中央总书记、国家主席、中央军委主席习近平出席大会并发表重要讲话。习近平总书记的重要讲话引起了学校干部师生广泛学习热议，大家纷纷表示要认真学习领会总书记的重要讲话精神，继承和弘扬伟大抗美援朝精神，勠力同心、锐意进取，为实现中华民族伟大复兴而努力奋斗。",
            "校党委书记刘波说，习近平总书记的重要讲话，振奋人心，催人奋进。抗美援朝战争的伟大胜利，让世界见证了中国人民汇聚起来的磅礴力量，让世界知道“中国人民是惹不得的”。站在“两个一百年”奋斗目标的历史交汇点上，重温中国人民志愿军建立的不朽历史功勋，致敬“最可爱的人”，在新时代继承和弘扬伟大抗美援朝精神，具有重大现实意义。我们将深入学习贯彻习近平总书记重要讲话精神，大力弘扬伟大抗美援朝精神，将其内化为推进学校事业发展的精神动力，坚持抓好理想信念教育，筑牢爱国主义精神根基，引导广大干部师生牢记初心使命，发扬斗争精神，以昂扬向上的精气神，全力推进能源资源特色的世界一流大学建设，为实现中华民族伟大复兴的中国梦作出矿大贡献。",
            "校长宋学锋说，习近平总书记的重要讲话慷慨激昂、情怀满满、鼓舞人心、意义重大。抗美援朝战争的胜利，是正义的胜利、和平的胜利、人民的胜利，必将永远铭刻在中华民族的史册上，永远铭刻在人类和平、发展、进步的史册上。伟大的抗美援朝精神必将跨越时空、历久弥新，永续传承、世代发扬。它告诉世人，“中国人民在任何困难和风险面前，腿肚子不会抖，腰杆子不会弯，中华民族是吓不倒、压不垮的！”我们将以习近平总书记的重要讲话精神为指引，继续夯实立德树人根基，坚持为党育人、为国育才，坚持固本强优拓新、转型发展的基本方略，更加紧密地融入国家能源强国战略，在实现中华民族伟大复兴的大道上，书写矿大人报效国家的华章。",
            "校机关党委书记吴瑜说，70年前，中国人民志愿军为了保家卫国踏上抗美援朝战场，他们付出鲜血和生命，以立国之战的胜利，展示了中国人民不畏强暴的钢铁意志。我国将进入新发展阶段，以古鉴今，继往开来，伟大的抗美援朝精神将成为激励我们干事创业的精神力量，鼓舞我们永远保持斗争精神、永远保持奋斗精神，为能源资源特色世界一流大学建设贡献智慧和力量。",
            "党委学生工作部、党委武装部部长冯震说，聆听了总书记的重要讲话，深受教育。作为从事大学生思想政治教育的干部，我们将学习和弘扬伟大的抗美援朝精神，加强当代大学生爱国主义精神，革命英雄主义精神、革命乐观主义精神、国际主义精神教育，引导青年学生牢固树立团结奋斗、敢打敢拼、不怕牺牲、奋勇向前的斗争精神和斗争意识，为实现中国民族伟大复兴的中国梦而努力奋斗。",
            "信控学院党委书记张磊说，总书记的讲话铿锵有力、振奋人心，带领我们深刻领略了那群英雄儿女交出的扬眉吐气、家国安宁的历史答卷。以史为鉴，作为高校思政工作者，我们要进一步引导广大青年增强“四个意识”，坚定“四个自信”，做到“两个维护”，弘扬伟大的抗美援朝精神，万众一心，奋力拼搏，成为能担当起民族复兴大任的时代新人。",
            "化工学院教授王虹说，伟大抗美援朝精神激励我们在实现中华民族伟大复兴征程上不畏艰难、奋勇前进。作为专业教师，要注重言传身教、率先垂范，抓住学生成长关键期，引导学生从抗美援朝精神中汲取成长力量，锻造过硬本领，培养富有创新精神、科学素养的人才，为服务国家能源战略贡献科技力量。",
            "马克思主义学院党委副书记阎国华说，抗美援朝战争，是交战双方力量极为悬殊的战争。我们的胜利得益于中国人民志愿军的浴血奋战，得益于中朝军民的密切配合，得益于反抗侵略、保卫和平的正义力量。回望70年前伟大的抗美援朝战争，我们要铭记伟大胜利，推进伟大事业，要化感动为行动，从点滴实践入手，尽职尽责，拼搏创新，为高校践行立德树人根本任务贡献自己的青春与智慧。",
            "计算机学院党委副书记王梦倩说，伟大的抗美援朝战争，是保卫和平、反抗侵略的正义之战。为国为民的人，是最可爱的人，历史将永远铭记。新时代需要一代又一代的年轻人高擎爱国主义伟大旗帜，在党和人民最需要的时候，挺身而出，接续奋斗。作为学生思想政治教育的一线工作者，要坚持立德树人根本任务，当好学生健康成长的引路人，这是对胜利最好的纪念，也是对英烈最好的告慰。",
            "矿业学院智能采矿2017班王嘉伟说，中国人民志愿军抛头颅、洒热血，拼来了山河无恙、家国安宁。自己作为一名退役大学生士兵，现已被保送至国防科技大学攻读研究生，在今后的学习生活中，一定会传承和发扬伟大抗美援朝精神，逢山开路、遇水架桥，努力为我国的国防科工事业贡献自己的绵薄之力。",
            "数学学院应用数学2018-3班茆琳说，从历史课本中学习过黄继光、邱少云等先烈的英雄事迹，在军训合唱中传唱过抗美援朝时期的歌曲。今天聆听了总书记的重要讲话，对抗美援朝精神有了更为深刻的认知。作为一名学生党员,自己将牢记历史，砥砺前行，肩负起青年一代的光荣使命。"
        ]
    }
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */

/**
 * @api {Get} /daily/rw_news
 * @apiGroup Z3视点新闻列表
 * @apiParam {String} page 页数
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/sd_news?page=1
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
  {
    "status": 200,
    "msg": "ok",
    "data": [
        {
            "title": "【镜湖大讲堂】（2020-28）——“诗仙”与“诗鬼”：唐诗的想象空间",
            "time": "2020-10-28",
            "detail": []
        },
        {
            "title": "【人文社科大讲堂】（2020-06）——形象诗学的理论建构和应用场域",
            "time": "2020-10-27",
            "detail": [
                "讲座题目：形象诗学的理论建构和应用场域",
                "讲座人：江苏师范大学文学院徐放鸣教授",
                "讲座时间：2020年10月28日（周三）15:00",
                "讲座地点：人文与艺术学院A110（线下）",
                "腾讯会议会议号：274321555（线上）",
                "主办单位：中国矿业大学人文与艺术学院",
                "中国矿业大学美育中心",
                "主讲人简介：徐放鸣，曾任徐州师范大学校长、江苏师范大学党委书记，现为江苏师范大学文学院教授，徐州市云龙书院院长。兼任国家教育部艺术学理论教学指导委员会委员，国家社科基金艺术学项目评审委员，国家社科基金项目成果鉴定专家，全国中文核心期刊评审专家，全国马列文论研究会副会长，中国中外文艺理论学会常务理事，中华孔子学会理事，江苏省艺术教育委员会副主任，江苏省美学学会副会长。是中央电视台“百家讲坛”栏目主讲人、国家精品视频公开课主讲人、中国现代文学馆公益讲座主讲人。主要从事美学、文艺学和传统文化研究，主持并完成国家社科基金重点项目“中国当代文艺实践中的国家形象构建研究”。"
            ]
        },
        {
            "title": "【镜湖大讲堂】（2020-27）—— 小探美的思维与逻辑：发现美，留下美",
            "time": "2020-10-23",
            "detail": [
                "讲座主题：2020年镜湖大讲堂系列讲座之二十七——小探美的思维与逻辑：发现美，留下美",
                "主讲人：邹兆群",
                "时间：2020年10月23日14:00",
                "地点：镜湖大讲堂",
                "主办方：共青团中国矿业大学委员会",
                "中国矿业大学镜湖讲座中心",
                "讲师介绍：",
                "邹兆群，自由摄影师；上海日报特约记者，境界传媒创始人，视觉中国签约摄影师，杜克大学签约摄影师，樱花卫厨签约摄影师，捷安特签约摄影师；从事商业摄影多年，与多家4A广告公司长期合作。",
                "讲座简介：",
                "生活中并不缺少美，缺少的是发现美的眼睛。本次讲座，邹兆群老师将向我们介绍美的思维与逻辑，带领我们了解发现美的方式、留下美的技巧。"
            ]
        },
        {
            "title": "【人文社科大讲堂】（2020-05）——相关性范式下的银行风险集成度",
            "time": "2020-10-21",
            "detail": [
                "报告题目：相关性范式下的银行风险集成度量研究",
                "报告人：李建平，教授、博士生导师",
                "报告时间：2020年10月23日14:00-17:00",
                "报告地点：经济管理学院B117",
                "报告摘要：银行面临着信用风险、市场风险和操作风险等多种类型的风险，这些风险之间不是相互独立的，银行风险集成是指在充分考虑银行风险相关关系的基础上，对银行风险进行较为准确的度量。对相关性下的银行风险集成研究进行综述，具体从集成对象、集成方法和集成数据三个层次系统展开。首先，对银行风险及其蕴含的种类繁多的相关关系类型进行解析；其次，分析银行风险相关关系表征出的多种复杂特性,根据对这些特性的刻画能力对银行风险的集成方法进行划分和比较；再次，总结获取银行风险集成数据的多种途径。在此基础上,重点介绍大数据环境下融合多源数据的银行风险集成研究前沿成果，以及分析该领域仍然存在的难点和未来研究趋势。",
                "报告人简介：",
                "‍",
                "李建平，国家杰出青年基金获得者，现任中国科学院特聘研究员、博士生导师、中国科学院大学经济与管理学院教授。兼任国际信息技术与量化管理学会（IAITQM）执行委员、秘书长；中国优选法统筹法与经济数学研究会副理事长、青年工作委员会主任、《中国管理科学》执行主编等。主要研究领域为：风险管理、大数据管理决策。获“中国青年科技奖”、“全国优秀科技工作者”、“中科院优秀导师奖”等荣誉。在国内外学术期刊上发表论文130余篇。获得省部级自然科学/科技进步奖一等奖2项，二等奖4项。指导的研究生中，获得中科院院长特别奖4人，中科院优秀博士论文奖3人。"
            ]
        },
        {
            "title": "【人文社科大讲堂】（2020-04）——人工智能与新冠抗疫",
            "time": "2020-10-20",
            "detail": [
                "讲座题目：人工智能与新冠抗疫",
                "讲座人：曹志冬研究员",
                "讲座时间：10月21日（星期三）15:30-17:00",
                "讲座地点：公共管理学院A426",
                "主办单位：中国矿业大学公共管理学院",
                "讲座人简介："
            ]
        },
        {
            "title": "【人文社科大讲堂】（2020-03）——柳琴戏的艺术风格与传承",
            "time": "2020-10-20",
            "detail": [
                "讲座题目：柳琴戏的艺术风格与传承",
                "讲座人：朱树龙",
                "讲座时间：2020年10月21日（周三）15:00",
                "讲座地点：人文与艺术学院艺术报告厅（建筑与设计学院二楼）",
                "主办单位：中国矿业大学人文与艺术学院",
                "中国矿业大学美育中心",
                "主讲人简介：朱树龙，国家一级演员，国家级非物质文化遗产项目（柳琴戏）代表性传承人，中国戏剧家协会会员。徐州市“十佳职工”，徐州市“五一奖章“获得者。荣获曹雨杯金奖、中国现代戏剧贡献奖、首届江苏省文华表演奖、江苏省第四届、第五届、第六届戏剧节优秀表演奖、江苏省优秀新剧目评比优秀表演奖、优秀唱腔设计奖、第二届江苏省红梅杯金奖。",
                "代表剧目:《红罗衫》、《汉宫怨》、《白玉楼》、《解忧公主》等。演唱的《铜台会》选段在中央电视台【名段欣赏】栏目中多次播出。"
            ]
        },
        {
            "title": "【人文社科大讲堂】（2020-02)—— 规划人生到人生规划",
            "time": "2020-10-20",
            "detail": [
                "讲座题目：规划人生到人生规划",
                "讲座人：王万茂教授",
                "讲座时间：10月20日19:00",
                "讲座地点：博二C102室",
                "主办单位：中国矿业大学公共管理学院",
                "讲座人简介：",
                "王万茂，南京农业大学教授、博导。中国土地科学研究领域的泰斗和宗师。1961年毕业于原苏联哈尔科夫农业大学土地规划（整理）工程系，获土地工程师称号，享受国务院政府特殊津贴，是原国家教委批准的全国第一位土地资源管理博士生导师，1998年获中国工程院院士候选人提名。曾任中国土地学会副理事长、俄罗斯莫斯科土地整理工程大学客座教授、白俄罗斯明斯克大学客座教授。王万茂教授长期从事土地规划学、土地管理学和土地生态经济学的教学和研究，主编《土地利用规划学》等国家级规划教材多部，出版专著3本、译著2本，发表论文100多篇，先后获农业部、原国家土地管理局、江苏省科技进步一、二等奖以及江苏省哲学社会科学优秀成果奖等多项。"
            ]
        },
        {
            "title": "【人文社科大讲堂】（2020-01）——中国图案学研究的意义",
            "time": "2020-10-12",
            "detail": [
                "讲座题目：中国图案学研究的意义",
                "讲座人：东南大学艺术学院李倍雷教授",
                "讲座时间：2020年10月14日（周三）14:30",
                "讲座地点：人文与艺术学院A110（线下）",
                "腾讯会议会议号：127973723（线上）",
                "主办单位：中国矿业大学人文与艺术学院",
                "中国矿业大学美育中心",
                "主讲人简介：李倍雷，博士，东南大学艺术学院教授，博士生导师，艺术学博士后流动站合作导师，艺术学理论A+双一流学科带头人之一，全国比较艺术学学会副会长，全国高教研究生艺术教育联盟执行副主席，中国美术家协会会员，国家社科基金评审专家，国家社科后期资助评审专家，教育部人文社科评审专家。主持国家重点课题、一般课题、教育部课题多项，主持江苏省艺术基金（油画创作）课题1项；出版专著20余部，发表论文170余篇；获教育部人文社科优秀成果奖3等奖，获江苏省哲学社会科学优秀成果奖1、2等奖，获全国文艺评论奖2等奖，获江苏省文艺评论奖1等奖，油画作品获全国、省级展多项。"
            ]
        },
        {
            "title": "【镜湖大讲堂】（2020-26）—— 技术世界的三原色",
            "time": "2020-10-12",
            "detail": [
                "讲座主题：2020年镜湖大讲堂系列讲座之二十六——技术世界的三原色",
                "主讲人：夏保华",
                "时间：2020年10月16日19:00",
                "地点：镜湖大讲堂线上直播",
                "主办方：共青团中国矿业大学委员会",
                "中国矿业大学镜湖讲座中心",
                "参与方式：观众可以通过访问https://live.bilibili.com/22194746或在哔哩哔哩客户端搜索“中国矿业大学镜湖大讲堂”或扫描下方二维码观看直播。",
                "讲师介绍：",
                "夏保华，教授、博士生导师、东南大学人文学院副院长。中国自然辩证法研究会理事，中国自然辩证法研究会技术哲学、科学技术与工程伦理等专业委员会常务理事；江苏省自然辩证法研究会副理事长。主要研究方向为技术创新哲学、技术哲学、科技与社会等。出版个人学术专著4部，发表学术论文80余篇。",
                "讲座简介：",
                "色彩斑斓的技术世界是由三类基本行动者所塑造的，他们是发明家、创新家和哲学家。本次讲座，夏保华教授将为我们讲解：何为技术世界的发明家、创新家和哲学家；在智能革命的新时代，技术世界的发明家、创新家和哲学家正面临着怎样的新挑战。"
            ]
        },
        {
            "title": "【杰出学者彭城讲坛】（2020-16）——林语堂中国文化对外译介中的语言自信研究：从中式英语、中国英语到中国话语",
            "time": "2020-10-10",
            "detail": [
                "报告题目：林语堂中国文化对外译介中的语言自信研究：从中式英语、中国英语到中国话语",
                "报告人：冯智强教授",
                "报告时间：10月14日15:00",
                "讲座方式：腾讯会议会议号：241906075",
                "主办单位：中国矿业大学外文学院翻译与跨文化研究中心、澳大利亚研究中心",
                "讲座摘要：",
                "林语堂中国文化对外译介中的语言自信，表现为语言层面所包含的中国元素。从词汇、句子篇章到修辞等诸多层面的中国表达，是中国文化主体性和民族性的具体体现，具有一定的必然性与合理性。研究表明，中国文化对外译介过程中，不仅要传播中国文化的内涵，更要体现中国语言、思维和心理等特点，这是由语言文化不可分割的一体性决定的，也是中国文化“走出去”的必然要求，更是中西文化交流的宗旨。从文化自觉到语言自觉，从文化自信到语言自信和翻译自信，林语堂的英文书写活动在当下更凸显出其重要的时代价值，而我们对其认知也经历了从中式英语、中国英语到中国话语的复杂过程。",
                "报告人简介：",
                "冯智强，天津外国语大学教授，博士，翻译与跨文化传播研究院执行院长，中央文献翻译研究基地研究员，天津市高校学科领军人才，中国外文局对外传播研究中心研究员，中国翻译史研究会常务理事，中外语言文化比较学会翻译文化研究会理事，林语堂研究会理事，《中译外研究》副主编。近年来在《中国翻译》、《上海翻译》、《外语教学理论与实践》、《湖北社会科学》、《意林》、《中华读书报》、《天津日报》等报刊上发表论文、译文、散文百余篇，主持《中国文化对外译介的林语堂模式研究》《林语堂对外话语建构模式研究》等各级科研项目多项。专著《中国智慧的跨文化传播：林语堂英文著译研究》获天津市第十三届社科优秀成果奖，曾被刘宓庆先生誉为“近年来两岸三地最优秀的博士论文之一”。主要研究领域：林语堂研究、中译外研究、儿童文学翻译研究。"
            ]
        },
        {
            "title": "【镜湖大讲堂】（2020-25）—— 林徽因的才情与风骨",
            "time": "2020-09-29",
            "detail": [
                "讲座主题：林徽因的才情与风骨",
                "主讲人：胡俊修",
                "时间：2020年10月9日19:30",
                "地点：镜湖大讲堂",
                "主办方：共青团中国矿业大学委员会、中国矿业大学镜湖讲座中心",
                "讲师介绍：",
                "胡俊修，华中师范大学历史学博士，三峡大学马克思主义学院教授、博士生导师；光明日报民国往事专栏作者；中央电视台《法律讲堂》（文史版）主讲嘉宾；主讲中国大学精品视频公开课《胡适的人生与风范》；主持国家社科基金等省部级以上课题6项，出版专著2部。",
                "讲座简介：",
                "林徽因是胡适口中的“一代才女”，也是备受争议的美女。围绕着林徽因的那些真假莫辨的绯闻，隐藏了一个怎样真实的林徽因？本次讲座，胡俊修老师将带领我们了解颜值艳压四海八荒，才华吊打五湖四海的林徽因，向大家展现一个人品风骨让人泪目的奇女子。"
            ]
        },
        {
            "title": "【镜湖大讲堂】（2020-24）—— 海上丝路与中国传统科技在域外的传播",
            "time": "2020-09-29",
            "detail": [
                "讲座主题：海上丝路与中国传统科技在域外的传播",
                "主讲人：萨日娜",
                "时间：2020年9月30日19:00",
                "地点：镜湖大讲堂线上直播",
                "主办方：共青团中国矿业大学委员会、中国矿业大学镜湖讲座中心",
                "参与方式：观众可以通过访问https://live.bilibili.com/22194746或在哔哩哔哩客户端搜索“中国矿业大学镜湖大讲堂”或扫描下方二维码观看直播。",
                "讲师介绍：",
                "萨日娜，上海交通大学教授，中国科学技术史学会理事，中国数学会数学史学会理事，日本科学史学会会员，上海市浦江人才计划获得者，日本数学史学会桑原奖获得者，英国剑桥李约瑟研究所劲牌中国的科技与文明荣誉学者。",
                "讲座简介：",
                "中国传统科技是其文明的重要表现，也孕育着独特的传统文化。本次讲座，萨日娜老师将聚焦海上丝路与中国传统科技在域外的传播、中外科技的交流和比较等方面，使大家全面了解文化、文明、科学与技术之间的关系，一同剖析我国优秀传统科技文化在域外的传播和影响的新视角、新案例。"
            ]
        },
        {
            "title": "  【镜湖大讲堂】（2020-23）——美学与青年",
            "time": "2020-09-25",
            "detail": [
                "讲座主题：2020年镜湖大讲堂系列讲座之二十三——美学与青年",
                "主讲人：韩清玉",
                "时间：2020年9月26日15:00",
                "地点：镜湖大讲堂线上直播",
                "主办方：共青团中国矿业大学委员会",
                "中国矿业大学镜湖讲座中心",
                "观众可以通过访问https://live.bilibili.com/22194746或在哔哩哔哩客户端搜索“中国矿业大学镜湖大讲堂”或扫描下方二维码观看直播。",
                "讲师介绍：",
                "韩清玉，山东大学文学院、文艺美学研究中心教授，博士生导师，山东大学齐鲁青年学者。其主要研究领域为西方美学、中国现代文艺理论等，著有《艺术自律性研究》等，在《文学评论》等期刊发表学术论文四十余篇，主持国家社科基金一般项目、国家社科基金重大项目子课题等国家级项目2项，省部级科研项目4项，曾获安徽省社会科学奖等，主要学术兼职有中国文艺评论家协会会员、韩国融合人文学会编委等。",
                "讲座简介：",
                "2020年青年节，bilibili推出的《后浪》短片，引发了关于青年的讨论。青年的话题是时代性的，本次讲座韩清玉教授将带领我们回到20世纪早期，重温现代美学大家与青年的对话，感悟美学之于青年的重要性，一同探讨在后现代与电子化特征日趋显明的今天，我们该如何在美学的话语情境中讨论青年。韩清玉教授还将带领大家感悟朱光潜、宗白华等名家对青年的谆谆教诲，体会其中蕴含的人生美学与人生智慧，分析其对当今青年的启示意义。"
            ]
        },
        {
            "title": "【杰出学者彭城讲坛】（2020-15）——马克思主义发展史研究方法和视野的提升",
            "time": "2020-09-17",
            "detail": [
                "报告题目：马克思主义发展史研究方法和视野的提升",
                "报告人：胡大平教授",
                "报告时间：2020年9月18日14：30",
                "讲座方式：腾讯会议会议号：183772272",
                "主办单位：人文社会科学处，马克思主义学院",
                "报告人简介：胡大平，南京大学马克思主义学院教授，博士生导师。",
                "独立和合作出版著作教材十部，公开发表学术论文百篇。教育部新世纪人才支持计划青年学术带头人、江苏省青蓝工程中青年学术带头人、霍英东青年教师奖获得者，江苏省优秀博士论文获得者，曾获得江苏省哲学社会科学优秀成果二、三等奖，参与出版的《走进马克思》获13届中国图书奖和第六届国家图书奖提名奖。"
            ]
        }
    ]
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */

/**
 * @api {Get} /daily/xs_news
 * @apiGroup Z4学术聚焦列表
 * @apiParam {String} page 页数
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/xs_news?page=1
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
  {
    "status": 200,
    "msg": "ok",
    "data": [
        {
            "title": "江苏省第十三届信息安全高层论坛在我校召开",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=579458",
            "time": "2020-10-29"
        },
        {
            "title": "信控学院教师在社交飞行物联网研究方面取得进展 ",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=579230",
            "time": "2020-10-26"
        },
        {
            "title": "浙江大学柴春雷教授、邹宁副教授作“AI视界”系列学术报告",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=578712",
            "time": "2020-10-20"
        },
        {
            "title": "国家重点研发计划项目“矿井灾变通风智能决策与应急控制关键技术研究”中期检查项目改进工作方案审定会在徐举行",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=577666",
            "time": "2020-10-13"
        },
        {
            "title": "公管学院教师在农村土地租赁和农业劳动生产率研究方面取得新成果",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=577243",
            "time": "2020-10-09"
        },
        {
            "title": "“城郊深部能源绿色安全综合开发与城市协同发展”项目专家论证会召开",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=576227",
            "time": "2020-09-28"
        },
        {
            "title": "我校澳大利亚研究中心举行国别与区域研究工作坊学术活动",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=575737",
            "time": "2020-09-23"
        },
        {
            "title": "建筑与设计学院工业设计系师生荣获欧洲产品设计奖",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=574770",
            "time": "2020-09-16"
        },
        {
            "title": "电力学院博士生在储能锂电池热安全研究方面取得进展",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=574250",
            "time": "2020-09-09"
        },
        {
            "title": "南京大学黄贤金和杜培军教授来我校开展学术交流",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=573645",
            "time": "2020-08-29"
        },
        {
            "title": "东南大学薛澄岐教授作“多学科交叉背景下的工业设计研究”线上报告",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=573347",
            "time": "2020-08-22"
        },
        {
            "title": "力学与土木工程学院举行力学·深部工程专题学术沙龙",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=573075",
            "time": "2020-08-15"
        },
        {
            "title": "人工智能研究院组织开展“AI视界”系列学术报告",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=572938",
            "time": "2020-08-08"
        },
        {
            "title": "材料与物理学院张俊廷课题组在多铁性材料领域研究取得进展",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19674&articleId=572644",
            "time": "2020-08-01"
        }
    ]
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */


/**
 * @api {Get} /daily/xs_new
 * @apiGroup Z5学术聚焦详细
 * @apiParam {String} page 页数
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/xs_new?url=http://www.cumt.edu.cn/_redirect?siteId=44%26columnId=19674%26articleId=571198
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
  {
    "status": 200,
    "msg": "ok",
    "data": {
        "title": "我校举行“智能煤矿建设现状与实践”专题讲座",
        "content": "讲座现场钱建生教授作讲座7月10日，由科学技术研究院主办的智能煤矿建设专题讲座“智能煤矿建设现状与实践”在信控学院报告厅举行，通过线下、线上方式同步开讲。本次讲座邀请了我校二级教授、博士生导师钱建生担任主讲人。钱建生教授对智能煤矿建设的发展历程进行了回顾，就智能煤矿建设的现状与发展目标进行了分析与展望，对支撑智能煤矿建设的技术架构进行了详细阐述。他以夹河煤矿、临沂煤矿为例，介绍了飞行机器人、煤矿AI智能视频分析监控系统在实际工作中的应用。此外，他还着重介绍了煤矿智能化前沿技术与装备以及智能煤矿建设工程的主要内容，就如何系统地推进智能煤矿建设谈了自己与团队的思考与实践。他表示，推动智能煤矿建设的发展需要矿业、安全、信控等学科的共同努力，希望能够与矿大的科技同仁在“十四五”到来之际，推动智能煤矿建设事业更上一个台阶。在建设智能化矿山成为国内外煤矿企业发展必由之路的大背景下，本次讲座全面深入地介绍了智能煤矿建设的相关内容，其中所蕴含的前瞻性思考与前沿性尝试极大地开拓了煤矿建设者的视野，为实现煤矿资源的安全开发与高效利用提供了理论依据和智力支持，对相关科研工作的开展具有启发作用。"
    }
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */


/**
 * @api {Get} /daily/xx_news
 * @apiGroup Z6信息公告
 * @apiParam {String} page 页数
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/xx_news?page=1
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 * @apiSuccessExample  {json} Response-Example
 {
    "status": 200,
    "msg": "ok",
    "data": [
        {
            "title": "中国矿业大学第八届半程马拉松赛校园交通管制及通勤班车调整通告",
            "link": "http://www.cumt.edu.cn/d7/d5/c19678a579541/page.htm"
        },
        {
            "title": "关于申报教育部2021年港澳与内地大中小学",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19678&articleId=579401"
        },
        {
            "title": "关于直属业务单位全面实行首接责任制的通告",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19678&articleId=579364"
        },
        {
            "title": "关于召开全校研究生教育会议的通知",
            "link": "http://www.cumt.edu.cn/d7/23/c19678a579363/page.htm"
        },
        {
            "title": "关于召开中国矿业大学2020年各类资产盘点工作布置会的通知",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19678&articleId=578655"
        },
        {
            "title": "关于组织收看贯彻落实《深化新时代教育评价改革总体方案》电视电话会议的通知",
            "link": "http://www.cumt.edu.cn/d3/36/c19678a578358/page.htm"
        },
        {
            "title": "关于举行2020级学生军训总结表彰大会的通知",
            "link": "http://www.cumt.edu.cn/d3/13/c19678a578323/page.htm"
        },
        {
            "title": "关于申报2021年中国矿业大学“越崎引智计划”项目的通知",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19678&articleId=578167"
        },
        {
            "title": "关于召开学校课程思政建设工作会的通知",
            "link": "http://www.cumt.edu.cn/d2/71/c19678a578161/page.htm"
        },
        {
            "title": "关于2020年下半年面向我校学生开展普通话水平测试的通知",
            "link": "http://www.cumt.edu.cn/_redirect?siteId=44&columnId=19678&articleId=578088"
        },
        {
            "title": "关于限时开放文昌校区西门的通告",
            "link": "http://www.cumt.edu.cn/d1/6a/c19678a577898/page.htm"
        },
        {
            "title": "关于举办新生消防疏散逃生演习的通知",
            "link": "http://www.cumt.edu.cn/d0/98/c19678a577688/page.htm"
        },
        {
            "title": "关于组织参加教育部2020年高等学校科研实验室安全现场检查启动暨培训视频会议的通知",
            "link": "http://www.cumt.edu.cn/cf/e0/c19678a577504/page.htm"
        },
        {
            "title": "关于举行2020级本科学生军训动员大会的通知",
            "link": "http://www.cumt.edu.cn/cd/fe/c19678a577022/page.htm"
        }
    ]
}
 * @apiErrorExample   {json} Response-Example
 * {
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 *
 */






function getUserInfo(username) {
  // 假如这个函数是根据用户名返回用户信息的
}