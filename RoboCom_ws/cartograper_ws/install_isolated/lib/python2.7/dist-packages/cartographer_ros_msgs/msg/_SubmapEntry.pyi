import types
import typing

import genpy
import geometry_msgs.msg

class SubmapEntry(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    trajectory_id: int
    submap_index: int
    submap_version: int
    pose: geometry_msgs.msg.Pose
    is_frozen: bool

    def __init__(
        self,
        trajectory_id: int = ...,
        submap_index: int = ...,
        submap_version: int = ...,
        pose: geometry_msgs.msg.Pose = ...,
        is_frozen: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SubmapEntry: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SubmapEntry: ...
