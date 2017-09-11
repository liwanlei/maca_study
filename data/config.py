# -*- coding: utf-8 -*-
# @Date    : 2017-09-07 08:52:04
# @Author  : lileilei 
die_arp={
    'platformName':'Desktop',
    'browserName':'electron'
}
server_url={
    'hostname':'localhost',
    'post':3456
}
login_data=[
{'username':'北漂的','password':'li1213456','id':'tip_btn','assert':'该用户不存在'},
{'username':'','password':'li123456','id':'tip_input1','assert':'请输入登录用户名'},
{'username':'','password':'','id':'tip_input1','assert':'请输入登录用户名'},
{'username':'','password':'li123456','id':'tip_input1','assert':'请输入登录用户名'},
{'username':'北漂的雷子','password':'li123456','id':'tip_btn','assert':'用户名或密码错误'},
{'username':'北漂的雷子','password':'','id':'tip_input2','assert':'请输入密码'},
{'username':'北漂的雷子','password':'li.930423','id':'feed_recent','assert':'最新动态'},]