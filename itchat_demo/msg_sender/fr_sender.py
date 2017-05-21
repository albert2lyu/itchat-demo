#!/usr/bin/env python
# encoding: utf-8


import itchat


class FrSender(object):

	fr_name = u'小公主'
	m_name = u'延昊南、'

	def get_nameid_by_kwd(self, kwd):
		target_contacts = itchat.search_mps(name=self.test_target_name)

		if not target_contacts:
			print(u'用户未找到, exit')
			exit(0)

		return target_contacts[0].UserName

	def send_msg2fr(self, msg):
		target_name_id = self.get_nameid_by_kwd(FrSender.m_name)
		itchat.send(msg, toUserName=target_name_id)
		print(u'- %s' % self.msg)

	def input_msg(self):
		while True:
			send_msg = raw_input('input:')
			self.send_msg2fr(send_msg)
