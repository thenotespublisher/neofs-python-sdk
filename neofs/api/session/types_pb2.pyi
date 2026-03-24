from acl import types_pb2 as _types_pb2
from refs import types_pb2 as _types_pb2_1
from status import types_pb2 as _types_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verb(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERB_UNSPECIFIED: _ClassVar[Verb]
    OBJECT_PUT: _ClassVar[Verb]
    OBJECT_GET: _ClassVar[Verb]
    OBJECT_HEAD: _ClassVar[Verb]
    OBJECT_SEARCH: _ClassVar[Verb]
    OBJECT_DELETE: _ClassVar[Verb]
    OBJECT_RANGE: _ClassVar[Verb]
    OBJECT_RANGEHASH: _ClassVar[Verb]
    CONTAINER_PUT: _ClassVar[Verb]
    CONTAINER_DELETE: _ClassVar[Verb]
    CONTAINER_SETEACL: _ClassVar[Verb]
    CONTAINER_SETATTRIBUTE: _ClassVar[Verb]
    CONTAINER_REMOVEATTRIBUTE: _ClassVar[Verb]
VERB_UNSPECIFIED: Verb
OBJECT_PUT: Verb
OBJECT_GET: Verb
OBJECT_HEAD: Verb
OBJECT_SEARCH: Verb
OBJECT_DELETE: Verb
OBJECT_RANGE: Verb
OBJECT_RANGEHASH: Verb
CONTAINER_PUT: Verb
CONTAINER_DELETE: Verb
CONTAINER_SETEACL: Verb
CONTAINER_SETATTRIBUTE: Verb
CONTAINER_REMOVEATTRIBUTE: Verb

class ObjectSessionContext(_message.Message):
    __slots__ = ("verb", "target")
    class Verb(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERB_UNSPECIFIED: _ClassVar[ObjectSessionContext.Verb]
        PUT: _ClassVar[ObjectSessionContext.Verb]
        GET: _ClassVar[ObjectSessionContext.Verb]
        HEAD: _ClassVar[ObjectSessionContext.Verb]
        SEARCH: _ClassVar[ObjectSessionContext.Verb]
        DELETE: _ClassVar[ObjectSessionContext.Verb]
        RANGE: _ClassVar[ObjectSessionContext.Verb]
        RANGEHASH: _ClassVar[ObjectSessionContext.Verb]
    VERB_UNSPECIFIED: ObjectSessionContext.Verb
    PUT: ObjectSessionContext.Verb
    GET: ObjectSessionContext.Verb
    HEAD: ObjectSessionContext.Verb
    SEARCH: ObjectSessionContext.Verb
    DELETE: ObjectSessionContext.Verb
    RANGE: ObjectSessionContext.Verb
    RANGEHASH: ObjectSessionContext.Verb
    class Target(_message.Message):
        __slots__ = ("container", "objects")
        CONTAINER_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_FIELD_NUMBER: _ClassVar[int]
        container: _types_pb2_1.ContainerID
        objects: _containers.RepeatedCompositeFieldContainer[_types_pb2_1.ObjectID]
        def __init__(self, container: _Optional[_Union[_types_pb2_1.ContainerID, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[_types_pb2_1.ObjectID, _Mapping]]] = ...) -> None: ...
    VERB_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    verb: ObjectSessionContext.Verb
    target: ObjectSessionContext.Target
    def __init__(self, verb: _Optional[_Union[ObjectSessionContext.Verb, str]] = ..., target: _Optional[_Union[ObjectSessionContext.Target, _Mapping]] = ...) -> None: ...

class ContainerSessionContext(_message.Message):
    __slots__ = ("verb", "wildcard", "container_id")
    class Verb(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERB_UNSPECIFIED: _ClassVar[ContainerSessionContext.Verb]
        PUT: _ClassVar[ContainerSessionContext.Verb]
        DELETE: _ClassVar[ContainerSessionContext.Verb]
        SETEACL: _ClassVar[ContainerSessionContext.Verb]
        SETATTRIBUTE: _ClassVar[ContainerSessionContext.Verb]
        REMOVEATTRIBUTE: _ClassVar[ContainerSessionContext.Verb]
    VERB_UNSPECIFIED: ContainerSessionContext.Verb
    PUT: ContainerSessionContext.Verb
    DELETE: ContainerSessionContext.Verb
    SETEACL: ContainerSessionContext.Verb
    SETATTRIBUTE: ContainerSessionContext.Verb
    REMOVEATTRIBUTE: ContainerSessionContext.Verb
    VERB_FIELD_NUMBER: _ClassVar[int]
    WILDCARD_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    verb: ContainerSessionContext.Verb
    wildcard: bool
    container_id: _types_pb2_1.ContainerID
    def __init__(self, verb: _Optional[_Union[ContainerSessionContext.Verb, str]] = ..., wildcard: bool = ..., container_id: _Optional[_Union[_types_pb2_1.ContainerID, _Mapping]] = ...) -> None: ...

class SessionToken(_message.Message):
    __slots__ = ("body", "signature")
    class Body(_message.Message):
        __slots__ = ("id", "owner_id", "lifetime", "session_key", "object", "container")
        class TokenLifetime(_message.Message):
            __slots__ = ("exp", "nbf", "iat")
            EXP_FIELD_NUMBER: _ClassVar[int]
            NBF_FIELD_NUMBER: _ClassVar[int]
            IAT_FIELD_NUMBER: _ClassVar[int]
            exp: int
            nbf: int
            iat: int
            def __init__(self, exp: _Optional[int] = ..., nbf: _Optional[int] = ..., iat: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        LIFETIME_FIELD_NUMBER: _ClassVar[int]
        SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_FIELD_NUMBER: _ClassVar[int]
        id: bytes
        owner_id: _types_pb2_1.OwnerID
        lifetime: SessionToken.Body.TokenLifetime
        session_key: bytes
        object: ObjectSessionContext
        container: ContainerSessionContext
        def __init__(self, id: _Optional[bytes] = ..., owner_id: _Optional[_Union[_types_pb2_1.OwnerID, _Mapping]] = ..., lifetime: _Optional[_Union[SessionToken.Body.TokenLifetime, _Mapping]] = ..., session_key: _Optional[bytes] = ..., object: _Optional[_Union[ObjectSessionContext, _Mapping]] = ..., container: _Optional[_Union[ContainerSessionContext, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    body: SessionToken.Body
    signature: _types_pb2_1.Signature
    def __init__(self, body: _Optional[_Union[SessionToken.Body, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ...) -> None: ...

class XHeader(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class RequestMetaHeader(_message.Message):
    __slots__ = ("version", "epoch", "ttl", "x_headers", "session_token", "session_token_v2", "bearer_token", "origin", "magic_number")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    X_HEADERS_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_V2_FIELD_NUMBER: _ClassVar[int]
    BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MAGIC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2_1.Version
    epoch: int
    ttl: int
    x_headers: _containers.RepeatedCompositeFieldContainer[XHeader]
    session_token: SessionToken
    session_token_v2: SessionTokenV2
    bearer_token: _types_pb2.BearerToken
    origin: RequestMetaHeader
    magic_number: int
    def __init__(self, version: _Optional[_Union[_types_pb2_1.Version, _Mapping]] = ..., epoch: _Optional[int] = ..., ttl: _Optional[int] = ..., x_headers: _Optional[_Iterable[_Union[XHeader, _Mapping]]] = ..., session_token: _Optional[_Union[SessionToken, _Mapping]] = ..., session_token_v2: _Optional[_Union[SessionTokenV2, _Mapping]] = ..., bearer_token: _Optional[_Union[_types_pb2.BearerToken, _Mapping]] = ..., origin: _Optional[_Union[RequestMetaHeader, _Mapping]] = ..., magic_number: _Optional[int] = ...) -> None: ...

class ResponseMetaHeader(_message.Message):
    __slots__ = ("version", "epoch", "ttl", "x_headers", "origin", "status")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    X_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    version: _types_pb2_1.Version
    epoch: int
    ttl: int
    x_headers: _containers.RepeatedCompositeFieldContainer[XHeader]
    origin: ResponseMetaHeader
    status: _types_pb2_1_1.Status
    def __init__(self, version: _Optional[_Union[_types_pb2_1.Version, _Mapping]] = ..., epoch: _Optional[int] = ..., ttl: _Optional[int] = ..., x_headers: _Optional[_Iterable[_Union[XHeader, _Mapping]]] = ..., origin: _Optional[_Union[ResponseMetaHeader, _Mapping]] = ..., status: _Optional[_Union[_types_pb2_1_1.Status, _Mapping]] = ...) -> None: ...

class RequestVerificationHeader(_message.Message):
    __slots__ = ("body_signature", "meta_signature", "origin_signature", "origin")
    BODY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    META_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    body_signature: _types_pb2_1.Signature
    meta_signature: _types_pb2_1.Signature
    origin_signature: _types_pb2_1.Signature
    origin: RequestVerificationHeader
    def __init__(self, body_signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., meta_signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., origin_signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., origin: _Optional[_Union[RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class ResponseVerificationHeader(_message.Message):
    __slots__ = ("body_signature", "meta_signature", "origin_signature", "origin")
    BODY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    META_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    body_signature: _types_pb2_1.Signature
    meta_signature: _types_pb2_1.Signature
    origin_signature: _types_pb2_1.Signature
    origin: ResponseVerificationHeader
    def __init__(self, body_signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., meta_signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., origin_signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., origin: _Optional[_Union[ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ("owner_id", "nns_name")
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    NNS_NAME_FIELD_NUMBER: _ClassVar[int]
    owner_id: _types_pb2_1.OwnerID
    nns_name: str
    def __init__(self, owner_id: _Optional[_Union[_types_pb2_1.OwnerID, _Mapping]] = ..., nns_name: _Optional[str] = ...) -> None: ...

class TokenLifetime(_message.Message):
    __slots__ = ("exp", "nbf", "iat")
    EXP_FIELD_NUMBER: _ClassVar[int]
    NBF_FIELD_NUMBER: _ClassVar[int]
    IAT_FIELD_NUMBER: _ClassVar[int]
    exp: int
    nbf: int
    iat: int
    def __init__(self, exp: _Optional[int] = ..., nbf: _Optional[int] = ..., iat: _Optional[int] = ...) -> None: ...

class SessionContextV2(_message.Message):
    __slots__ = ("container", "verbs")
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    VERBS_FIELD_NUMBER: _ClassVar[int]
    container: _types_pb2_1.ContainerID
    verbs: _containers.RepeatedScalarFieldContainer[Verb]
    def __init__(self, container: _Optional[_Union[_types_pb2_1.ContainerID, _Mapping]] = ..., verbs: _Optional[_Iterable[_Union[Verb, str]]] = ...) -> None: ...

class SessionTokenV2(_message.Message):
    __slots__ = ("body", "signature", "origin")
    class Body(_message.Message):
        __slots__ = ("version", "appdata", "issuer", "subjects", "lifetime", "contexts", "final")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        APPDATA_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        SUBJECTS_FIELD_NUMBER: _ClassVar[int]
        LIFETIME_FIELD_NUMBER: _ClassVar[int]
        CONTEXTS_FIELD_NUMBER: _ClassVar[int]
        FINAL_FIELD_NUMBER: _ClassVar[int]
        version: int
        appdata: bytes
        issuer: _types_pb2_1.OwnerID
        subjects: _containers.RepeatedCompositeFieldContainer[Target]
        lifetime: TokenLifetime
        contexts: _containers.RepeatedCompositeFieldContainer[SessionContextV2]
        final: bool
        def __init__(self, version: _Optional[int] = ..., appdata: _Optional[bytes] = ..., issuer: _Optional[_Union[_types_pb2_1.OwnerID, _Mapping]] = ..., subjects: _Optional[_Iterable[_Union[Target, _Mapping]]] = ..., lifetime: _Optional[_Union[TokenLifetime, _Mapping]] = ..., contexts: _Optional[_Iterable[_Union[SessionContextV2, _Mapping]]] = ..., final: bool = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    body: SessionTokenV2.Body
    signature: _types_pb2_1.Signature
    origin: SessionTokenV2
    def __init__(self, body: _Optional[_Union[SessionTokenV2.Body, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1.Signature, _Mapping]] = ..., origin: _Optional[_Union[SessionTokenV2, _Mapping]] = ...) -> None: ...
