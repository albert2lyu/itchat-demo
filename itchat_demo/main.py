#!/usr/bin/env python
# encoding: utf-8


import itchat
from msg_listener.mp_listener import MpListener
from msg_listener import mp_listener_s
from msg_sender.mp_sender import MpSender


if __name__ == '__main__':
	itchat.auto_login(hotReload=True, enableCmdQR=True)

	mp_listener = MpListener()
	mp_sender = MpSender()

	mp_listener.register_run()
	mp_sender.send_msg2mp()
