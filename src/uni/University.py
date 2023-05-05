from abc import ABC, abstractmethod
import os

class University(ABC):
    sep = ","
    wrap = "\""

    @abstractmethod
    def ScrapeForData(self, isRaw, depth, keywords):
        pass

    @abstractmethod
    def OutputCSV(self):
        pass

    @abstractmethod
    def OutputRaw(self):
        pass