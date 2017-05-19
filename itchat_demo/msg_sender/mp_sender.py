#!/usr/bin/env python
# encoding: utf-8


import itchat


class MpSender(object):

	target_name = u'北京交通大学教育基金会'
	test_target_name = u'北京移动10086'
	msg = u'你好, 这里是测试'

	def get_nameid_by_kwd(self, kwd):
		target_contacts = itchat.search_mps(name=self.test_target_name)

		if not target_contacts:
			print(u'用户未找到, exit')
			exit(0)

		return target_contacts[0].UserName

	def send_msg2mp(self):
		target_name_id = self.get_nameid_by_kwd(MpSender.test_target_name)
		itchat.send(self.msg, toUserName=target_name_id)
		print(u'- %s' % self.msg)
