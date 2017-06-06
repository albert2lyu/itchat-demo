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
	target_stamp = time.mktime(time.strptime('17 03 21 16 41 59', '%y %m %d %H %M %S'))
	if local_stamp >= target_stamp:
		return True
	return False


if __name__ == '__main__':
	itchat.auto_login(hotReload=True, enableCmdQR=2)

	mp_listener = MpListener()
	fr_listener = FrListener()
	mp_sender = MpSender()
	fr_sender = FrSender()

	# mp_listener.register_run()
	# fr_listener.register_run()

	while True:
		if time_check():
			mp_sender.send_msg2mp_loop(1, 5)
		else:
			time.sleep(1 * random.random())
	# fr_sender.input_msg()
