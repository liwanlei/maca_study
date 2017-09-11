# -*- coding: utf-8 -*-
# @Date    : 2017-09-07 08:57:35
# @Author  : lileilei
from page.page import page_data 
def login(deriver,username,password):
	deriver.element_by_id(page_data['username']).send_keys(username)
	deriver.element_by_id(page_data['password']).send_keys(password)
	deriver.element_by_id(page_data['login']).click()