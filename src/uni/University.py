from abc import ABC, abstractmethod
import os

class University(ABC):
    @abstractmethod
    def ScrapeForData(self, isRaw):
        pass

    @abstractmethod
    def OutputCSV(self):
        pass

    @abstractmethod
    def OutputRaw(self):
        pass