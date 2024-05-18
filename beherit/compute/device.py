from dataclasses import dataclass
from enum import Enum, auto
from os import getenv
import platform
from beherit.compute.allocator import Allocator, LRUAlloc, MetalAlloc

class Devices(Enum):
    CPU = auto(); METAL = auto(); CUDA = auto(); APPLE = auto()

@dataclass(order=True)
class Device:
    type: Devices
    alloc: Allocator

class MetalDevice(Device):
    def __init__(self):
        super().__init__(Devices.METAL, MetalAlloc())


class LocalDevice(Device):
    def __init__(self):
        super().__init__(Devices.CPU, LRUAlloc())

def check_device(device) -> Device:
    if getenv('METAL', 0): return Device(Devices.METAL, MetalAlloc())
    if getenv('CLANG', 0) or device == 'cpu': return Device(Devices.CPU, LRUAlloc())
    if getenv('CUDA', 0) or device == 'cuda': return Device(Devices.CUDA, Allocator())
    if getenv('AMX', 0) or device == 'amx': return Device(Devices.APPLE, MetalAlloc())

    return Device(Devices.CPU, LRUAlloc())

