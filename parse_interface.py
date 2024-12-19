from abc import ABC, abstractmethod

class ParseInterface(ABC):
    @abstractmethod
    def parse(self):
        pass