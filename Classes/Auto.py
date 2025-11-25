from abc import ABC, abstractmethod

# Ősosztály
class Auto(ABC):
    def __init__(self, tipus, berleti_dij):
        self._tipus = tipus
        self._berleti_dij = berleti_dij

    @abstractmethod
    def auto_berles(self):
        pass

    @abstractmethod
    def auto_berles_lemondas(self):
        pass