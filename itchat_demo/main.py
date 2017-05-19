#!/usr/bin/env python
# encoding: utf-8


import itchat
from msg_listener import mp_listener
from msg_sender import mp_sender


if __name__ == '__main__':
	itchat.auto_login(hotReload=True, enableCmdQR=True)
	mp_listener.register_run()
	mp_sender.send_msg2mp()
