from abc import abstractmethod


class Data:
    @abstractmethod
    def __init__(self, origin_source: str = None):
        pass

    @abstractmethod
    def save(self):
        pass