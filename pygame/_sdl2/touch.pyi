# Portions (c) Microsoft Corporation

from typing import Callable, Mapping, Optional, Union


def get_num_devices() -> int: ...
def get_device(index: int) -> int: ...
def get_num_fingers(device_id: int) -> int: ...
def get_finger(touchid: int, index: int) -> Mapping[str, Union[int, float]]: ...
def get_audio_device_name(index: int, iscapture: bool) -> str: ...
def get_num_audio_devices(iscapture: bool) -> int: ...

# def    AUDIO_F32,
# def    AUDIO_ALLOW_FORMAT_CHANGE,

class AudioDevice:
    def __init__(
        self,
        devicename: Optional[str] = ...,
        iscapture: Optional[bool] = ...,
        frequency: Optional[int] = ...,
        audioformat: Optional[int] = ...,
        numchannels: Optional[int] = ...,
        chunksize: Optional[int] = ...,
        allowed_changes: Optional[int] = ...,
        callback: Optional[Callable[[AudioDevice, bytes], None]] = ...,
    ) -> None: ...
    def iscapture(self) -> bool: ...
    def deviceid(self) -> int: ...
    def devicename(self) -> str: ...
    def callback(self) -> Callable[[AudioDevice, bytes], None]: ...
    def frequency(self) -> int: ...
    def audioformat(self) -> int: ...
    def numchannels(self) -> int: ...
    def chunksize(self) -> int: ...
    def pause(self, pause_on: bool) -> None: ...
    def close(self) -> None: ...
