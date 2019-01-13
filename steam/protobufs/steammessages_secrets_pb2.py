# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_secrets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_secrets.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1bsteammessages_secrets.proto\x1a steammessages_unified_base.proto\"\x9b\x01\n\x12\x43KeyEscrow_Request\x12\x1b\n\x13rsa_oaep_sha_ticket\x18\x01 \x01(\x0c\x12\x10\n\x08password\x18\x02 \x01(\x0c\x12\x41\n\x05usage\x18\x03 \x01(\x0e\x32\x10.EKeyEscrowUsage: k_EKeyEscrowUsageStreamingDevice\x12\x13\n\x0b\x64\x65vice_name\x18\x04 \x01(\t\"\x82\x02\n\x11\x43KeyEscrow_Ticket\x12\x10\n\x08password\x18\x01 \x01(\x0c\x12\x12\n\nidentifier\x18\x02 \x01(\x04\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\r\x12\x41\n\x05usage\x18\x05 \x01(\x0e\x32\x10.EKeyEscrowUsage: k_EKeyEscrowUsageStreamingDevice\x12\x13\n\x0b\x64\x65vice_name\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x07 \x01(\t\x12\x15\n\rdevice_serial\x18\x08 \x01(\t\x12\x1e\n\x16\x64\x65vice_provisioning_id\x18\t \x01(\r\"9\n\x13\x43KeyEscrow_Response\x12\"\n\x06ticket\x18\x01 \x01(\x0b\x32\x12.CKeyEscrow_Ticket*7\n\x0f\x45KeyEscrowUsage\x12$\n k_EKeyEscrowUsageStreamingDevice\x10\x00\x32\xc8\x01\n\x07Secrets\x12\x80\x01\n\tKeyEscrow\x12\x13.CKeyEscrow_Request\x1a\x14.CKeyEscrow_Response\"H\x82\xb5\x18\x44Service to perform authenticated key-exchange involving Steam Client\x1a:\x82\xb5\x18\x36Service for accessing credentials and guarding secretsB\x03\x90\x01\x01')
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])

_EKEYESCROWUSAGE = _descriptor.EnumDescriptor(
  name='EKeyEscrowUsage',
  full_name='EKeyEscrowUsage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_EKeyEscrowUsageStreamingDevice', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=543,
  serialized_end=598,
)
_sym_db.RegisterEnumDescriptor(_EKEYESCROWUSAGE)

EKeyEscrowUsage = enum_type_wrapper.EnumTypeWrapper(_EKEYESCROWUSAGE)
k_EKeyEscrowUsageStreamingDevice = 0



_CKEYESCROW_REQUEST = _descriptor.Descriptor(
  name='CKeyEscrow_Request',
  full_name='CKeyEscrow_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rsa_oaep_sha_ticket', full_name='CKeyEscrow_Request.rsa_oaep_sha_ticket', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='CKeyEscrow_Request.password', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usage', full_name='CKeyEscrow_Request.usage', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='CKeyEscrow_Request.device_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=221,
)


_CKEYESCROW_TICKET = _descriptor.Descriptor(
  name='CKeyEscrow_Ticket',
  full_name='CKeyEscrow_Ticket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='password', full_name='CKeyEscrow_Ticket.password', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='CKeyEscrow_Ticket.identifier', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='CKeyEscrow_Ticket.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='CKeyEscrow_Ticket.timestamp', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usage', full_name='CKeyEscrow_Ticket.usage', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='CKeyEscrow_Ticket.device_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_model', full_name='CKeyEscrow_Ticket.device_model', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_serial', full_name='CKeyEscrow_Ticket.device_serial', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_provisioning_id', full_name='CKeyEscrow_Ticket.device_provisioning_id', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=482,
)


_CKEYESCROW_RESPONSE = _descriptor.Descriptor(
  name='CKeyEscrow_Response',
  full_name='CKeyEscrow_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticket', full_name='CKeyEscrow_Response.ticket', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=541,
)

_CKEYESCROW_REQUEST.fields_by_name['usage'].enum_type = _EKEYESCROWUSAGE
_CKEYESCROW_TICKET.fields_by_name['usage'].enum_type = _EKEYESCROWUSAGE
_CKEYESCROW_RESPONSE.fields_by_name['ticket'].message_type = _CKEYESCROW_TICKET
DESCRIPTOR.message_types_by_name['CKeyEscrow_Request'] = _CKEYESCROW_REQUEST
DESCRIPTOR.message_types_by_name['CKeyEscrow_Ticket'] = _CKEYESCROW_TICKET
DESCRIPTOR.message_types_by_name['CKeyEscrow_Response'] = _CKEYESCROW_RESPONSE
DESCRIPTOR.enum_types_by_name['EKeyEscrowUsage'] = _EKEYESCROWUSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CKeyEscrow_Request = _reflection.GeneratedProtocolMessageType('CKeyEscrow_Request', (_message.Message,), dict(
  DESCRIPTOR = _CKEYESCROW_REQUEST,
  __module__ = 'steammessages_secrets_pb2'
  # @@protoc_insertion_point(class_scope:CKeyEscrow_Request)
  ))
_sym_db.RegisterMessage(CKeyEscrow_Request)

CKeyEscrow_Ticket = _reflection.GeneratedProtocolMessageType('CKeyEscrow_Ticket', (_message.Message,), dict(
  DESCRIPTOR = _CKEYESCROW_TICKET,
  __module__ = 'steammessages_secrets_pb2'
  # @@protoc_insertion_point(class_scope:CKeyEscrow_Ticket)
  ))
_sym_db.RegisterMessage(CKeyEscrow_Ticket)

CKeyEscrow_Response = _reflection.GeneratedProtocolMessageType('CKeyEscrow_Response', (_message.Message,), dict(
  DESCRIPTOR = _CKEYESCROW_RESPONSE,
  __module__ = 'steammessages_secrets_pb2'
  # @@protoc_insertion_point(class_scope:CKeyEscrow_Response)
  ))
_sym_db.RegisterMessage(CKeyEscrow_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_SECRETS = _descriptor.ServiceDescriptor(
  name='Secrets',
  full_name='Secrets',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\202\265\0306Service for accessing credentials and guarding secrets')),
  serialized_start=601,
  serialized_end=801,
  methods=[
  _descriptor.MethodDescriptor(
    name='KeyEscrow',
    full_name='Secrets.KeyEscrow',
    index=0,
    containing_service=None,
    input_type=_CKEYESCROW_REQUEST,
    output_type=_CKEYESCROW_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030DService to perform authenticated key-exchange involving Steam Client')),
  ),
])

Secrets = service_reflection.GeneratedServiceType('Secrets', (_service.Service,), dict(
  DESCRIPTOR = _SECRETS,
  __module__ = 'steammessages_secrets_pb2'
  ))

Secrets_Stub = service_reflection.GeneratedServiceStubType('Secrets_Stub', (Secrets,), dict(
  DESCRIPTOR = _SECRETS,
  __module__ = 'steammessages_secrets_pb2'
  ))


# @@protoc_insertion_point(module_scope)
