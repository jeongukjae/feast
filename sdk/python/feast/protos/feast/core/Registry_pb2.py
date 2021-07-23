# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Registry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from feast.protos.feast.core import Entity_pb2 as feast_dot_core_dot_Entity__pb2
from feast.protos.feast.core import (
    FeatureTable_pb2 as feast_dot_core_dot_FeatureTable__pb2,
)
from feast.protos.feast.core import (
    FeatureView_pb2 as feast_dot_core_dot_FeatureView__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/Registry.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=b'\n\020feast.proto.coreB\rRegistryProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x66\x65\x61st/core/Registry.proto\x12\nfeast.core\x1a\x17\x66\x65\x61st/core/Entity.proto\x1a\x1d\x66\x65\x61st/core/FeatureTable.proto\x1a\x1c\x66\x65\x61st/core/FeatureView.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf9\x01\n\x08Registry\x12$\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x12.feast.core.Entity\x12\x30\n\x0e\x66\x65\x61ture_tables\x18\x02 \x03(\x0b\x32\x18.feast.core.FeatureTable\x12.\n\rfeature_views\x18\x06 \x03(\x0b\x32\x17.feast.core.FeatureView\x12\x1f\n\x17registry_schema_version\x18\x03 \x01(\t\x12\x12\n\nversion_id\x18\x04 \x01(\t\x12\x30\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampBV\n\x10\x66\x65\x61st.proto.coreB\rRegistryProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/coreb\x06proto3'
  ,
  dependencies=[feast_dot_core_dot_Entity__pb2.DESCRIPTOR,feast_dot_core_dot_FeatureTable__pb2.DESCRIPTOR,feast_dot_core_dot_FeatureView__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_REGISTRY = _descriptor.Descriptor(
  name='Registry',
  full_name='feast.core.Registry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.Registry.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_tables', full_name='feast.core.Registry.feature_tables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_views', full_name='feast.core.Registry.feature_views', index=2,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registry_schema_version', full_name='feast.core.Registry.registry_schema_version', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='feast.core.Registry.version_id', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='feast.core.Registry.last_updated', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=410,
)

_REGISTRY.fields_by_name['entities'].message_type = feast_dot_core_dot_Entity__pb2._ENTITY
_REGISTRY.fields_by_name['feature_tables'].message_type = feast_dot_core_dot_FeatureTable__pb2._FEATURETABLE
_REGISTRY.fields_by_name['feature_views'].message_type = feast_dot_core_dot_FeatureView__pb2._FEATUREVIEW
_REGISTRY.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Registry'] = _REGISTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Registry = _reflection.GeneratedProtocolMessageType('Registry', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRY,
  '__module__' : 'feast.core.Registry_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.Registry)
  })
_sym_db.RegisterMessage(Registry)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)