from refs import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_UNSPECIFIED: _ClassVar[Operation]
    EQ: _ClassVar[Operation]
    NE: _ClassVar[Operation]
    GT: _ClassVar[Operation]
    GE: _ClassVar[Operation]
    LT: _ClassVar[Operation]
    LE: _ClassVar[Operation]
    OR: _ClassVar[Operation]
    AND: _ClassVar[Operation]

class Clause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLAUSE_UNSPECIFIED: _ClassVar[Clause]
    SAME: _ClassVar[Clause]
    DISTINCT: _ClassVar[Clause]
OPERATION_UNSPECIFIED: Operation
EQ: Operation
NE: Operation
GT: Operation
GE: Operation
LT: Operation
LE: Operation
OR: Operation
AND: Operation
CLAUSE_UNSPECIFIED: Clause
SAME: Clause
DISTINCT: Clause

class Filter(_message.Message):
    __slots__ = ("name", "key", "op", "value", "filters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    op: Operation
    value: str
    filters: _containers.RepeatedCompositeFieldContainer[Filter]
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ..., op: _Optional[_Union[Operation, str]] = ..., value: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ...) -> None: ...

class Selector(_message.Message):
    __slots__ = ("name", "count", "clause", "attribute", "filter")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    clause: Clause
    attribute: str
    filter: str
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., clause: _Optional[_Union[Clause, str]] = ..., attribute: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class Replica(_message.Message):
    __slots__ = ("count", "selector")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    count: int
    selector: str
    def __init__(self, count: _Optional[int] = ..., selector: _Optional[str] = ...) -> None: ...

class PlacementPolicy(_message.Message):
    __slots__ = ("replicas", "container_backup_factor", "selectors", "filters", "subnet_id", "ec_rules")
    class ECRule(_message.Message):
        __slots__ = ("data_part_num", "parity_part_num", "selector")
        DATA_PART_NUM_FIELD_NUMBER: _ClassVar[int]
        PARITY_PART_NUM_FIELD_NUMBER: _ClassVar[int]
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        data_part_num: int
        parity_part_num: int
        selector: str
        def __init__(self, data_part_num: _Optional[int] = ..., parity_part_num: _Optional[int] = ..., selector: _Optional[str] = ...) -> None: ...
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_BACKUP_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SELECTORS_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    EC_RULES_FIELD_NUMBER: _ClassVar[int]
    replicas: _containers.RepeatedCompositeFieldContainer[Replica]
    container_backup_factor: int
    selectors: _containers.RepeatedCompositeFieldContainer[Selector]
    filters: _containers.RepeatedCompositeFieldContainer[Filter]
    subnet_id: _types_pb2.SubnetID
    ec_rules: _containers.RepeatedCompositeFieldContainer[PlacementPolicy.ECRule]
    def __init__(self, replicas: _Optional[_Iterable[_Union[Replica, _Mapping]]] = ..., container_backup_factor: _Optional[int] = ..., selectors: _Optional[_Iterable[_Union[Selector, _Mapping]]] = ..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ..., subnet_id: _Optional[_Union[_types_pb2.SubnetID, _Mapping]] = ..., ec_rules: _Optional[_Iterable[_Union[PlacementPolicy.ECRule, _Mapping]]] = ...) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("public_key", "addresses", "attributes", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NodeInfo.State]
        ONLINE: _ClassVar[NodeInfo.State]
        OFFLINE: _ClassVar[NodeInfo.State]
        MAINTENANCE: _ClassVar[NodeInfo.State]
    UNSPECIFIED: NodeInfo.State
    ONLINE: NodeInfo.State
    OFFLINE: NodeInfo.State
    MAINTENANCE: NodeInfo.State
    class Attribute(_message.Message):
        __slots__ = ("key", "value", "parents")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        PARENTS_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        parents: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., parents: _Optional[_Iterable[str]] = ...) -> None: ...
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    addresses: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.RepeatedCompositeFieldContainer[NodeInfo.Attribute]
    state: NodeInfo.State
    def __init__(self, public_key: _Optional[bytes] = ..., addresses: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[NodeInfo.Attribute, _Mapping]]] = ..., state: _Optional[_Union[NodeInfo.State, str]] = ...) -> None: ...

class Netmap(_message.Message):
    __slots__ = ("epoch", "nodes")
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    nodes: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    def __init__(self, epoch: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ...) -> None: ...

class NetworkConfig(_message.Message):
    __slots__ = ("parameters",)
    class Parameter(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bytes
        value: bytes
        def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.RepeatedCompositeFieldContainer[NetworkConfig.Parameter]
    def __init__(self, parameters: _Optional[_Iterable[_Union[NetworkConfig.Parameter, _Mapping]]] = ...) -> None: ...

class NetworkInfo(_message.Message):
    __slots__ = ("current_epoch", "magic_number", "ms_per_block", "network_config")
    CURRENT_EPOCH_FIELD_NUMBER: _ClassVar[int]
    MAGIC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MS_PER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    current_epoch: int
    magic_number: int
    ms_per_block: int
    network_config: NetworkConfig
    def __init__(self, current_epoch: _Optional[int] = ..., magic_number: _Optional[int] = ..., ms_per_block: _Optional[int] = ..., network_config: _Optional[_Union[NetworkConfig, _Mapping]] = ...) -> None: ...
