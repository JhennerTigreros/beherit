from __future__ import annotations

from typing import Tuple, List
from beherit.storage import Storage
import platform
from beherit.utils import check_dtype

class Tensor:
    dim: Tuple[int, ...]
    strides: Tuple[int, int, int]
    dtype: str
    storage: Storage
    # TODO: Support more formats of tensor
    layout: str = "strided"

    def __init__(self, data, dtype=None, device="cpu") -> None:
        if dtype is not None:
            self.dtype = dtype
        else:
            dtype =  check_dtype(data)
            if not dtype:
                raise Exception("Dtype not matching")
            self.dtype = dtype
        
        if platform.system() == "Darwin":
            device = "metal"

        self.storage = Storage(device, data)
        self.dim = tuple([len(data), len(data[0])])

    def __getitem__(self, indices) -> Tensor:
        if type(indices) is tuple:
            return Tensor(self.storage.data[indices[0]][indices[1]])

        return Tensor(self.storage.data[indices])

    def to_list(self) -> List:
        return self.storage.data

    def __repr__(self) -> str:
        return f"Tensor({self.dim[0], self.dim[1]}), Device: {self.storage.device}, DType: {self.dtype}, Data: {self.storage.data}"