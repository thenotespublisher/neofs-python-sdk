from refs import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tombstone(_message.Message):
    __slots__ = ("expiration_epoch", "split_id", "members")
    EXPIRATION_EPOCH_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    expiration_epoch: int
    split_id: bytes
    members: _containers.RepeatedCompositeFieldContainer[_types_pb2.ObjectID]
    def __init__(self, expiration_epoch: _Optional[int] = ..., split_id: _Optional[bytes] = ..., members: _Optional[_Iterable[_Union[_types_pb2.ObjectID, _Mapping]]] = ...) -> None: ...
