#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  @Filename:    exercise_02
  @Author:      José Luis Corcuera Bárcena
  @Time:        10/30/24 10:11 AM
"""

from pyrlang.node import Node
from pyrlang.process import Process as PyrlangProcess
from Term.term.atom import Atom

node_name = "pyrlang_node2@127.0.0.1"
cookie = "abcde"
mailbox = "nodeMailBox"

class TestProcess(PyrlangProcess):

    def __init__(self, **kwargs) -> None:
        PyrlangProcess.__init__(self)
        self.get_node().register_name(self, Atom(mailbox))

    def handle_one_inbox_message(self, msg):
        print(f"msg: {msg}")


n = Node(node_name=node_name, cookie=cookie)
TestProcess()
n.run()
