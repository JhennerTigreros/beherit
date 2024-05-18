

from dataclasses import dataclass


@dataclass(order=True)
class Allocator:
    def alloc(self) -> None: ...

class LRUAlloc(Allocator):
    
    def alloc(self) -> None: 

    

class MetalAlloc(Allocator):
    pass