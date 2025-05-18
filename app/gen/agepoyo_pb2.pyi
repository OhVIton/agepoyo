from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
import datetime

DESCRIPTOR: _descriptor.FileDescriptor

class ConversationRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_ROLE_UNSPECIFIED: _ClassVar[ConversationRole]
    USER: _ClassVar[ConversationRole]
    ASSISTANT: _ClassVar[ConversationRole]

class LlmModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LLM_MODEL_UNSPECIFIED: _ClassVar[LlmModel]
    GPT_41: _ClassVar[LlmModel]
    GPT_4O: _ClassVar[LlmModel]
    GEMINI_20_FLASH: _ClassVar[LlmModel]
    CLAUDE_37_SONNET: _ClassVar[LlmModel]

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_UNSPECIFIED: _ClassVar[ContentType]
    TEXT: _ClassVar[ContentType]
    IMAGE: _ClassVar[ContentType]
    AUDIO: _ClassVar[ContentType]
    VIDEO: _ClassVar[ContentType]
    FILE: _ClassVar[ContentType]

CONVERSATION_ROLE_UNSPECIFIED: ConversationRole
USER: ConversationRole
ASSISTANT: ConversationRole
LLM_MODEL_UNSPECIFIED: LlmModel
GPT_41: LlmModel
GPT_4O: LlmModel
GEMINI_20_FLASH: LlmModel
CLAUDE_37_SONNET: LlmModel
CONTENT_TYPE_UNSPECIFIED: ContentType
TEXT: ContentType
IMAGE: ContentType
AUDIO: ContentType
VIDEO: ContentType
FILE: ContentType

class ConversationMessage(_message.Message):
    __slots__ = ("role", "content")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    role: ConversationRole
    content: str
    def __init__(
        self,
        role: _Optional[_Union[ConversationRole, str]] = ...,
        content: _Optional[str] = ...,
    ) -> None: ...

class ConversationRequest(_message.Message):
    __slots__ = ("messages", "model")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ConversationMessage]
    model: LlmModel
    def __init__(
        self,
        messages: _Optional[_Iterable[_Union[ConversationMessage, _Mapping]]] = ...,
        model: _Optional[_Union[LlmModel, str]] = ...,
    ) -> None: ...

class ConversationResponse(_message.Message):
    __slots__ = ("content_type", "content", "generated_at")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    content_type: ContentType
    content: str
    generated_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        content_type: _Optional[_Union[ContentType, str]] = ...,
        content: _Optional[str] = ...,
        generated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
