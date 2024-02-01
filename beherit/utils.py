import itertools
from typing import Optional


def check_dtype(data) -> Optional[str]:
    dtype = set([type(x).__name__ for x in list(itertools.chain(*data))])

    if len(dtype) > 1: return None

    return dtype[0]
