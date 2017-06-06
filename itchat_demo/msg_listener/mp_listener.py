#!/usr/bin/env python
# encoding: utf-8


import threading

import itchat
from itchat.content import TEXT


class MpListener(object):

	@staticmethod
	@itchat.msg_register(TEXT, isMpChat=True)
	def text_show(msg):
		print(u'--- %s' % msg.text)

	def msg_loog_mp(self):
		itchat.run(debug=True)

	def register_run(self):
		recv_mp_t = threading.Thread(target=self.msg_loog_mp, name='msg_recv_mp')
		recv_mp_t.start()
