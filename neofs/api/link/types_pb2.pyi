from refs import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Link(_message.Message):
    __slots__ = ("children",)
    class MeasuredObject(_message.Message):
        __slots__ = ("id", "size")
        ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        id: _types_pb2.ObjectID
        size: int
        def __init__(self, id: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ..., size: _Optional[int] = ...) -> None: ...
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[Link.MeasuredObject]
    def __init__(self, children: _Optional[_Iterable[_Union[Link.MeasuredObject, _Mapping]]] = ...) -> None: ...
