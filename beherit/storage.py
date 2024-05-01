from beherit import Device 

class Storage:
    device: str
    data: list

    def __init__(self, device: str, data: list) -> None:
        self.device = device
        self.data = data
