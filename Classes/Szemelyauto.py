from Classes.Auto import Auto
from datetime import datetime

# Gyerek osztály
class Szemelyauto(Auto):
    def __init__(self, rendszam, marka, tipus, szin, berleti_dij, evjarat, ferohely):
        super().__init__(rendszam, marka, tipus, szin, berleti_dij)
        self._evjarat = evjarat
        self._ferohely = ferohely
    
    @property
    def evjarat(self):
        return self._evjarat
    
    @evjarat.setter
    def evjarat(self, ertek):
        aktualis_ev = datetime.now().year
        if ertek < 2005 or ertek > aktualis_ev:
            raise ValueError(f"Az évjáratnak (teherautónál) 2005 és {aktualis_ev} között kell lennie!")
        self._evjarat = ertek
    
    @property
    def ferohely(self):
        return self._ferohely
    
    @ferohely.setter
    def ferohely(self, uj_ferohely):
        if 0 <= uj_ferohely < 9:
            raise ValueError("A férőhelyeknek 1 és 8 között lehet!")
        self._ferohely = uj_ferohely

    def auto_berles(self, datum_str):
        return super().auto_berles(datum_str)

    def auto_berles_lemondas(self, datum_str):
        return super().auto_berles_lemondas(datum_str)
    
    def _tipus_specifikus_adatok(self):
        return f"Férőhelyek: {self._ferohely}"