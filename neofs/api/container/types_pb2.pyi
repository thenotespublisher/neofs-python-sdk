from netmap import types_pb2 as _types_pb2
from refs import types_pb2 as _types_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Container(_message.Message):
    __slots__ = ("version", "owner_id", "nonce", "basic_acl", "attributes", "placement_policy")
    class Attribute(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    BASIC_ACL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_POLICY_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2_1.Version
    owner_id: _types_pb2_1.OwnerID
    nonce: bytes
    basic_acl: int
    attributes: _containers.RepeatedCompositeFieldContainer[Container.Attribute]
    placement_policy: _types_pb2.PlacementPolicy
    def __init__(self, version: _Optional[_Union[_types_pb2_1.Version, _Mapping]] = ..., owner_id: _Optional[_Union[_types_pb2_1.OwnerID, _Mapping]] = ..., nonce: _Optional[bytes] = ..., basic_acl: _Optional[int] = ..., attributes: _Optional[_Iterable[_Union[Container.Attribute, _Mapping]]] = ..., placement_policy: _Optional[_Union[_types_pb2.PlacementPolicy, _Mapping]] = ...) -> None: ...
