#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  @Filename:    exercise_04a
  @Author:      José Luis Corcuera Bárcena
  @Time:        10/30/24 10:11 AM
"""
import pickle
import numpy as np
from pyrlang.node import Node
from pyrlang.process import Process as PyrlangProcess
from typing import Callable

from Term.term.atom import Atom

node_name = "pyrlang_node4a@127.0.0.1"
cookie = "abcde"
mailbox = "nodeMailBox"

pickle_dumps: Callable = pickle.dumps


class TestProcess(PyrlangProcess):

    def __init__(self, **kwargs) -> None:
        PyrlangProcess.__init__(self)
        self.get_node().register_name(self, Atom(mailbox))

    def handle_one_inbox_message(self, msg):
        print(f"incoming message: {msg}")
        sender_pid = msg[0]
        print(f"sender_pid: {sender_pid}")
        data_to_return = np.array([232, 545, 445, 64444])
        serialized_data = pickle_dumps(data_to_return)
        print(f"serialized_data: {serialized_data}")
        self.get_node().send_nowait(sender=self.pid_,
                                    receiver=sender_pid,
                                    message=(self.pid_, serialized_data))


n = Node(node_name=node_name, cookie=cookie)
TestProcess()
n.run()
