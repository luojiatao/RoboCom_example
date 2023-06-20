import types
import typing

import cartographer_ros_msgs.msg
import genpy

class ReadMetricsRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    def __init__(self, *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ReadMetricsRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ReadMetricsRequest: ...

class ReadMetricsResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    status: cartographer_ros_msgs.msg.StatusResponse
    metric_families: typing.List[cartographer_ros_msgs.msg.MetricFamily]
    timestamp: genpy.Time

    def __init__(
        self,
        status: cartographer_ros_msgs.msg.StatusResponse = ...,
        metric_families: typing.List[cartographer_ros_msgs.msg.MetricFamily] = ...,
        timestamp: genpy.Time = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ReadMetricsResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ReadMetricsResponse: ...

class ReadMetrics(object):
    _type: str
    _md5sum: str
    _request_class = ReadMetricsRequest
    _response_class = ReadMetricsResponse
