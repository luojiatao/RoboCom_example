import types
import typing

import genpy

class StatusCode(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    OK: int
    CANCELLED: int
    UNKNOWN: int
    INVALID_ARGUMENT: int
    DEADLINE_EXCEEDED: int
    NOT_FOUND: int
    ALREADY_EXISTS: int
    PERMISSION_DENIED: int
    RESOURCE_EXHAUSTED: int
    FAILED_PRECONDITION: int
    ABORTED: int
    OUT_OF_RANGE: int
    UNIMPLEMENTED: int
    INTERNAL: int
    UNAVAILABLE: int
    DATA_LOSS: int

    def __init__(self, *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> StatusCode: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> StatusCode: ...
