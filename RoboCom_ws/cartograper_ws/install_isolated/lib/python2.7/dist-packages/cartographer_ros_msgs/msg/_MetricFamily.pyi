import types
import typing

import cartographer_ros_msgs.msg
import genpy

class MetricFamily(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    name: str
    description: str
    metrics: typing.List[cartographer_ros_msgs.msg.Metric]

    def __init__(
        self,
        name: str = ...,
        description: str = ...,
        metrics: typing.List[cartographer_ros_msgs.msg.Metric] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MetricFamily: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MetricFamily: ...
