from object import types_pb2 as _types_pb2
from refs import types_pb2 as _types_pb2_1
from session import types_pb2 as _types_pb2_1_1
from status import types_pb2 as _types_pb2_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("address", "raw")
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        RAW_FIELD_NUMBER: _ClassVar[int]
        address: _types_pb2_1.Address
        raw: bool
        def __init__(self, address: _Optional[_Union[_types_pb2_1.Address, _Mapping]] = ..., raw: bool = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[GetRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("init", "chunk", "split_info")
        class Init(_message.Message):
            __slots__ = ("object_id", "signature", "header")
            OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
            SIGNATURE_FIELD_NUMBER: _ClassVar[int]
            HEADER_FIELD_NUMBER: _ClassVar[int]
            object_id: _types_pb2_1.ObjectID
            signature: _types_pb2_1.Signature
            header: _types_pb2.Header
            def __init__(self, object_id: _Optional[_Union[_types_pb2_1.ObjectID, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., header: _Optional[_Union[_types_pb2.Header, _Mapping]] = ...) -> None: ...
        INIT_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        SPLIT_INFO_FIELD_NUMBER: _ClassVar[int]
        init: GetResponse.Body.Init
        chunk: bytes
        split_info: _types_pb2.SplitInfo
        def __init__(self, init: _Optional[_Union[GetResponse.Body.Init, _Mapping]] = ..., chunk: _Optional[bytes] = ..., split_info: _Optional[_Union[_types_pb2.SplitInfo, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[GetResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class PutRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("init", "chunk")
        class Init(_message.Message):
            __slots__ = ("object_id", "signature", "header", "copies_number")
            OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
            SIGNATURE_FIELD_NUMBER: _ClassVar[int]
            HEADER_FIELD_NUMBER: _ClassVar[int]
            COPIES_NUMBER_FIELD_NUMBER: _ClassVar[int]
            object_id: _types_pb2_1.ObjectID
            signature: _types_pb2_1.Signature
            header: _types_pb2.Header
            copies_number: int
            def __init__(self, object_id: _Optional[_Union[_types_pb2_1.ObjectID, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., header: _Optional[_Union[_types_pb2.Header, _Mapping]] = ..., copies_number: _Optional[int] = ...) -> None: ...
        INIT_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        init: PutRequest.Body.Init
        chunk: bytes
        def __init__(self, init: _Optional[_Union[PutRequest.Body.Init, _Mapping]] = ..., chunk: _Optional[bytes] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: PutRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[PutRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class PutResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("object_id",)
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        object_id: _types_pb2_1.ObjectID
        def __init__(self, object_id: _Optional[_Union[_types_pb2_1.ObjectID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: PutResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[PutResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("address",)
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        address: _types_pb2_1.Address
        def __init__(self, address: _Optional[_Union[_types_pb2_1.Address, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: DeleteRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[DeleteRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("tombstone",)
        TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
        tombstone: _types_pb2_1.Address
        def __init__(self, tombstone: _Optional[_Union[_types_pb2_1.Address, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: DeleteResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[DeleteResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class HeadRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("address", "main_only", "raw")
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        MAIN_ONLY_FIELD_NUMBER: _ClassVar[int]
        RAW_FIELD_NUMBER: _ClassVar[int]
        address: _types_pb2_1.Address
        main_only: bool
        raw: bool
        def __init__(self, address: _Optional[_Union[_types_pb2_1.Address, _Mapping]] = ..., main_only: bool = ..., raw: bool = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: HeadRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[HeadRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class HeaderWithSignature(_message.Message):
    __slots__ = ("header", "signature")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    header: _types_pb2.Header
    signature: _types_pb2_1.Signature
    def __init__(self, header: _Optional[_Union[_types_pb2.Header, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ...) -> None: ...

class HeadResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("header", "short_header", "split_info")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        SHORT_HEADER_FIELD_NUMBER: _ClassVar[int]
        SPLIT_INFO_FIELD_NUMBER: _ClassVar[int]
        header: HeaderWithSignature
        short_header: _types_pb2.ShortHeader
        split_info: _types_pb2.SplitInfo
        def __init__(self, header: _Optional[_Union[HeaderWithSignature, _Mapping]] = ..., short_header: _Optional[_Union[_types_pb2.ShortHeader, _Mapping]] = ..., split_info: _Optional[_Union[_types_pb2.SplitInfo, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: HeadResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[HeadResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_id", "version", "filters")
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FILTERS_FIELD_NUMBER: _ClassVar[int]
        container_id: _types_pb2_1.ContainerID
        version: int
        filters: _containers.RepeatedCompositeFieldContainer[_types_pb2.SearchFilter]
        def __init__(self, container_id: _Optional[_Union[_types_pb2_1.ContainerID, _Mapping]] = ..., version: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[_types_pb2.SearchFilter, _Mapping]]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: SearchRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[SearchRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("id_list",)
        ID_LIST_FIELD_NUMBER: _ClassVar[int]
        id_list: _containers.RepeatedCompositeFieldContainer[_types_pb2_1.ObjectID]
        def __init__(self, id_list: _Optional[_Iterable[_Union[_types_pb2_1.ObjectID, _Mapping]]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: SearchResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[SearchResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class SearchV2Request(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_id", "version", "filters", "cursor", "count", "attributes")
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FILTERS_FIELD_NUMBER: _ClassVar[int]
        CURSOR_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        container_id: _types_pb2_1.ContainerID
        version: int
        filters: _containers.RepeatedCompositeFieldContainer[_types_pb2.SearchFilter]
        cursor: str
        count: int
        attributes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, container_id: _Optional[_Union[_types_pb2_1.ContainerID, _Mapping]] = ..., version: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[_types_pb2.SearchFilter, _Mapping]]] = ..., cursor: _Optional[str] = ..., count: _Optional[int] = ..., attributes: _Optional[_Iterable[str]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: SearchV2Request.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[SearchV2Request.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class SearchV2Response(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class OIDWithMeta(_message.Message):
        __slots__ = ("id", "attributes")
        ID_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        id: _types_pb2_1.ObjectID
        attributes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[_Union[_types_pb2_1.ObjectID, _Mapping]] = ..., attributes: _Optional[_Iterable[str]] = ...) -> None: ...
    class Body(_message.Message):
        __slots__ = ("result", "cursor")
        RESULT_FIELD_NUMBER: _ClassVar[int]
        CURSOR_FIELD_NUMBER: _ClassVar[int]
        result: _containers.RepeatedCompositeFieldContainer[SearchV2Response.OIDWithMeta]
        cursor: str
        def __init__(self, result: _Optional[_Iterable[_Union[SearchV2Response.OIDWithMeta, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: SearchV2Response.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[SearchV2Response.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetRangeRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("address", "range", "raw")
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        RANGE_FIELD_NUMBER: _ClassVar[int]
        RAW_FIELD_NUMBER: _ClassVar[int]
        address: _types_pb2_1.Address
        range: Range
        raw: bool
        def __init__(self, address: _Optional[_Union[_types_pb2_1.Address, _Mapping]] = ..., range: _Optional[_Union[Range, _Mapping]] = ..., raw: bool = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetRangeRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[GetRangeRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class GetRangeResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("chunk", "split_info")
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        SPLIT_INFO_FIELD_NUMBER: _ClassVar[int]
        chunk: bytes
        split_info: _types_pb2.SplitInfo
        def __init__(self, chunk: _Optional[bytes] = ..., split_info: _Optional[_Union[_types_pb2.SplitInfo, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetRangeResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[GetRangeResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class GetRangeHashRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("address", "ranges", "salt", "type")
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        RANGES_FIELD_NUMBER: _ClassVar[int]
        SALT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        address: _types_pb2_1.Address
        ranges: _containers.RepeatedCompositeFieldContainer[Range]
        salt: bytes
        type: _types_pb2_1.ChecksumType
        def __init__(self, address: _Optional[_Union[_types_pb2_1.Address, _Mapping]] = ..., ranges: _Optional[_Iterable[_Union[Range, _Mapping]]] = ..., salt: _Optional[bytes] = ..., type: _Optional[_Union[_types_pb2_1.ChecksumType, str]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetRangeHashRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[GetRangeHashRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class GetRangeHashResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("type", "hash_list")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        HASH_LIST_FIELD_NUMBER: _ClassVar[int]
        type: _types_pb2_1.ChecksumType
        hash_list: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, type: _Optional[_Union[_types_pb2_1.ChecksumType, str]] = ..., hash_list: _Optional[_Iterable[bytes]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetRangeHashResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[GetRangeHashResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class ReplicateRequest(_message.Message):
    __slots__ = ("object", "signature", "sign_object")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGN_OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _types_pb2.Object
    signature: _types_pb2_1.Signature
    sign_object: bool
    def __init__(self, object: _Optional[_Union[_types_pb2.Object, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., sign_object: bool = ...) -> None: ...

class ReplicateResponse(_message.Message):
    __slots__ = ("status", "object_signature")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    status: _types_pb2_1_1_1.Status
    object_signature: bytes
    def __init__(self, status: _Optional[_Union[_types_pb2_1_1_1.Status, _Mapping]] = ..., object_signature: _Optional[bytes] = ...) -> None: ...
