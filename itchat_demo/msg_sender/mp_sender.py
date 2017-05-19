#!/usr/bin/env python
# encoding: utf-8


import itchat


target_name = u'北京交通大学教育基金会'
test_target_name = u'北京移动10086'


def get_nameid_by_kwd(kwd):
	target_contacts = itchat.search_mps(name=test_target_name)

	if not target_contacts:
		print(u'用户未找到, exit')
		exit(0)

	return target_contacts[0].UserName


def send_msg2mp():
	target_name_id = get_nameid_by_kwd(test_target_name)
	itchat.send(u'你好, 这里是测试', toUserName=target_name_id)
