import types
import typing

import genpy
import std_msgs.msg

class TrajectoryStates(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    ACTIVE: int
    FINISHED: int
    FROZEN: int
    DELETED: int

    # Fields
    header: std_msgs.msg.Header
    trajectory_id: typing.List[int]
    trajectory_state: bytes

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        trajectory_id: typing.List[int] = ...,
        trajectory_state: bytes = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> TrajectoryStates: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> TrajectoryStates: ...
