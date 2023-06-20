import types
import typing

import genpy
import geometry_msgs.msg

class LandmarkEntry(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    id: str
    tracking_from_landmark_transform: geometry_msgs.msg.Pose
    translation_weight: float
    rotation_weight: float

    def __init__(
        self,
        id: str = ...,
        tracking_from_landmark_transform: geometry_msgs.msg.Pose = ...,
        translation_weight: float = ...,
        rotation_weight: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LandmarkEntry: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LandmarkEntry: ...
