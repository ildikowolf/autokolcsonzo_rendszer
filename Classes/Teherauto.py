from Classes.Auto import Auto
from datetime import datetime

class Teherauto(Auto):
    def __init__(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
        if berleti_dij <= 0:
            raise ValueError("A bérleti díjnak 0-nál nagyobbnak kell lennie!")

        # 2010-nél ne legyen régebbi
        aktualis_ev = datetime.now().year
        if evjarat < 2010 or evjarat > aktualis_ev:
            raise ValueError(f"Az évjáratnak (teherautónál) 2010 és {aktualis_ev} között kell lennie!")
        
        super().__init__(rendszam, tipus, berleti_dij)

        self._marka = marka
        self._szin = szin
        self._evjarat = evjarat
        self._berelt = False

    def auto_berles(self):
        if self._berelt:
            print(f"A(z) {self._rendszam} jármű már ki van bérelve.")
            return None
        else:
            self._berelt = True
            print(f"A(z) {self._rendszam} rendszámú autó sikeresen kibérelve.")
            return self._berleti_dij 

    def auto_berles_lemondas(self):
        pass

    def __str__(self):
        return f"{self._rendszam} : {self._marka} {self._tipus} - {self._berleti_dij} Ft/nap"