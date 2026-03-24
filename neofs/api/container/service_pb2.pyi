from acl import types_pb2 as _types_pb2
from container import types_pb2 as _types_pb2_1
from refs import types_pb2 as _types_pb2_1_1
from session import types_pb2 as _types_pb2_1_1_1
from status import types_pb2 as _types_pb2_1_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PutRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container", "signature")
        CONTAINER_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        container: _types_pb2_1.Container
        signature: _types_pb2_1_1.SignatureRFC6979
        def __init__(self, container: _Optional[_Union[_types_pb2_1.Container, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: PutRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[PutRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class PutResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_id",)
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        container_id: _types_pb2_1_1.ContainerID
        def __init__(self, container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: PutResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[PutResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_id", "signature")
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        container_id: _types_pb2_1_1.ContainerID
        signature: _types_pb2_1_1.SignatureRFC6979
        def __init__(self, container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: DeleteRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[DeleteRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: DeleteResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[DeleteResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_id",)
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        container_id: _types_pb2_1_1.ContainerID
        def __init__(self, container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[GetRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container", "signature", "session_token")
        CONTAINER_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        container: _types_pb2_1.Container
        signature: _types_pb2_1_1.SignatureRFC6979
        session_token: _types_pb2_1_1_1.SessionToken
        def __init__(self, container: _Optional[_Union[_types_pb2_1.Container, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ..., session_token: _Optional[_Union[_types_pb2_1_1_1.SessionToken, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[GetResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("owner_id",)
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        owner_id: _types_pb2_1_1.OwnerID
        def __init__(self, owner_id: _Optional[_Union[_types_pb2_1_1.OwnerID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: ListRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[ListRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_ids",)
        CONTAINER_IDS_FIELD_NUMBER: _ClassVar[int]
        container_ids: _containers.RepeatedCompositeFieldContainer[_types_pb2_1_1.ContainerID]
        def __init__(self, container_ids: _Optional[_Iterable[_Union[_types_pb2_1_1.ContainerID, _Mapping]]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: ListResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[ListResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class SetExtendedACLRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("eacl", "signature")
        EACL_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        eacl: _types_pb2.EACLTable
        signature: _types_pb2_1_1.SignatureRFC6979
        def __init__(self, eacl: _Optional[_Union[_types_pb2.EACLTable, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: SetExtendedACLRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[SetExtendedACLRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class SetExtendedACLResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: SetExtendedACLResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[SetExtendedACLResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class GetExtendedACLRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("container_id",)
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        container_id: _types_pb2_1_1.ContainerID
        def __init__(self, container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetExtendedACLRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[GetExtendedACLRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class GetExtendedACLResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("eacl", "signature", "session_token")
        EACL_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        eacl: _types_pb2.EACLTable
        signature: _types_pb2_1_1.SignatureRFC6979
        session_token: _types_pb2_1_1_1.SessionToken
        def __init__(self, eacl: _Optional[_Union[_types_pb2.EACLTable, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ..., session_token: _Optional[_Union[_types_pb2_1_1_1.SessionToken, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: GetExtendedACLResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[GetExtendedACLResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class AnnounceUsedSpaceRequest(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ("announcements",)
        class Announcement(_message.Message):
            __slots__ = ("epoch", "container_id", "used_space")
            EPOCH_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
            USED_SPACE_FIELD_NUMBER: _ClassVar[int]
            epoch: int
            container_id: _types_pb2_1_1.ContainerID
            used_space: int
            def __init__(self, epoch: _Optional[int] = ..., container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ..., used_space: _Optional[int] = ...) -> None: ...
        ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
        announcements: _containers.RepeatedCompositeFieldContainer[AnnounceUsedSpaceRequest.Body.Announcement]
        def __init__(self, announcements: _Optional[_Iterable[_Union[AnnounceUsedSpaceRequest.Body.Announcement, _Mapping]]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: AnnounceUsedSpaceRequest.Body
    meta_header: _types_pb2_1_1_1.RequestMetaHeader
    verify_header: _types_pb2_1_1_1.RequestVerificationHeader
    def __init__(self, body: _Optional[_Union[AnnounceUsedSpaceRequest.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.RequestMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.RequestVerificationHeader, _Mapping]] = ...) -> None: ...

class AnnounceUsedSpaceResponse(_message.Message):
    __slots__ = ("body", "meta_header", "verify_header")
    class Body(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_HEADER_FIELD_NUMBER: _ClassVar[int]
    body: AnnounceUsedSpaceResponse.Body
    meta_header: _types_pb2_1_1_1.ResponseMetaHeader
    verify_header: _types_pb2_1_1_1.ResponseVerificationHeader
    def __init__(self, body: _Optional[_Union[AnnounceUsedSpaceResponse.Body, _Mapping]] = ..., meta_header: _Optional[_Union[_types_pb2_1_1_1.ResponseMetaHeader, _Mapping]] = ..., verify_header: _Optional[_Union[_types_pb2_1_1_1.ResponseVerificationHeader, _Mapping]] = ...) -> None: ...

class SetAttributeRequest(_message.Message):
    __slots__ = ("body", "body_signature")
    class Body(_message.Message):
        __slots__ = ("parameters", "signature", "session_token", "session_token_v1")
        class Parameters(_message.Message):
            __slots__ = ("container_id", "attribute", "value", "valid_until")
            CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
            container_id: _types_pb2_1_1.ContainerID
            attribute: str
            value: str
            valid_until: int
            def __init__(self, container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ..., attribute: _Optional[str] = ..., value: _Optional[str] = ..., valid_until: _Optional[int] = ...) -> None: ...
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_V1_FIELD_NUMBER: _ClassVar[int]
        parameters: SetAttributeRequest.Body.Parameters
        signature: _types_pb2_1_1.SignatureRFC6979
        session_token: _types_pb2_1_1_1.SessionTokenV2
        session_token_v1: _types_pb2_1_1_1.SessionToken
        def __init__(self, parameters: _Optional[_Union[SetAttributeRequest.Body.Parameters, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ..., session_token: _Optional[_Union[_types_pb2_1_1_1.SessionTokenV2, _Mapping]] = ..., session_token_v1: _Optional[_Union[_types_pb2_1_1_1.SessionToken, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    BODY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    body: SetAttributeRequest.Body
    body_signature: _types_pb2_1_1.Signature
    def __init__(self, body: _Optional[_Union[SetAttributeRequest.Body, _Mapping]] = ..., body_signature: _Optional[_Union[_types_pb2_1_1.Signature, _Mapping]] = ...) -> None: ...

class SetAttributeResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _types_pb2_1_1_1_1.Status
    def __init__(self, status: _Optional[_Union[_types_pb2_1_1_1_1.Status, _Mapping]] = ...) -> None: ...

class RemoveAttributeRequest(_message.Message):
    __slots__ = ("body", "body_signature")
    class Body(_message.Message):
        __slots__ = ("parameters", "signature", "session_token", "session_token_v1")
        class Parameters(_message.Message):
            __slots__ = ("container_id", "attribute", "valid_until")
            CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
            VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
            container_id: _types_pb2_1_1.ContainerID
            attribute: str
            valid_until: int
            def __init__(self, container_id: _Optional[_Union[_types_pb2_1_1.ContainerID, _Mapping]] = ..., attribute: _Optional[str] = ..., valid_until: _Optional[int] = ...) -> None: ...
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_V1_FIELD_NUMBER: _ClassVar[int]
        parameters: RemoveAttributeRequest.Body.Parameters
        signature: _types_pb2_1_1.SignatureRFC6979
        session_token: _types_pb2_1_1_1.SessionTokenV2
        session_token_v1: _types_pb2_1_1_1.SessionToken
        def __init__(self, parameters: _Optional[_Union[RemoveAttributeRequest.Body.Parameters, _Mapping]] = ..., signature: _Optional[_Union[_types_pb2_1_1.SignatureRFC6979, _Mapping]] = ..., session_token: _Optional[_Union[_types_pb2_1_1_1.SessionTokenV2, _Mapping]] = ..., session_token_v1: _Optional[_Union[_types_pb2_1_1_1.SessionToken, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    BODY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    body: RemoveAttributeRequest.Body
    body_signature: _types_pb2_1_1.Signature
    def __init__(self, body: _Optional[_Union[RemoveAttributeRequest.Body, _Mapping]] = ..., body_signature: _Optional[_Union[_types_pb2_1_1.Signature, _Mapping]] = ...) -> None: ...

class RemoveAttributeResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _types_pb2_1_1_1_1.Status
    def __init__(self, status: _Optional[_Union[_types_pb2_1_1_1_1.Status, _Mapping]] = ...) -> None: ...
