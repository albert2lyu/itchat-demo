#!/usr/bin/env python
# encoding: utf-8


import itchat
from msg_listener.mp_listener import MpListener
from msg_listener.fr_listener import FrListener
from msg_sender.mp_sender import MpSender
from msg_sender.fr_sender import FrSender


if __name__ == '__main__':
	itchat.auto_login(hotReload=True, enableCmdQR=True)

	mp_listener = MpListener()
	fr_listener = FrListener()
	mp_sender = MpSender()
	fr_sender = FrSender()

	# mp_listener.register_run()
	fr_listener.register_run()

	# mp_sender.send_msg2mp()
	fr_sender.input_msg()
