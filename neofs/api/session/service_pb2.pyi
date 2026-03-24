from refs import types_pb2 as _types_pb2
from session import types_pb2 as _types_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("owner_id", "expiration")
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        owner_id: _types_pb2.OwnerID
        expiration: int
        def __init__(self, owner_id: _Optional[_Union[_types_pb2.OwnerID, _Mapping]] = ..., expiration: _Optional[int] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: CreateRequest.Body
    meta_header: _types_pb2_1.RequestMetaHeader
    verify_header: _types_pb2_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[CreateRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("id", "session_key")
        ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
        id: bytes
        session_key: bytes
        def __init__(self, id: _Optional[bytes] = ..., session_key: _Optional[bytes] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: CreateResponse.Body
    meta_header: _types_pb2_1.ResponseMetaHeader
    verify_header: _types_pb2_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[CreateResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...
