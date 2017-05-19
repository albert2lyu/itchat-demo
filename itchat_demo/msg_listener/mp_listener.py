#!/usr/bin/env python
# encoding: utf-8


import threading

import itchat
from itchat.content import TEXT


@itchat.msg_register(TEXT, isMpChat=True)
def text_show(msg):
	print('- %s' % msg.text)


def msg_loog_mp():
	itchat.run(True)


def register_run():
	recv_mp_t = threading.Thread(target=msg_loog_mp, name='msg_recv_mp')
	recv_mp_t.start()
