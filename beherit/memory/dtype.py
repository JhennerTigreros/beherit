from dataclasses import dataclass
from itertools  import chain
from typing import Optional, Final

class DTypeException(Exception): pass 

@dataclass(order=True)
class DType:
    size: int
    priority: int
    format: str

class dtypes:
    bool: Final[DType] = DType(1, 0, "bool")
    int8: Final[DType] = DType(1, 1, "char",)
    uint8: Final[DType] = DType(1, 2, "unsigned char")
    int16: Final[DType] = DType(2, 3, "short")
    uint16: Final[DType] = DType(2, 4, "unsigned short")
    int32: Final[DType] = DType(4, 5, "int")
    uint32: Final[DType] = DType(4, 6, "unsigned int")
    int64: Final[DType] = DType(8, 7, "long")
    uint64: Final[DType] = DType(8, 8, "unsigned long")
    float16: Final[DType] = DType(2, 9, "half")
    bfloat16: Final[DType] = DType(2, 10, "__bf16")
    float32: Final[DType] = DType(4, 11, "float")
    float64: Final[DType] = DType(8, 12, "double")

def check_dtype(data, dtype: Optional[DType] = None) -> DType:  # noqa: UP007
    # Check
    tmp_dtype = set([type(x).__name__ for x in list(chain(*data))])

    if len(dtype) > 1: raise DTypeException("dtype not matching")

    return dtype.pop()
