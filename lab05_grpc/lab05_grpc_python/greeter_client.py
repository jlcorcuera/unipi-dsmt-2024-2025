#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  @Filename:    greeter_client
  @Author:      José Luis Corcuera Bárcena
  @Time:        10/31/24 3:59 PM
"""
import logging
import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8999') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
