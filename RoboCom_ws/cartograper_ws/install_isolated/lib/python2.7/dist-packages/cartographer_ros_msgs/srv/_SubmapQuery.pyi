import types
import typing

import cartographer_ros_msgs.msg
import genpy

class SubmapQueryRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    trajectory_id: int
    submap_index: int

    def __init__(
        self,
        trajectory_id: int = ...,
        submap_index: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SubmapQueryRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SubmapQueryRequest: ...

class SubmapQueryResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    status: cartographer_ros_msgs.msg.StatusResponse
    submap_version: int
    textures: typing.List[cartographer_ros_msgs.msg.SubmapTexture]

    def __init__(
        self,
        status: cartographer_ros_msgs.msg.StatusResponse = ...,
        submap_version: int = ...,
        textures: typing.List[cartographer_ros_msgs.msg.SubmapTexture] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SubmapQueryResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SubmapQueryResponse: ...

class SubmapQuery(object):
    _type: str
    _md5sum: str
    _request_class = SubmapQueryRequest
    _response_class = SubmapQueryResponse
