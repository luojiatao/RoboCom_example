import types
import typing

import cartographer_ros_msgs.msg
import genpy
import geometry_msgs.msg

class StartTrajectoryRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    configuration_directory: str
    configuration_basename: str
    use_initial_pose: bool
    initial_pose: geometry_msgs.msg.Pose
    relative_to_trajectory_id: int

    def __init__(
        self,
        configuration_directory: str = ...,
        configuration_basename: str = ...,
        use_initial_pose: bool = ...,
        initial_pose: geometry_msgs.msg.Pose = ...,
        relative_to_trajectory_id: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> StartTrajectoryRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> StartTrajectoryRequest: ...

class StartTrajectoryResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    status: cartographer_ros_msgs.msg.StatusResponse
    trajectory_id: int

    def __init__(
        self,
        status: cartographer_ros_msgs.msg.StatusResponse = ...,
        trajectory_id: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> StartTrajectoryResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> StartTrajectoryResponse: ...

class StartTrajectory(object):
    _type: str
    _md5sum: str
    _request_class = StartTrajectoryRequest
    _response_class = StartTrajectoryResponse
