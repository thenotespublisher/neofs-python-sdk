from refs import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeerID(_message.Message):
    __slots__ = ("public_key",)
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    def __init__(self, public_key: _Optional[bytes] = ...) -> None: ...

class Trust(_message.Message):
    __slots__ = ("peer", "value")
    PEER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    peer: PeerID
    value: float
    def __init__(self, peer: _Optional[_Union[PeerID, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class PeerToPeerTrust(_message.Message):
    __slots__ = ("trusting_peer", "trust")
    TRUSTING_PEER_FIELD_NUMBER: _ClassVar[int]
    TRUST_FIELD_NUMBER: _ClassVar[int]
    trusting_peer: PeerID
    trust: Trust
    def __init__(self, trusting_peer: _Optional[_Union[PeerID, _Mapping]] = ..., trust: _Optional[_Union[Trust, _Mapping]] = ...) -> None: ...

class GlobalTrust(_message.Message):
    __slots__ = ("version", "body", "signature")
    class Body(_message.Message):
        __slots__ = ("manager", "trust")
        MANAGER_FIELD_NUMBER: _ClassVar[int]
        TRUST_FIELD_NUMBER: _ClassVar[int]
        manager: PeerID
        trust: Trust
        def __init__(self, manager: _Optional[_Union[PeerID, _Mapping]] = ..., trust: _Optional[_Union[Trust, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2.Version
    body: GlobalTrust.Body
    signature: _types_pb2.Signature
    def __init__(self, version: _Optional[_Union[_types_pb2.Version, _Mapping]] = ..., body: _Optional[_Union[GlobalTrust.Body, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2.Signature, _Mapping]] = ...) -> None: ...
