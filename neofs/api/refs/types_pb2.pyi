from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignatureScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECDSA_SHA512: _ClassVar[SignatureScheme]
    ECDSA_RFC6979_SHA256: _ClassVar[SignatureScheme]
    ECDSA_RFC6979_SHA256_WALLET_CONNECT: _ClassVar[SignatureScheme]
    N3: _ClassVar[SignatureScheme]

class ChecksumType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECKSUM_TYPE_UNSPECIFIED: _ClassVar[ChecksumType]
    TZ: _ClassVar[ChecksumType]
    SHA256: _ClassVar[ChecksumType]
ECDSA_SHA512: SignatureScheme
ECDSA_RFC6979_SHA256: SignatureScheme
ECDSA_RFC6979_SHA256_WALLET_CONNECT: SignatureScheme
N3: SignatureScheme
CHECKSUM_TYPE_UNSPECIFIED: ChecksumType
TZ: ChecksumType
SHA256: ChecksumType

class Address(_message.Message):
    __slots__ = ("container_id", "object_id")
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    container_id: ContainerID
    object_id: ObjectID
    def __init__(self, container_id: _Optional[_Union[ContainerID, _Mapping]] = ..., object_id: _Optional[_Union[ObjectID, _Mapping]] = ...) -> None: ...

class ObjectID(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class ContainerID(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class OwnerID(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class SubnetID(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ("major", "minor")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("key", "sign", "scheme")
    KEY_FIELD_NUMBER: _ClassVar[int]
    SIGN_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    sign: bytes
    scheme: SignatureScheme
    def __init__(self, key: _Optional[bytes] = ..., sign: _Optional[bytes] = ..., scheme: _Optional[_Union[SignatureScheme, str]] = ...) -> None: ...

class SignatureRFC6979(_message.Message):
    __slots__ = ("key", "sign")
    KEY_FIELD_NUMBER: _ClassVar[int]
    SIGN_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    sign: bytes
    def __init__(self, key: _Optional[bytes] = ..., sign: _Optional[bytes] = ...) -> None: ...

class Checksum(_message.Message):
    __slots__ = ("type", "sum")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    type: ChecksumType
    sum: bytes
    def __init__(self, type: _Optional[_Union[ChecksumType, str]] = ..., sum: _Optional[bytes] = ...) -> None: ...
