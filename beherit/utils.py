import itertools
from typing import Tuple

def first_value(x) -> str:
    if type(x) is list:
        return first_value(x[0])
    
    return type(x).__name__

def check_dtype(data) -> Tuple[bool, str]:
    aux_dtype = first_value(data)
    return all([type(x).__name__ == aux_dtype for x in list(itertools.chain(*data))]), aux_dtype