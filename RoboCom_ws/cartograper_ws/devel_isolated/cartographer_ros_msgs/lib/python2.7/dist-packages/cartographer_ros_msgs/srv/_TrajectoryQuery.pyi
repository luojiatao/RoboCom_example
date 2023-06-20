import types
import typing

import cartographer_ros_msgs.msg
import genpy
import geometry_msgs.msg

class TrajectoryQueryRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    trajectory_id: int

    def __init__(self, trajectory_id: int = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> TrajectoryQueryRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> TrajectoryQueryRequest: ...

class TrajectoryQueryResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    status: cartographer_ros_msgs.msg.StatusResponse
    trajectory: typing.List[geometry_msgs.msg.PoseStamped]

    def __init__(
        self,
        status: cartographer_ros_msgs.msg.StatusResponse = ...,
        trajectory: typing.List[geometry_msgs.msg.PoseStamped] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> TrajectoryQueryResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> TrajectoryQueryResponse: ...

class TrajectoryQuery(object):
    _type: str
    _md5sum: str
    _request_class = TrajectoryQueryRequest
    _response_class = TrajectoryQueryResponse
