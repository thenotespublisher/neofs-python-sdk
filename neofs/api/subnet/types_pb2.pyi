from refs import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubnetInfo(_message.Message):
    __slots__ = ("id", "owner")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    id: _types_pb2.SubnetID
    owner: _types_pb2.OwnerID
    def __init__(self, id: _Optional[_Union[_types_pb2.SubnetID, _Mapping]] = ..., owner: _Optional[_Union[_types_pb2.OwnerID, _Mapping]] = ...) -> None: ...
