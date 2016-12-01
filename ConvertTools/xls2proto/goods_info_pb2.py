# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='goods_info.proto',
  package='tnt_deploy',
  serialized_pb='\n\x10goods_info.proto\x12\ntnt_deploy\"\xc4\x07\n\nGOODS_INFO\x12\x13\n\x08goods_id\x18\x01 \x02(\r:\x01\x30\x12\x0e\n\x04name\x18\x02 \x01(\x0c:\x00\x12\x0e\n\x03sex\x18\x03 \x01(\r:\x01\x30\x12\x16\n\x0blevel_limit\x18\x04 \x01(\r:\x01\x30\x12\x19\n\x0e\x63lub_vip_level\x18\x05 \x01(\x05:\x01\x30\x12\x0f\n\x04qb_2\x18\x06 \x01(\x05:\x01\x30\x12\x17\n\x0c\x63onsume_type\x18\x07 \x01(\r:\x01\x30\x12\x14\n\ttime_unit\x18\x08 \x01(\r:\x01\x30\x12\x14\n\tis_online\x18\t \x01(\r:\x01\x30\x12\x12\n\x07\x63\x61n_buy\x18\n \x01(\r:\x01\x30\x12\x17\n\x0c\x63\x61n_recharge\x18\x0b \x01(\r:\x01\x30\x12\x15\n\x0bonline_time\x18\x0c \x01(\x0c:\x00\x12\x16\n\x0coffline_time\x18\r \x01(\x0c:\x00\x12\x1f\n\x17privileged_plat_id_list\x18\x0e \x03(\r\x12$\n\x19privileged_plat_is_online\x18\x0f \x01(\r:\x01\x30\x12\"\n\x17privileged_plat_can_buy\x18\x10 \x01(\r:\x01\x30\x12\'\n\x1cprivileged_plat_can_recharge\x18\x11 \x01(\r:\x01\x30\x12\x18\n\rpayment_terms\x18\x12 \x01(\r:\x01\x30\x12\x14\n\nvalid_time\x18\x13 \x01(\x0c:\x00\x12\x18\n\rsort_priority\x18\x14 \x01(\r:\x01\x30\x12\x16\n\x0bsuit_number\x18\x15 \x01(\x05:\x01\x30\x12\x1c\n\x11\x62\x61g_sort_priority\x18\x16 \x01(\r:\x01\x30\x12\x10\n\x06status\x18\x17 \x01(\x0c:\x00\x12\x0f\n\x04rank\x18\x18 \x01(\r:\x01\x30\x12\x19\n\x0eprice_discount\x18\x19 \x01(\r:\x01\x30\x12\x17\n\x0cvip_discount\x18\x1a \x01(\r:\x01\x30\x12\x31\n\x0bprice_table\x18\x1b \x03(\x0b\x32\x1c.tnt_deploy.GOODS_INFO.Price\x12\x34\n\ngoods_attr\x18\x1c \x03(\x0b\x32 .tnt_deploy.GOODS_INFO.GoodsAttr\x12\x15\n\x0b\x64\x65scription\x18\x1d \x01(\x0c:\x00\x12\x13\n\x08limit_id\x18\x1e \x01(\r:\x01\x30\x12\x15\n\x0bsubSystemId\x18\x1f \x01(\x0c:\x00\x1aK\n\x05Price\x12\x13\n\x08price_dq\x18\x01 \x01(\r:\x01\x30\x12\x15\n\nprice_gold\x18\x02 \x01(\r:\x01\x30\x12\x16\n\x0bprice_value\x18\x03 \x01(\r:\x01\x30\x1a\x38\n\tGoodsAttr\x12\x14\n\tattr_type\x18\x01 \x01(\r:\x01\x30\x12\x15\n\nattr_value\x18\x02 \x01(\r:\x01\x30\"9\n\x10GOODS_INFO_ARRAY\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.tnt_deploy.GOODS_INFO')




_GOODS_INFO_PRICE = descriptor.Descriptor(
  name='Price',
  full_name='tnt_deploy.GOODS_INFO.Price',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='price_dq', full_name='tnt_deploy.GOODS_INFO.Price.price_dq', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price_gold', full_name='tnt_deploy.GOODS_INFO.Price.price_gold', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price_value', full_name='tnt_deploy.GOODS_INFO.Price.price_value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  serialized_start=864,
  serialized_end=939,
)

_GOODS_INFO_GOODSATTR = descriptor.Descriptor(
  name='GoodsAttr',
  full_name='tnt_deploy.GOODS_INFO.GoodsAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr_type', full_name='tnt_deploy.GOODS_INFO.GoodsAttr.attr_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr_value', full_name='tnt_deploy.GOODS_INFO.GoodsAttr.attr_value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  serialized_start=941,
  serialized_end=997,
)

_GOODS_INFO = descriptor.Descriptor(
  name='GOODS_INFO',
  full_name='tnt_deploy.GOODS_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='goods_id', full_name='tnt_deploy.GOODS_INFO.goods_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='tnt_deploy.GOODS_INFO.name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sex', full_name='tnt_deploy.GOODS_INFO.sex', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level_limit', full_name='tnt_deploy.GOODS_INFO.level_limit', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='club_vip_level', full_name='tnt_deploy.GOODS_INFO.club_vip_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='qb_2', full_name='tnt_deploy.GOODS_INFO.qb_2', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='consume_type', full_name='tnt_deploy.GOODS_INFO.consume_type', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_unit', full_name='tnt_deploy.GOODS_INFO.time_unit', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_online', full_name='tnt_deploy.GOODS_INFO.is_online', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='can_buy', full_name='tnt_deploy.GOODS_INFO.can_buy', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='can_recharge', full_name='tnt_deploy.GOODS_INFO.can_recharge', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='online_time', full_name='tnt_deploy.GOODS_INFO.online_time', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offline_time', full_name='tnt_deploy.GOODS_INFO.offline_time', index=12,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='privileged_plat_id_list', full_name='tnt_deploy.GOODS_INFO.privileged_plat_id_list', index=13,
      number=14, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='privileged_plat_is_online', full_name='tnt_deploy.GOODS_INFO.privileged_plat_is_online', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='privileged_plat_can_buy', full_name='tnt_deploy.GOODS_INFO.privileged_plat_can_buy', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='privileged_plat_can_recharge', full_name='tnt_deploy.GOODS_INFO.privileged_plat_can_recharge', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='payment_terms', full_name='tnt_deploy.GOODS_INFO.payment_terms', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='valid_time', full_name='tnt_deploy.GOODS_INFO.valid_time', index=18,
      number=19, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sort_priority', full_name='tnt_deploy.GOODS_INFO.sort_priority', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suit_number', full_name='tnt_deploy.GOODS_INFO.suit_number', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bag_sort_priority', full_name='tnt_deploy.GOODS_INFO.bag_sort_priority', index=21,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='tnt_deploy.GOODS_INFO.status', index=22,
      number=23, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank', full_name='tnt_deploy.GOODS_INFO.rank', index=23,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price_discount', full_name='tnt_deploy.GOODS_INFO.price_discount', index=24,
      number=25, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vip_discount', full_name='tnt_deploy.GOODS_INFO.vip_discount', index=25,
      number=26, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price_table', full_name='tnt_deploy.GOODS_INFO.price_table', index=26,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='goods_attr', full_name='tnt_deploy.GOODS_INFO.goods_attr', index=27,
      number=28, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='tnt_deploy.GOODS_INFO.description', index=28,
      number=29, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='limit_id', full_name='tnt_deploy.GOODS_INFO.limit_id', index=29,
      number=30, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='subSystemId', full_name='tnt_deploy.GOODS_INFO.subSystemId', index=30,
      number=31, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GOODS_INFO_PRICE, _GOODS_INFO_GOODSATTR, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=33,
  serialized_end=997,
)


_GOODS_INFO_ARRAY = descriptor.Descriptor(
  name='GOODS_INFO_ARRAY',
  full_name='tnt_deploy.GOODS_INFO_ARRAY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='items', full_name='tnt_deploy.GOODS_INFO_ARRAY.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=999,
  serialized_end=1056,
)

_GOODS_INFO_PRICE.containing_type = _GOODS_INFO;
_GOODS_INFO_GOODSATTR.containing_type = _GOODS_INFO;
_GOODS_INFO.fields_by_name['price_table'].message_type = _GOODS_INFO_PRICE
_GOODS_INFO.fields_by_name['goods_attr'].message_type = _GOODS_INFO_GOODSATTR
_GOODS_INFO_ARRAY.fields_by_name['items'].message_type = _GOODS_INFO
DESCRIPTOR.message_types_by_name['GOODS_INFO'] = _GOODS_INFO
DESCRIPTOR.message_types_by_name['GOODS_INFO_ARRAY'] = _GOODS_INFO_ARRAY

class GOODS_INFO(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Price(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GOODS_INFO_PRICE
    
    # @@protoc_insertion_point(class_scope:tnt_deploy.GOODS_INFO.Price)
  
  class GoodsAttr(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GOODS_INFO_GOODSATTR
    
    # @@protoc_insertion_point(class_scope:tnt_deploy.GOODS_INFO.GoodsAttr)
  DESCRIPTOR = _GOODS_INFO
  
  # @@protoc_insertion_point(class_scope:tnt_deploy.GOODS_INFO)

class GOODS_INFO_ARRAY(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOODS_INFO_ARRAY
  
  # @@protoc_insertion_point(class_scope:tnt_deploy.GOODS_INFO_ARRAY)

# @@protoc_insertion_point(module_scope)
