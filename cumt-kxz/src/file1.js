



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
 * @apiSuccess {string} grade     专业
 * @apiSuccess {string} classs    班级
 * @apiError {String}  code         1
 * @apiError {String}  msg        登录失败
 *
 *
 * @apiSuccessExample  {json} Response-Example
 * {
    "code": 0,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDE5MDgyMDIuMTEwNDYsImRhdGEiOnsidXNlcm5hbWUiOiIwODE5MzEwOSIsInBhc3N3b3JkIjoiMDMwMDE0In19.G-7U7NWLbA-Y4DBMCgQopi0McaFzUdMYf67SeQwjx8E",
    "name": "吕迎朝",
    "college": "计算机科学与技术学院",
    "grade": "数据科学与大数据技术专业(0850)",
    "class": "数据科学与大数据技术2019-02班",
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
 * @apiParamExample {json} Request-Example
 * http://127.0.0.1:5000/lib/book?book=三体
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
            "book_id": 413400,
            "name": "三体.Ⅲ.Ⅲ,死神永生,Dead end.中国科幻基石丛书",
            "author": "刘慈欣著",
            "publisher": "重庆出版社",
            "isbn": "978-7-229-03093-3",
            "pcount": 3,
            "ecount": 1,
            "search_code": "I247.55/L-236.2/3",
            "image": "https://unicover.duxiu.com/coverNew/CoverNew.dll?iid=69696969686A6E726C6B68706C6B5FA7A898B09AAD9EABA69AABA45F6A3231343233333039",
            "status_now": [
                {
                    "bookcode": "C01759935",
                    "location": "南湖校区-南湖社科图书阅览室Ⅱ",
                    "current": "借出-应还日期:2020-12-10"
                },
                {
                    "bookcode": "C01759936",
                    "location": "文昌校区-文昌社科书阅览室",
                    "current": "在架"
                },
                {
                    "bookcode": "C01759934",
                    "location": "南湖校区-南湖社科图书阅览室Ⅱ",
                    "current": "借出-应还日期:2020-09-15"
                }
            ]
        },
        {
            "book_id": 373428,
            "name": "三体.Ⅹ,观想之宙.中国科幻基石丛书",
            "author": "宝树著",
            "publisher": "重庆出版社",
            "isbn": "978-7-229-03981-3",
            "pcount": 3,
            "ecount": 1,
            "search_code": "I247.5/B-764/5",
            "image": "https://unicover.duxiu.com/coverNew/CoverNew.dll?iid=6364616A646661636B6858A0A191A993A697A49F93A49D58633139343236393232",
            "status_now": [
                {
                    "bookcode": "C01697588",
                    "location": "南湖校区-南湖社科图书阅览室Ⅱ",
                    "current": "在架"
                },
                {
                    "bookcode": "C01697587",
                    "location": "南湖校区-南湖社科图书阅览室Ⅱ",
                    "current": "典藏处理"
                },
                {
                    "bookcode": "C01697589",
                    "location": "文昌校区-文昌社科书阅览室",
                    "current": "在架"
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






function getUserInfo(username) {
  // 假如这个函数是根据用户名返回用户信息的
}