from __future__ import annotations
from typing import Tuple, Optional, Union
from beherit.memory.buffer import Buffer
from beherit.compute.device import Device, check_device
from beherit.memory.dtype import DType, check_dtype

import platform


'''
Tensor initialization just need three optional values:
    - data: Esta puede ser una representación de un Buffer (ir a buffer.py para una explicación). O un valor vacio, el
        valor por defecto para estos tensores sera de un tensor de dim=1, values=0, size=0
    - dtype: Tipo de dato que conformara el tensor, para mas información del sistema de tipos ir a dtype.py
    - device: You can pass a custom device or let the code choece the best for your architecture.
'''
class Tensor:
    strides: Tuple[int, int, int]
    buffer: Buffer

    def __init__(self, data: Union[None, Buffer, list], dtype: Optional[DType] = None, device="cpu", shape: Tuple[int, ...] = ()) -> None:
        device = check_device(device)
        if isinstance(data, list):
            shape = (len(data[0]), len(data[1]), len(data[2]))

        self.buffer = Buffer(check_device(device), check_dtype(data, dtype), shape)

        if isinstance(data, list): self.buffer.device.allocate(data)

    def to_list(self) -> list:
        return self.buffer.device

    def __repr__(self) -> str:
        return f"Tensor\nShape:{self.buffer.shape}, Device: {self.buffer.device}, DType: {self.dtype}, Data: {self.buffer.data}"
    
    @property
    def shape(self) -> Tuple[int, ...]: return self.buffer.shape
