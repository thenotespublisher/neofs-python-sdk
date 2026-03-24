from reputation import types_pb2 as _types_pb2
from session import types_pb2 as _types_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnnounceLocalTrustRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("epoch", "trusts")
        EPOCH_FIELD_NUMBER: _ClassVar[int]
        TRUSTS_FIELD_NUMBER: _ClassVar[int]
        epoch: int
        trusts: _containers.RepeatedCompositeFieldContainer[_types_pb2.Trust]
        def __init__(self, epoch: _Optional[int] = ..., trusts: _Optional[_Iterable[_Union[_types_pb2.Trust, _Mapping]]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: AnnounceLocalTrustRequest.Body
    meta_header: _types_pb2_1.RequestMetaHeader
    verify_header: _types_pb2_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[AnnounceLocalTrustRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class AnnounceLocalTrustResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: AnnounceLocalTrustResponse.Body
    meta_header: _types_pb2_1.ResponseMetaHeader
    verify_header: _types_pb2_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[AnnounceLocalTrustResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class AnnounceIntermediateResultRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("epoch", "iteration", "trust")
        EPOCH_FIELD_NUMBER: _ClassVar[int]
        ITERATION_FIELD_NUMBER: _ClassVar[int]
        TRUST_FIELD_NUMBER: _ClassVar[int]
        epoch: int
        iteration: int
        trust: _types_pb2.PeerToPeerTrust
        def __init__(self, epoch: _Optional[int] = ..., iteration: _Optional[int] = ..., trust: _Optional[_Union[_types_pb2.PeerToPeerTrust, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: AnnounceIntermediateResultRequest.Body
    meta_header: _types_pb2_1.RequestMetaHeader
    verify_header: _types_pb2_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[AnnounceIntermediateResultRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class AnnounceIntermediateResultResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: AnnounceIntermediateResultResponse.Body
    meta_header: _types_pb2_1.ResponseMetaHeader
    verify_header: _types_pb2_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[AnnounceIntermediateResultResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...
