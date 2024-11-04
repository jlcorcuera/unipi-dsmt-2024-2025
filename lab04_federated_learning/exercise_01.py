#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  @Filename:    exercise_01
  @Author:      José Luis Corcuera Bárcena
  @Time:        10/30/24 10:09 AM
"""

from pyrlang.node import Node

node_name = "pyrlang_node1@127.0.0.1"
cookie = "abcde"

n = Node(node_name=node_name, cookie=cookie)

n.run()
