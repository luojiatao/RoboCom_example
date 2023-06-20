import types
import typing

import genpy

class BagfileProgress(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    current_bagfile_name: str
    current_bagfile_id: int
    total_bagfiles: int
    total_messages: int
    processed_messages: int
    total_seconds: float
    processed_seconds: float

    def __init__(
        self,
        current_bagfile_name: str = ...,
        current_bagfile_id: int = ...,
        total_bagfiles: int = ...,
        total_messages: int = ...,
        processed_messages: int = ...,
        total_seconds: float = ...,
        processed_seconds: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> BagfileProgress: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> BagfileProgress: ...
