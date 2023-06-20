import types
import typing

import cartographer_ros_msgs.msg
import genpy
import std_msgs.msg

class LandmarkList(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    landmarks: typing.List[cartographer_ros_msgs.msg.LandmarkEntry]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        landmarks: typing.List[cartographer_ros_msgs.msg.LandmarkEntry] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LandmarkList: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LandmarkList: ...
