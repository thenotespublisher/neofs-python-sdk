from refs import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    USER: _ClassVar[Role]
    SYSTEM: _ClassVar[Role]
    OTHERS: _ClassVar[Role]

class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATCH_TYPE_UNSPECIFIED: _ClassVar[MatchType]
    STRING_EQUAL: _ClassVar[MatchType]
    STRING_NOT_EQUAL: _ClassVar[MatchType]
    NOT_PRESENT: _ClassVar[MatchType]
    NUM_GT: _ClassVar[MatchType]
    NUM_GE: _ClassVar[MatchType]
    NUM_LT: _ClassVar[MatchType]
    NUM_LE: _ClassVar[MatchType]

class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_UNSPECIFIED: _ClassVar[Operation]
    GET: _ClassVar[Operation]
    HEAD: _ClassVar[Operation]
    PUT: _ClassVar[Operation]
    DELETE: _ClassVar[Operation]
    SEARCH: _ClassVar[Operation]
    GETRANGE: _ClassVar[Operation]
    GETRANGEHASH: _ClassVar[Operation]

class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_UNSPECIFIED: _ClassVar[Action]
    ALLOW: _ClassVar[Action]
    DENY: _ClassVar[Action]

class HeaderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEADER_UNSPECIFIED: _ClassVar[HeaderType]
    REQUEST: _ClassVar[HeaderType]
    OBJECT: _ClassVar[HeaderType]
    SERVICE: _ClassVar[HeaderType]
ROLE_UNSPECIFIED: Role
USER: Role
SYSTEM: Role
OTHERS: Role
MATCH_TYPE_UNSPECIFIED: MatchType
STRING_EQUAL: MatchType
STRING_NOT_EQUAL: MatchType
NOT_PRESENT: MatchType
NUM_GT: MatchType
NUM_GE: MatchType
NUM_LT: MatchType
NUM_LE: MatchType
OPERATION_UNSPECIFIED: Operation
GET: Operation
HEAD: Operation
PUT: Operation
DELETE: Operation
SEARCH: Operation
GETRANGE: Operation
GETRANGEHASH: Operation
ACTION_UNSPECIFIED: Action
ALLOW: Action
DENY: Action
HEADER_UNSPECIFIED: HeaderType
REQUEST: HeaderType
OBJECT: HeaderType
SERVICE: HeaderType

class EACLRecord(_message.Message):
    __slots__ = ("operation", "action", "filters", "targets")
    class Filter(_message.Message):
        __slots__ = ("header_type", "match_type", "key", "value")
        HEADER_TYPE_FIELD_NUMBER: _ClassVar[int]
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        header_type: HeaderType
        match_type: MatchType
        key: str
        value: str
        def __init__(self, header_type: _Optional[_Union[HeaderType, str]] = ..., match_type: _Optional[_Union[MatchType, str]] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Target(_message.Message):
        __slots__ = ("role", "keys")
        ROLE_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        role: Role
        keys: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, role: _Optional[_Union[Role, str]] = ..., keys: _Optional[_Iterable[bytes]] = ...) -> None: ...
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    operation: Operation
    action: Action
    filters: _containers.RepeatedCompositeFieldContainer[EACLRecord.Filter]
    targets: _containers.RepeatedCompositeFieldContainer[EACLRecord.Target]
    def __init__(self, operation: _Optional[_Union[Operation, str]] = ..., action: _Optional[_Union[Action, str]] = ..., filters: _Optional[_Iterable[_Union[EACLRecord.Filter, _Mapping]]] = ..., targets: _Optional[_Iterable[_Union[EACLRecord.Target, _Mapping]]] = ...) -> None: ...

class EACLTable(_message.Message):
    __slots__ = ("version", "container_id", "records")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2.Version
    container_id: _types_pb2.ContainerID
    records: _containers.RepeatedCompositeFieldContainer[EACLRecord]
    def __init__(self, version: _Optional[_Union[_types_pb2.Version, _Mapping]] = ..., container_id: _Optional[_Union[_types_pb2.ContainerID, _Mapping]] = ..., records: _Optional[_Iterable[_Union[EACLRecord, _Mapping]]] = ...) -> None: ...

class BearerToken(_message.Message):
    __slots__ = ("body", "signature")
    class Body(_message.Message):
        __slots__ = ("eacl_table", "owner_id", "lifetime", "issuer")
        class TokenLifetime(_message.Message):
            __slots__ = ("exp", "nbf", "iat")
            EXP_FIELD_NUMBER: _ClassVar[int]
            NBF_FIELD_NUMBER: _ClassVar[int]
            IAT_FIELD_NUMBER: _ClassVar[int]
            exp: int
            nbf: int
            iat: int
            def __init__(self, exp: _Optional[int] = ..., nbf: _Optional[int] = ..., iat: _Optional[int] = ...) -> None: ...
        EACL_TABLE_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        LIFETIME_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        eacl_table: EACLTable
        owner_id: _types_pb2.OwnerID
        lifetime: BearerToken.Body.TokenLifetime
        issuer: _types_pb2.OwnerID
        def __init__(self, eacl_table: _Optional[_Union[EACLTable, _Mapping]] = ..., owner_id: _Optional[_Union[_types_pb2.OwnerID, _Mapping]] = ..., lifetime: _Optional[_Union[BearerToken.Body.TokenLifetime, _Mapping]] = ..., issuer: _Optional[_Union[_types_pb2.OwnerID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    body: BearerToken.Body
    signature: _types_pb2.Signature
    def __init__(self, body: _Optional[_Union[BearerToken.Body, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2.Signature, _Mapping]] = ...) -> None: ...
