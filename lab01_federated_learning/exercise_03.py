#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  @Filename:    exercise_03
  @Author:      José Luis Corcuera Bárcena
  @Time:        10/30/24 10:11 AM
"""

from pyrlang.node import Node
from pyrlang.process import Process as PyrlangProcess
from Term.term.atom import Atom

node_name = "pyrlang_node3@127.0.0.1"
cookie = "abcde"
mailbox = "nodeMailBox"


class TestProcess(PyrlangProcess):

    def __init__(self, **kwargs) -> None:
        PyrlangProcess.__init__(self)
        self.get_node().register_name(self, Atom(mailbox))

    def handle_one_inbox_message(self, msg):
        print(f"incoming message: {msg}")
        sender_pid = msg[0]
        data = msg[1]
        print(f"sender_pid: {sender_pid}")
        print(f"data type: {type(data)}, data = {data}")
        min_value = min(data)
        max_value = max(data)
        sum_value = sum(data)

        self.get_node().send_nowait(sender=self.pid_,
                                    receiver=sender_pid,
                                    message=(self.pid_, sum_value, max_value, min_value))


n = Node(node_name=node_name, cookie=cookie)
TestProcess()
n.run()
