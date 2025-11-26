from Classes.Auto import Auto
from datetime import datetime

class Szemelyauto(Auto):
    def __init__(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
        if berleti_dij <= 0:
            raise ValueError("A bérleti díjnak 0-nál nagyobbnak kell lennie!")

        # 2005-nél ne legyen régebbi
        aktualis_ev = datetime.now().year
        if evjarat < 2005 or evjarat > aktualis_ev:
            raise ValueError(f"Az évjáratnak (személyautónál) 2005 és {aktualis_ev} között kell lennie!")

        super().__init__(tipus, berleti_dij)

        self._rendszam = rendszam
        self._marka = marka
        self._szin = szin
        self._evjarat = evjarat

    def auto_berles(self):
        pass

    def auto_berles_lemondas(self):
        pass

    def __str__(self):
        return f"{self._marka} {self._tipus} - {self._berleti_dij} Ft/nap"