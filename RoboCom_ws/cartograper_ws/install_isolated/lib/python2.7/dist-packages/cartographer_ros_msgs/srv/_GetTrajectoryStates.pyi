import types
import typing

import cartographer_ros_msgs.msg
import genpy

class GetTrajectoryStatesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    def __init__(self, *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetTrajectoryStatesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetTrajectoryStatesRequest: ...

class GetTrajectoryStatesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    status: cartographer_ros_msgs.msg.StatusResponse
    trajectory_states: cartographer_ros_msgs.msg.TrajectoryStates

    def __init__(
        self,
        status: cartographer_ros_msgs.msg.StatusResponse = ...,
        trajectory_states: cartographer_ros_msgs.msg.TrajectoryStates = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetTrajectoryStatesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetTrajectoryStatesResponse: ...

class GetTrajectoryStates(object):
    _type: str
    _md5sum: str
    _request_class = GetTrajectoryStatesRequest
    _response_class = GetTrajectoryStatesResponse
