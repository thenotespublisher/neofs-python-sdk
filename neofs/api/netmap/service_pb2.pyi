from netmap import types_pb2 as _types_pb2
from refs import types_pb2 as _types_pb2_1
from session import types_pb2 as _types_pb2_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalNodeInfoRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: LocalNodeInfoRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[LocalNodeInfoRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class LocalNodeInfoResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("version", "node_info")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NODE_INFO_FIELD_NUMBER: _ClassVar[int]
        version: _types_pb2_1.Version
        node_info: _types_pb2.NodeInfo
        def __init__(self, version: _Optional[_Union[_types_pb2_1.Version, _Mapping]] = ..., node_info: _Optional[_Union[_types_pb2.NodeInfo, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: LocalNodeInfoResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[LocalNodeInfoResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class NetworkInfoRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: NetworkInfoRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[NetworkInfoRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class NetworkInfoResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("network_info",)
        NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
        network_info: _types_pb2.NetworkInfo
        def __init__(self, network_info: _Optional[_Union[_types_pb2.NetworkInfo, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: NetworkInfoResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[NetworkInfoResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class NetmapSnapshotRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: NetmapSnapshotRequest.Body
    meta_header: _types_pb2_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[NetmapSnapshotRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class NetmapSnapshotResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("netmap",)
        NETMAP_FIELD_NUMBER: _ClassVar[int]
        netmap: _types_pb2.Netmap
        def __init__(self, netmap: _Optional[_Union[_types_pb2.Netmap, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: NetmapSnapshotResponse.Body
    meta_header: _types_pb2_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[NetmapSnapshotResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...
