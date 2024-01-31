from typing import List

class Storage:
    device: str
    data: List

    def __init__(self, device: str, data: List) -> None:
        self.device = device
        self.data = data