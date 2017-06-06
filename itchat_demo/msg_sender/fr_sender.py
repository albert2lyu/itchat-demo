#!/usr/bin/env python
# encoding: utf-8


import itchat
import sys


class FrSender(object):

	fr_name = u'小公主'
	m_name = u'延昊南'

	def get_nameid_by_kwd(self, kwd):
		target_contacts = itchat.search_friends(name=self.m_name)

		if not target_contacts:
			print(u'用户未找到, exit')
			return None

		return target_contacts[0].UserName

	def send_msg2fr(self, msg):
		target_name_id = self.get_nameid_by_kwd(FrSender.fr_name)
		itchat.send(msg, toUserName=target_name_id)
		print(u'- 我: %s' % msg)

	def input_msg(self):
		while True:
			send_msg = raw_input().decode(sys.stdin.encoding)
			self.send_msg2fr(send_msg)
