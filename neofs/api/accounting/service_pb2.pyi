from accounting import types_pb2 as _types_pb2
from refs import types_pb2 as _types_pb2_1
from session import types_pb2 as _types_pb2_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BalanceRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("owner_id",)
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        owner_id: _types_pb2_1.OwnerID
        def __init__(self, owner_id: _Optional[_Union[_types_pb2_1.OwnerID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: BalanceRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[BalanceRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class BalanceResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("balance",)
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        balance: _types_pb2.Decimal
        def __init__(self, balance: _Optional[_Union[_types_pb2.Decimal, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: BalanceResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[BalanceResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...
