# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: helloworld.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'helloworld.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\x0fhelloworld_gprc\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xa2\x01\n\x07Greeter\x12H\n\x08SayHello\x12\x1d.helloworld_gprc.HelloRequest\x1a\x1b.helloworld_gprc.HelloReply\"\x00\x12M\n\rSayHelloAgain\x12\x1d.helloworld_gprc.HelloRequest\x1a\x1b.helloworld_gprc.HelloReply\"\x00\x42;\n&it.unipi.dsmt_2024_2025.grpc.generatedB\x0fHelloWorldProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&it.unipi.dsmt_2024_2025.grpc.generatedB\017HelloWorldProtoP\001'
  _globals['_HELLOREQUEST']._serialized_start=37
  _globals['_HELLOREQUEST']._serialized_end=65
  _globals['_HELLOREPLY']._serialized_start=67
  _globals['_HELLOREPLY']._serialized_end=96
  _globals['_GREETER']._serialized_start=99
  _globals['_GREETER']._serialized_end=261
# @@protoc_insertion_point(module_scope)