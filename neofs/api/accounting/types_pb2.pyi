from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Decimal(_message.Message):
    __slots__ = ("value", "precision")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    value: int
    precision: int
    def __init__(self, value: _Optional[int] = ..., precision: _Optional[int] = ...) -> None: ...
