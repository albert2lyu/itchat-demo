#!/usr/bin/env python
# encoding: utf-8


import threading

import itchat
from itchat.content import *


class FrListener(object):

	@staticmethod
	@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isFriendChat=True)
	def text_show(msg):
		print(u'--- %s' % msg.text)

	@staticmethod
	@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
	def download_files(msg):
		msg.download(msg.fileName)
		typeSymbol = {
			PICTURE: 'img',
			VIDEO: 'vid', }.get(msg.type, 'fil')
		return '@%s@%s' % (typeSymbol, msg.fileName)

	def msg_loog_mp(self):
		itchat.run(debug=True)

	def register_run(self):
		recv_mp_t = threading.Thread(target=self.msg_loog_mp(), name='msg_recv_fr')
		recv_mp_t.start()
