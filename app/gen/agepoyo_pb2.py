# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: agepoyo.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 6, 31, 0, "", "agepoyo.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ragepoyo.proto\x12\x07\x61gepoyo\x1a\x1fgoogle/protobuf/timestamp.proto"^\n\x13\x43onversationMessage\x12-\n\x04role\x18\x01 \x01(\x0e\x32\x19.agepoyo.ConversationRoleR\x04role\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent"x\n\x13\x43onversationRequest\x12\x38\n\x08messages\x18\x01 \x03(\x0b\x32\x1c.agepoyo.ConversationMessageR\x08messages\x12\'\n\x05model\x18\x02 \x01(\x0e\x32\x11.agepoyo.LlmModelR\x05model"\xa8\x01\n\x14\x43onversationResponse\x12\x37\n\x0c\x63ontent_type\x18\x01 \x01(\x0e\x32\x14.agepoyo.ContentTypeR\x0b\x63ontentType\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12=\n\x0cgenerated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0bgeneratedAt*N\n\x10\x43onversationRole\x12!\n\x1d\x43ONVERSATION_ROLE_UNSPECIFIED\x10\x00\x12\x08\n\x04USER\x10\x01\x12\r\n\tASSISTANT\x10\x02*h\n\x08LlmModel\x12\x19\n\x15LLM_MODEL_UNSPECIFIED\x10\x00\x12\n\n\x06GPT_41\x10\x01\x12\n\n\x06GPT_4O\x10\x02\x12\x13\n\x0fGEMINI_20_FLASH\x10\x14\x12\x14\n\x10\x43LAUDE_37_SONNET\x10(*`\n\x0b\x43ontentType\x12\x1c\n\x18\x43ONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\t\n\x05\x41UDIO\x10\x03\x12\t\n\x05VIDEO\x10\x04\x12\x08\n\x04\x46ILE\x10\x05\x32\xbc\x01\n\x0e\x41gepoyoService\x12P\n\x11\x63onverseWithAgent\x12\x1c.agepoyo.ConversationRequest\x1a\x1d.agepoyo.ConversationResponse\x12X\n\x17\x63onverseWithAgentStream\x12\x1c.agepoyo.ConversationRequest\x1a\x1d.agepoyo.ConversationResponse0\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "agepoyo_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_CONVERSATIONROLE"]._serialized_start = 448
    _globals["_CONVERSATIONROLE"]._serialized_end = 526
    _globals["_LLMMODEL"]._serialized_start = 528
    _globals["_LLMMODEL"]._serialized_end = 632
    _globals["_CONTENTTYPE"]._serialized_start = 634
    _globals["_CONTENTTYPE"]._serialized_end = 730
    _globals["_CONVERSATIONMESSAGE"]._serialized_start = 59
    _globals["_CONVERSATIONMESSAGE"]._serialized_end = 153
    _globals["_CONVERSATIONREQUEST"]._serialized_start = 155
    _globals["_CONVERSATIONREQUEST"]._serialized_end = 275
    _globals["_CONVERSATIONRESPONSE"]._serialized_start = 278
    _globals["_CONVERSATIONRESPONSE"]._serialized_end = 446
    _globals["_AGEPOYOSERVICE"]._serialized_start = 733
    _globals["_AGEPOYOSERVICE"]._serialized_end = 921
# @@protoc_insertion_point(module_scope)
