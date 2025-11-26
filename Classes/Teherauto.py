from Classes.Auto import Auto
from datetime import datetime

# Gyerek osztály
class Teherauto(Auto):
    def __init__(self, rendszam, marka, tipus, szin, berleti_dij, evjarat, teherbiras):
        super().__init__(rendszam, marka, tipus, szin, berleti_dij)
        self._evjarat = evjarat
        self._teherbiras = teherbiras # kg
    
    @property
    def evjarat(self):
        return self._evjarat
    
    @evjarat.setter
    def evjarat(self, ertek):
        aktualis_ev = datetime.now().year
        if ertek < 2010 or ertek > aktualis_ev:
            raise ValueError(f"Az évjáratnak (teherautónál) 2010 és {aktualis_ev} között kell lennie!")
        self._evjarat = ertek    
    
    @property
    def teherbiras(self):
        return self._teherbiras
    
    @teherbiras.setter
    def teherbiras(self, uj_teherbiras):
        if uj_teherbiras <= 0:
            raise ValueError("A teherbírás értéke nem lehet nulla!")
        self._teherbiras = uj_teherbiras

    def auto_berles(self, datum_str):
        return super().auto_berles(datum_str)

    def auto_berles_lemondas(self, datum_str):
        return super().auto_berles_lemondas(datum_str)
    
    def _tipus_specifikus_adatok(self):
        return f"Teherbírás: {self._teherbiras} kg"