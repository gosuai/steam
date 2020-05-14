# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_shader.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_shader.proto',
  package='',
  syntax='proto2',
  serialized_options=b'\220\001\001',
  serialized_pb=b'\n\x1asteammessages_shader.proto\x1a steammessages_unified_base.proto\"\xc9\x01\n\x1e\x43Shader_RegisterShader_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08gpu_desc\x18\x02 \x01(\t\x12\x13\n\x0b\x64river_desc\x18\x03 \x01(\t\x12\x37\n\x07shaders\x18\x04 \x03(\x0b\x32&.CShader_RegisterShader_Request.Shader\x1a\x38\n\x06Shader\x12\x15\n\rcache_key_sha\x18\x01 \x01(\x0c\x12\x17\n\x0fshader_code_sha\x18\x02 \x01(\x0c\"<\n\x1f\x43Shader_RegisterShader_Response\x12\x19\n\x11requested_codeids\x18\x01 \x03(\r\"\xa0\x01\n\x1a\x43Shader_SendShader_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x37\n\x07shaders\x18\x02 \x03(\x0b\x32&.CShader_SendShader_Request.ShaderCode\x1a:\n\nShaderCode\x12\x17\n\x0fshader_code_sha\x18\x01 \x01(\x0c\x12\x13\n\x0bshader_code\x18\x02 \x01(\x0c\"\x1d\n\x1b\x43Shader_SendShader_Response\"Y\n!CShader_GetBucketManifest_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08gpu_desc\x18\x02 \x01(\t\x12\x13\n\x0b\x64river_desc\x18\x03 \x01(\t\"]\n\"CShader_GetBucketManifest_Response\x12\x12\n\nmanifestid\x18\x01 \x01(\x04\x12\x11\n\tdepotsize\x18\x02 \x01(\r\x12\x10\n\x08\x62ucketid\x18\x03 \x01(\x04\x32\x9f\x04\n\x06Shader\x12\xbe\x01\n\x0eRegisterShader\x12\x1f.CShader_RegisterShader_Request\x1a .CShader_RegisterShader_Response\"i\x82\xb5\x18\x65\x43lient just finished playing a game, detected new shader cache entries and is notifying us about them\x12\x8f\x01\n\nSendShader\x12\x1b.CShader_SendShader_Request\x1a\x1c.CShader_SendShader_Response\"F\x82\xb5\x18\x42\x43lient is sending us actual compiled shader code that we requested\x12\xad\x01\n\x11GetBucketManifest\x12\".CShader_GetBucketManifest_Request\x1a#.CShader_GetBucketManifest_Response\"O\x82\xb5\x18KClient wants to know the manifest ID to fetch (if any) for a bucket\'s depot\x1a\x12\x82\xb5\x18\x0eShader methodsB\x03\x90\x01\x01'
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])




_CSHADER_REGISTERSHADER_REQUEST_SHADER = _descriptor.Descriptor(
  name='Shader',
  full_name='CShader_RegisterShader_Request.Shader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cache_key_sha', full_name='CShader_RegisterShader_Request.Shader.cache_key_sha', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shader_code_sha', full_name='CShader_RegisterShader_Request.Shader.shader_code_sha', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=266,
)

_CSHADER_REGISTERSHADER_REQUEST = _descriptor.Descriptor(
  name='CShader_RegisterShader_Request',
  full_name='CShader_RegisterShader_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CShader_RegisterShader_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_desc', full_name='CShader_RegisterShader_Request.gpu_desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driver_desc', full_name='CShader_RegisterShader_Request.driver_desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shaders', full_name='CShader_RegisterShader_Request.shaders', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CSHADER_REGISTERSHADER_REQUEST_SHADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=266,
)


_CSHADER_REGISTERSHADER_RESPONSE = _descriptor.Descriptor(
  name='CShader_RegisterShader_Response',
  full_name='CShader_RegisterShader_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_codeids', full_name='CShader_RegisterShader_Response.requested_codeids', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=328,
)


_CSHADER_SENDSHADER_REQUEST_SHADERCODE = _descriptor.Descriptor(
  name='ShaderCode',
  full_name='CShader_SendShader_Request.ShaderCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shader_code_sha', full_name='CShader_SendShader_Request.ShaderCode.shader_code_sha', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shader_code', full_name='CShader_SendShader_Request.ShaderCode.shader_code', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=491,
)

_CSHADER_SENDSHADER_REQUEST = _descriptor.Descriptor(
  name='CShader_SendShader_Request',
  full_name='CShader_SendShader_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CShader_SendShader_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shaders', full_name='CShader_SendShader_Request.shaders', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CSHADER_SENDSHADER_REQUEST_SHADERCODE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=491,
)


_CSHADER_SENDSHADER_RESPONSE = _descriptor.Descriptor(
  name='CShader_SendShader_Response',
  full_name='CShader_SendShader_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=522,
)


_CSHADER_GETBUCKETMANIFEST_REQUEST = _descriptor.Descriptor(
  name='CShader_GetBucketManifest_Request',
  full_name='CShader_GetBucketManifest_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CShader_GetBucketManifest_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_desc', full_name='CShader_GetBucketManifest_Request.gpu_desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driver_desc', full_name='CShader_GetBucketManifest_Request.driver_desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=613,
)


_CSHADER_GETBUCKETMANIFEST_RESPONSE = _descriptor.Descriptor(
  name='CShader_GetBucketManifest_Response',
  full_name='CShader_GetBucketManifest_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manifestid', full_name='CShader_GetBucketManifest_Response.manifestid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depotsize', full_name='CShader_GetBucketManifest_Response.depotsize', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketid', full_name='CShader_GetBucketManifest_Response.bucketid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=615,
  serialized_end=708,
)

_CSHADER_REGISTERSHADER_REQUEST_SHADER.containing_type = _CSHADER_REGISTERSHADER_REQUEST
_CSHADER_REGISTERSHADER_REQUEST.fields_by_name['shaders'].message_type = _CSHADER_REGISTERSHADER_REQUEST_SHADER
_CSHADER_SENDSHADER_REQUEST_SHADERCODE.containing_type = _CSHADER_SENDSHADER_REQUEST
_CSHADER_SENDSHADER_REQUEST.fields_by_name['shaders'].message_type = _CSHADER_SENDSHADER_REQUEST_SHADERCODE
DESCRIPTOR.message_types_by_name['CShader_RegisterShader_Request'] = _CSHADER_REGISTERSHADER_REQUEST
DESCRIPTOR.message_types_by_name['CShader_RegisterShader_Response'] = _CSHADER_REGISTERSHADER_RESPONSE
DESCRIPTOR.message_types_by_name['CShader_SendShader_Request'] = _CSHADER_SENDSHADER_REQUEST
DESCRIPTOR.message_types_by_name['CShader_SendShader_Response'] = _CSHADER_SENDSHADER_RESPONSE
DESCRIPTOR.message_types_by_name['CShader_GetBucketManifest_Request'] = _CSHADER_GETBUCKETMANIFEST_REQUEST
DESCRIPTOR.message_types_by_name['CShader_GetBucketManifest_Response'] = _CSHADER_GETBUCKETMANIFEST_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CShader_RegisterShader_Request = _reflection.GeneratedProtocolMessageType('CShader_RegisterShader_Request', (_message.Message,), {

  'Shader' : _reflection.GeneratedProtocolMessageType('Shader', (_message.Message,), {
    'DESCRIPTOR' : _CSHADER_REGISTERSHADER_REQUEST_SHADER,
    '__module__' : 'steammessages_shader_pb2'
    # @@protoc_insertion_point(class_scope:CShader_RegisterShader_Request.Shader)
    })
  ,
  'DESCRIPTOR' : _CSHADER_REGISTERSHADER_REQUEST,
  '__module__' : 'steammessages_shader_pb2'
  # @@protoc_insertion_point(class_scope:CShader_RegisterShader_Request)
  })
_sym_db.RegisterMessage(CShader_RegisterShader_Request)
_sym_db.RegisterMessage(CShader_RegisterShader_Request.Shader)

CShader_RegisterShader_Response = _reflection.GeneratedProtocolMessageType('CShader_RegisterShader_Response', (_message.Message,), {
  'DESCRIPTOR' : _CSHADER_REGISTERSHADER_RESPONSE,
  '__module__' : 'steammessages_shader_pb2'
  # @@protoc_insertion_point(class_scope:CShader_RegisterShader_Response)
  })
_sym_db.RegisterMessage(CShader_RegisterShader_Response)

CShader_SendShader_Request = _reflection.GeneratedProtocolMessageType('CShader_SendShader_Request', (_message.Message,), {

  'ShaderCode' : _reflection.GeneratedProtocolMessageType('ShaderCode', (_message.Message,), {
    'DESCRIPTOR' : _CSHADER_SENDSHADER_REQUEST_SHADERCODE,
    '__module__' : 'steammessages_shader_pb2'
    # @@protoc_insertion_point(class_scope:CShader_SendShader_Request.ShaderCode)
    })
  ,
  'DESCRIPTOR' : _CSHADER_SENDSHADER_REQUEST,
  '__module__' : 'steammessages_shader_pb2'
  # @@protoc_insertion_point(class_scope:CShader_SendShader_Request)
  })
_sym_db.RegisterMessage(CShader_SendShader_Request)
_sym_db.RegisterMessage(CShader_SendShader_Request.ShaderCode)

CShader_SendShader_Response = _reflection.GeneratedProtocolMessageType('CShader_SendShader_Response', (_message.Message,), {
  'DESCRIPTOR' : _CSHADER_SENDSHADER_RESPONSE,
  '__module__' : 'steammessages_shader_pb2'
  # @@protoc_insertion_point(class_scope:CShader_SendShader_Response)
  })
_sym_db.RegisterMessage(CShader_SendShader_Response)

CShader_GetBucketManifest_Request = _reflection.GeneratedProtocolMessageType('CShader_GetBucketManifest_Request', (_message.Message,), {
  'DESCRIPTOR' : _CSHADER_GETBUCKETMANIFEST_REQUEST,
  '__module__' : 'steammessages_shader_pb2'
  # @@protoc_insertion_point(class_scope:CShader_GetBucketManifest_Request)
  })
_sym_db.RegisterMessage(CShader_GetBucketManifest_Request)

CShader_GetBucketManifest_Response = _reflection.GeneratedProtocolMessageType('CShader_GetBucketManifest_Response', (_message.Message,), {
  'DESCRIPTOR' : _CSHADER_GETBUCKETMANIFEST_RESPONSE,
  '__module__' : 'steammessages_shader_pb2'
  # @@protoc_insertion_point(class_scope:CShader_GetBucketManifest_Response)
  })
_sym_db.RegisterMessage(CShader_GetBucketManifest_Response)


DESCRIPTOR._options = None

_SHADER = _descriptor.ServiceDescriptor(
  name='Shader',
  full_name='Shader',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\202\265\030\016Shader methods',
  serialized_start=711,
  serialized_end=1254,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterShader',
    full_name='Shader.RegisterShader',
    index=0,
    containing_service=None,
    input_type=_CSHADER_REGISTERSHADER_REQUEST,
    output_type=_CSHADER_REGISTERSHADER_RESPONSE,
    serialized_options=b'\202\265\030eClient just finished playing a game, detected new shader cache entries and is notifying us about them',
  ),
  _descriptor.MethodDescriptor(
    name='SendShader',
    full_name='Shader.SendShader',
    index=1,
    containing_service=None,
    input_type=_CSHADER_SENDSHADER_REQUEST,
    output_type=_CSHADER_SENDSHADER_RESPONSE,
    serialized_options=b'\202\265\030BClient is sending us actual compiled shader code that we requested',
  ),
  _descriptor.MethodDescriptor(
    name='GetBucketManifest',
    full_name='Shader.GetBucketManifest',
    index=2,
    containing_service=None,
    input_type=_CSHADER_GETBUCKETMANIFEST_REQUEST,
    output_type=_CSHADER_GETBUCKETMANIFEST_RESPONSE,
    serialized_options=b'\202\265\030KClient wants to know the manifest ID to fetch (if any) for a bucket\'s depot',
  ),
])
_sym_db.RegisterServiceDescriptor(_SHADER)

DESCRIPTOR.services_by_name['Shader'] = _SHADER

Shader = service_reflection.GeneratedServiceType('Shader', (_service.Service,), dict(
  DESCRIPTOR = _SHADER,
  __module__ = 'steammessages_shader_pb2'
  ))

Shader_Stub = service_reflection.GeneratedServiceStubType('Shader_Stub', (Shader,), dict(
  DESCRIPTOR = _SHADER,
  __module__ = 'steammessages_shader_pb2'
  ))


# @@protoc_insertion_point(module_scope)
