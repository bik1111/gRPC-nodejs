# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63ustomers.proto\"\x07\n\x05\x45mpty\"B\n\x08\x43ustomer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\",\n\x0c\x43ustomerList\x12\x1c\n\tcustomers\x18\x01 \x03(\x0b\x32\t.Customer\"\x1f\n\x11\x43ustomerRequestId\x12\n\n\x02id\x18\x01 \x01(\t2\xc8\x01\n\x0f\x43ustomerService\x12!\n\x06GetAll\x12\x06.Empty\x1a\r.CustomerList\"\x00\x12&\n\x03Get\x12\x12.CustomerRequestId\x1a\t.Customer\"\x00\x12 \n\x06Insert\x12\t.Customer\x1a\t.Customer\"\x00\x12 \n\x06Update\x12\t.Customer\x1a\t.Customer\"\x00\x12&\n\x06Remove\x12\x12.CustomerRequestId\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'customers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=19
  _globals['_EMPTY']._serialized_end=26
  _globals['_CUSTOMER']._serialized_start=28
  _globals['_CUSTOMER']._serialized_end=94
  _globals['_CUSTOMERLIST']._serialized_start=96
  _globals['_CUSTOMERLIST']._serialized_end=140
  _globals['_CUSTOMERREQUESTID']._serialized_start=142
  _globals['_CUSTOMERREQUESTID']._serialized_end=173
  _globals['_CUSTOMERSERVICE']._serialized_start=176
  _globals['_CUSTOMERSERVICE']._serialized_end=376
# @@protoc_insertion_point(module_scope)