#!/usr/bin/env python
# encoding: utf-8


import time
import random
import itchat


class MpSender(object):

	target_name = u'北京交通大学教育基金会'
	test_target_name = u'北京移动10086'
	msg = u't'
	m_msg = u'我爱交大，毕业快乐。王辉，15231171，182XXXX1559'

	def get_nameid_by_kwd(self, kwd):
		target_contacts = itchat.search_mps(name=kwd)

		if not target_contacts:
			print(u'用户未找到, exit')
			return None

		return target_contacts[0].UserName

	def send_msg2mp(self):
		target_name_id = self.get_nameid_by_kwd(MpSender.test_target_name)
		itchat.send(self.msg, toUserName=target_name_id)
		print(u'- %s' % self.msg)

	def send_msg2mp_loop(self, interval, times):
		for i in range(times):
			self.send_msg2mp()
			time.sleep(interval * random.random())
