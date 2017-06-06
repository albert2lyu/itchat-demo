#!/usr/bin/env python
# encoding: utf-8


import itchat
import time
import random

from itchat_demo.msg_listener.mp_listener import MpListener
from itchat_demo.msg_listener.fr_listener import FrListener
from itchat_demo.msg_sender.mp_sender import MpSender
from itchat_demo.msg_sender.fr_sender import FrSender


def time_check():
	local_stamp = time.time()
	target_stamp = time.mktime(time.strptime('17 06 06 08 10 00', '%y %m %d %H %M %S'))
	if local_stamp >= target_stamp:
		return True
	return False


if __name__ == '__main__':
	itchat.auto_login(hotReload=True, enableCmdQR=2)

	fr_sender = FrSender()
	msg = u'test'

	while True:
		if time_check():
			fr_sender.send_msg2fr(msg)
			print(msg)
			break
		else:
			time.sleep(60 * 5)

	print('task end')
