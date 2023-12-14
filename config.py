# 公众号配置
# 公众号appId
app_id = "wx3fdfe0e286fc8741"
# 公众号appSecret
app_secret = "1306b872df510b960705d5fefeda7f19"
# 模板消息id
# 每日消息
template_id1 = "tt9YCM_nx0p4EvVnjbqTviix2y84AI-J1ewVoxwIqf8"
# 课程消息,上课提醒
template_id2 = "80enWK6k0f_THdy1JHcsIwqiPCGzEHVmSvCUT4B481E"
# 晚安心语
template_id3 = "uyzSArbU14EwrsTO06rCDOcvyDYIioYrAkke8LxndzU"
# 接收公众号消息的微信号
# 这是openid
user = ["o29V-6G3qXqew848F8jfxvEF1T64"]

# 信息配置
# 所在省份
province = "河南"
# 所在城市
city = "郑州"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "2004-7-28"
# 在一起的日子，格式同上------------计时器
love_date = "2023-1-31"
# 天行数据晚安心语 key
good_Night_Key = "10efc222c4e82107b85e4a58c52bf92a"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2022
month = 9
day = 11
# 每日推送时间
post_Time = "07:35:00"
# 每节课提醒时间（有课才会提醒）, 时:分:秒  的形式, 字符串, 根据个人需要设置几次
time_table = ["07:40:00", "09:40:00", "13:40:00", "15:40:00", "18:40:00"]
# 课程时间
course_Time = ["8:00--9:45", "10:00--11:45", "14:00--15:45", "16:00--17:45", "19:00--20:45"]
# 晚安心语及第二天课程推送时间
good_Night_Time = "22:55:00"
# 课程表 "1"代表第一周，依次类推，根据个人实际课表添加，有几周就添加几周,
# 每一行代表一天, 例如  ['', '编译原理', '', '数据库原理及应用', '数据分析原理', '']  代表周一
classes = \
    {
        "1": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['', '', '', '大学物理', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
       "2": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['大学物理实验', '大学物理实验', '', '', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "3": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['', '', '', '大学物理', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "4": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['大学物理实验', '大学物理实验', '', '', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "14": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['大学物理实验', '大学物理实验', '', '', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "15": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['', '', '', '大学物理', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "16": [
            ['', '数据结构', '离散数学', '数据结构实验', '', ''],
            ['大学物理', '', '', '', '', ''],
            ['离散数学', '大学英语', '体育', '中国近代史纲要', '', ''],
            ['大学物理实验', '大学物理实验', '', '', '', ''],
            ['数字逻辑', '数据结构', '毛泽东思想概论', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
    }


# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{birthday.DATA}} 天
# 在一起的第: {{love_date.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
