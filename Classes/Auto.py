from abc import ABC, abstractmethod
from datetime import datetime, date

# Ősosztály
class Auto(ABC):
    def __init__(self, rendszam, marka, tipus, szin, berleti_dij):
        self._rendszam = rendszam
        self._marka = marka
        self._tipus = tipus
        self._szin = szin
        self._berleti_dij = berleti_dij
        self._berlesek = set()

    @property
    def rendszam(self):
        return self._rendszam
    
    @property
    def marka(self):
        return self._marka

    @property
    def tipus(self):
        return self._tipus
    
    @property
    def szin(self):
        return self._szin

    @property
    def berleti_dij(self):
        return self._berleti_dij
    
    @berleti_dij.setter
    def berleti_dij(self, uj_berleti_dij):
        if uj_berleti_dij <= 0:
            raise ValueError("A bérleti díj nem lehet nulla!")
        self._teherbiras = uj_berleti_dij

    def auto_berles(self, datum_str):       
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            print("Hibás dátumformátum! Használja ezt: ÉÉÉÉ-HH-NN")
            return None

        if datum < date.today():
            print("A dátum nem lehet régebbi a mai napnál!")
            return None
        
        if datum in self._berelt:
            print(f"{self._rendszam} jármű ki van bérelve ekkor: {datum}")
            return None

        self._berelt = True
        print(f"A(z) {self._rendszam} rendszámú autó sikeresen kibérelve.")
        return self._berleti_dij

    def auto_berles_lemondas(self, datum_str):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            print("Hibás dátumformátum! Használja ezt: ÉÉÉÉ-HH-NN")
            return False
        
        if datum not in self._berlesek:
            print(f"{self._rendszam} jármű nincs kibérelve ezen a napon.")
            return False

        self._berlesek.remove(datum)
        print(f"A(z) {self._rendszam} bérlése sikeresen lemondva.")
        return True
    
    @abstractmethod
    def _tipus_specifikus_adatok(self):
        pass

    def __str__(self):
        return f"{self._rendszam} ({self._tipus}) : {self._marka} - {self._berleti_dij} Ft/nap"