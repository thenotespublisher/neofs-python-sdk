from refs import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageGroup(_message.Message):
    __slots__ = ("validation_data_size", "validation_hash", "expiration_epoch", "members")
    VALIDATION_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_HASH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_EPOCH_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    validation_data_size: int
    validation_hash: _types_pb2.Checksum
    expiration_epoch: int
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.ObjectID]
    def __init__(self, validation_data_size: _Optional[int] = ..., validation_hash: _Optional[_Union[_types_pb2.Checksum, _Mapping]] = ..., expiration_epoch: _Optional[int] = ..., members: _Optional[_Iterable[_Union[_types_pb2.ObjectID, _Mapping]]] = ...) -> None: ...
