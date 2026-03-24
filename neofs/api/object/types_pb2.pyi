from refs import types_pb2 as _types_pb2
from session import types_pb2 as _types_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGULAR: _ClassVar[ObjectType]
    TOMBSTONE: _ClassVar[ObjectType]
    STORAGE_GROUP: _ClassVar[ObjectType]
    LOCK: _ClassVar[ObjectType]
    LINK: _ClassVar[ObjectType]

class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATCH_TYPE_UNSPECIFIED: _ClassVar[MatchType]
    STRING_EQUAL: _ClassVar[MatchType]
    STRING_NOT_EQUAL: _ClassVar[MatchType]
    NOT_PRESENT: _ClassVar[MatchType]
    COMMON_PREFIX: _ClassVar[MatchType]
    NUM_GT: _ClassVar[MatchType]
    NUM_GE: _ClassVar[MatchType]
    NUM_LT: _ClassVar[MatchType]
    NUM_LE: _ClassVar[MatchType]
REGULAR: ObjectType
TOMBSTONE: ObjectType
STORAGE_GROUP: ObjectType
LOCK: ObjectType
LINK: ObjectType
MATCH_TYPE_UNSPECIFIED: MatchType
STRING_EQUAL: MatchType
STRING_NOT_EQUAL: MatchType
NOT_PRESENT: MatchType
COMMON_PREFIX: MatchType
NUM_GT: MatchType
NUM_GE: MatchType
NUM_LT: MatchType
NUM_LE: MatchType

class SearchFilter(_message.Message):
    __slots__ = ("match_type", "key", "value")
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    match_type: MatchType
    key: str
    value: str
    def __init__(self, match_type: _Optional[_Union[MatchType, str]] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ShortHeader(_message.Message):
    __slots__ = ("version", "creation_epoch", "owner_id", "object_type", "payload_length", "payload_hash", "homomorphic_hash")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATION_EPOCH_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_HASH_FIELD_NUMBER: _ClassVar[int]
    HOMOMORPHIC_HASH_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2.Version
    creation_epoch: int
    owner_id: _types_pb2.OwnerID
    object_type: ObjectType
    payload_length: int
    payload_hash: _types_pb2.Checksum
    homomorphic_hash: _types_pb2.Checksum
    def __init__(self, version: _Optional[_Union[_types_pb2.Version, _Mapping]] = ..., creation_epoch: _Optional[int] = ..., owner_id: _Optional[_Union[_types_pb2.OwnerID, _Mapping]] = ..., object_type: _Optional[_Union[ObjectType, str]] = ..., payload_length: _Optional[int] = ..., payload_hash: _Optional[_Union[_types_pb2.Checksum, _Mapping]] = ..., homomorphic_hash: _Optional[_Union[_types_pb2.Checksum, _Mapping]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ("version", "container_id", "owner_id", "creation_epoch", "payload_length", "payload_hash", "object_type", "homomorphic_hash", "session_token", "attributes", "split", "session_token_v2")
    class Attribute(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Split(_message.Message):
        __slots__ = ("parent", "previous", "parent_signature", "parent_header", "children", "split_id", "first")
        PARENT_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        PARENT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        PARENT_HEADER_FIELD_NUMBER: _ClassVar[int]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_FIELD_NUMBER: _ClassVar[int]
        parent: _types_pb2.ObjectID
        previous: _types_pb2.ObjectID
        parent_signature: _types_pb2.Signature
        parent_header: Header
        children: _containers.RepeatedCompositeFieldContainer[_types_pb2.ObjectID]
        split_id: bytes
        first: _types_pb2.ObjectID
        def __init__(self, parent: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ..., previous: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ..., parent_signature: _Optional[_Union[_types_pb2.Signature, _Mapping]] = ..., parent_header: _Optional[_Union[Header, _Mapping]] = ..., children: _Optional[_Iterable[_Union[_types_pb2.ObjectID, _Mapping]]] = ..., split_id: _Optional[bytes] = ..., first: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_EPOCH_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_HASH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOMOMORPHIC_HASH_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_V2_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2.Version
    container_id: _types_pb2.ContainerID
    owner_id: _types_pb2.OwnerID
    creation_epoch: int
    payload_length: int
    payload_hash: _types_pb2.Checksum
    object_type: ObjectType
    homomorphic_hash: _types_pb2.Checksum
    session_token: _types_pb2_1.SessionToken
    attributes: _containers.RepeatedCompositeFieldContainer[Header.Attribute]
    split: Header.Split
    session_token_v2: _types_pb2_1.SessionTokenV2
    def __init__(self, version: _Optional[_Union[_types_pb2.Version, _Mapping]] = ..., container_id: _Optional[_Union[_types_pb2.ContainerID, _Mapping]] = ..., owner_id: _Optional[_Union[_types_pb2.OwnerID, _Mapping]] = ..., creation_epoch: _Optional[int] = ..., payload_length: _Optional[int] = ..., payload_hash: _Optional[_Union[_types_pb2.Checksum, _Mapping]] = ..., object_type: _Optional[_Union[ObjectType, str]] = ..., homomorphic_hash: _Optional[_Union[_types_pb2.Checksum, _Mapping]] = ..., session_token: _Optional[_Union[_types_pb2_1.SessionToken, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[Header.Attribute, _Mapping]]] = ..., split: _Optional[_Union[Header.Split, _Mapping]] = ..., session_token_v2: _Optional[_Union[_types_pb2_1.SessionTokenV2, _Mapping]] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ("object_id", "signature", "header", "payload")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    object_id: _types_pb2.ObjectID
    signature: _types_pb2.Signature
    header: Header
    payload: bytes
    def __init__(self, object_id: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2.Signature, _Mapping]] = ..., header: _Optional[_Union[Header, _Mapping]] = ..., payload: _Optional[bytes] = ...) -> None: ...

class SplitInfo(_message.Message):
    __slots__ = ("split_id", "last_part", "link", "first_part")
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PART_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    FIRST_PART_FIELD_NUMBER: _ClassVar[int]
    split_id: bytes
    last_part: _types_pb2.ObjectID
    link: _types_pb2.ObjectID
    first_part: _types_pb2.ObjectID
    def __init__(self, split_id: _Optional[bytes] = ..., last_part: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ..., link: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ..., first_part: _Optional[_Union[_types_pb2.ObjectID, _Mapping]] = ...) -> None: ...
