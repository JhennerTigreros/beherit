import itertools


def check_dtype(data) -> str:
    dtype = set([type(x).__name__ for x in list(itertools.chain(*data))])

    if len(dtype) > 1: return dtype

    return dtype
