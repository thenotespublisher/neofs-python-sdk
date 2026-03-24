from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Section(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECTION_SUCCESS: _ClassVar[Section]
    SECTION_FAILURE_COMMON: _ClassVar[Section]
    SECTION_OBJECT: _ClassVar[Section]
    SECTION_CONTAINER: _ClassVar[Section]
    SECTION_SESSION: _ClassVar[Section]

class Success(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[Success]
    INCOMPLETE: _ClassVar[Success]

class CommonFail(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERNAL: _ClassVar[CommonFail]
    WRONG_MAGIC_NUMBER: _ClassVar[CommonFail]
    SIGNATURE_VERIFICATION_FAIL: _ClassVar[CommonFail]
    NODE_UNDER_MAINTENANCE: _ClassVar[CommonFail]
    BAD_REQUEST: _ClassVar[CommonFail]
    BUSY: _ClassVar[CommonFail]

class Object(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_DENIED: _ClassVar[Object]
    OBJECT_NOT_FOUND: _ClassVar[Object]
    LOCKED: _ClassVar[Object]
    LOCK_NON_REGULAR_OBJECT: _ClassVar[Object]
    OBJECT_ALREADY_REMOVED: _ClassVar[Object]
    OUT_OF_RANGE: _ClassVar[Object]
    QUOTA_EXCEEDED: _ClassVar[Object]

class Container(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTAINER_NOT_FOUND: _ClassVar[Container]
    EACL_NOT_FOUND: _ClassVar[Container]
    CONTAINER_LOCKED: _ClassVar[Container]
    CONTAINER_AWAIT_TIMEOUT: _ClassVar[Container]

class Session(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKEN_NOT_FOUND: _ClassVar[Session]
    TOKEN_EXPIRED: _ClassVar[Session]
SECTION_SUCCESS: Section
SECTION_FAILURE_COMMON: Section
SECTION_OBJECT: Section
SECTION_CONTAINER: Section
SECTION_SESSION: Section
OK: Success
INCOMPLETE: Success
INTERNAL: CommonFail
WRONG_MAGIC_NUMBER: CommonFail
SIGNATURE_VERIFICATION_FAIL: CommonFail
NODE_UNDER_MAINTENANCE: CommonFail
BAD_REQUEST: CommonFail
BUSY: CommonFail
ACCESS_DENIED: Object
OBJECT_NOT_FOUND: Object
LOCKED: Object
LOCK_NON_REGULAR_OBJECT: Object
OBJECT_ALREADY_REMOVED: Object
OUT_OF_RANGE: Object
QUOTA_EXCEEDED: Object
CONTAINER_NOT_FOUND: Container
EACL_NOT_FOUND: Container
CONTAINER_LOCKED: Container
CONTAINER_AWAIT_TIMEOUT: Container
TOKEN_NOT_FOUND: Session
TOKEN_EXPIRED: Session

class Status(_message.Message):
    __slots__ = ("code", "message", "details")
    class Detail(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: int
        value: bytes
        def __init__(self, id: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    details: _containers.RepeatedCompositeFieldContainer[Status.Detail]
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., details: _Optional[_Iterable[_Union[Status.Detail, _Mapping]]] = ...) -> None: ...
