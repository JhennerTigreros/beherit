from dataclasses import dataclass
from typing import Tuple, Optional
from beherit.compute.device import Device

from beherit.memory.dtype import DType, check_dtype

@dataclass(order=True)
class Buffer:
    device: Device
    dtype: DType
    shape: Tuple[int, ...]

    def realize(self): ...


class LazyBuffer(Buffer):
    def _to_accelerator(self):
        pass
    
    def realize(self):
        pass

class MemoryBuffer(Buffer):

    def _to_cpu(self):
        pass
    
    def realize(self):
        pass