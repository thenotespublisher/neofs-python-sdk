from refs import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataAuditResult(_message.Message):
    __slots__ = ("version", "audit_epoch", "container_id", "public_key", "complete", "requests", "retries", "pass_sg", "fail_sg", "hit", "miss", "fail", "pass_nodes", "fail_nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    AUDIT_EPOCH_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    PASS_SG_FIELD_NUMBER: _ClassVar[int]
    FAIL_SG_FIELD_NUMBER: _ClassVar[int]
    HIT_FIELD_NUMBER: _ClassVar[int]
    MISS_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    PASS_NODES_FIELD_NUMBER: _ClassVar[int]
    FAIL_NODES_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2.Version
    audit_epoch: int
    container_id: _types_pb2.ContainerID
    public_key: bytes
    complete: bool
    requests: int
    retries: int
    pass_sg: _containers.RepeatedCompositeFieldContainer[_types_pb2.ObjectID]
    fail_sg: _containers.RepeatedCompositeFieldContainer[_types_pb2.ObjectID]
    hit: int
    miss: int
    fail: int
    pass_nodes: _containers.RepeatedScalarFieldContainer[bytes]
    fail_nodes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, version: _Optional[_Union[_types_pb2.Version, _Mapping]] = ..., audit_epoch: _Optional[int] = ..., container_id: _Optional[_Union[_types_pb2.ContainerID, _Mapping]] = ..., public_key: _Optional[bytes] = ..., complete: bool = ..., requests: _Optional[int] = ..., retries: _Optional[int] = ..., pass_sg: _Optional[_Iterable[_Union[_types_pb2.ObjectID, _Mapping]]] = ..., fail_sg: _Optional[_Iterable[_Union[_types_pb2.ObjectID, _Mapping]]] = ..., hit: _Optional[int] = ..., miss: _Optional[int] = ..., fail: _Optional[int] = ..., pass_nodes: _Optional[_Iterable[bytes]] = ..., fail_nodes: _Optional[_Iterable[bytes]] = ...) -> None: ...
