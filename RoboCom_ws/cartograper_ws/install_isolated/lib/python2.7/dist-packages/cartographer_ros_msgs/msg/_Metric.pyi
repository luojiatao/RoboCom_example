import types
import typing

import cartographer_ros_msgs.msg
import genpy

class Metric(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    TYPE_COUNTER: int
    TYPE_GAUGE: int
    TYPE_HISTOGRAM: int

    # Fields
    type: int
    labels: typing.List[cartographer_ros_msgs.msg.MetricLabel]
    value: float
    counts_by_bucket: typing.List[cartographer_ros_msgs.msg.HistogramBucket]

    def __init__(
        self,
        type: int = ...,
        labels: typing.List[cartographer_ros_msgs.msg.MetricLabel] = ...,
        value: float = ...,
        counts_by_bucket: typing.List[cartographer_ros_msgs.msg.HistogramBucket] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Metric: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Metric: ...
