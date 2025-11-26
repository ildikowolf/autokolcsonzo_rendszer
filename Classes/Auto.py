from abc import ABC, abstractmethod

# Ősosztály
class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self._berelt = False 

    @abstractmethod
    def auto_berles(self):
        if self._berelt:
            print(f"A(z) {self._rendszam} jármű már ki van bérelve.")
            return None
        else:
            self._berelt = True
            print(f"A(z) {self._rendszam} rendszámú autó sikeresen kibérelve.")
            return self._berleti_dij

    @abstractmethod
    def auto_berles_lemondas(self):
        if not self._berelt:
            print(f"A(z) {self._rendszam} jármű nincs kibérelve.")
            return False
        else:
            self._berelt = False
            print(f"A(z) {self._rendszam} bérlése sikeresen lemondva.")
            return True