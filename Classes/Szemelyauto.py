from Classes.Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
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
        return f"{self._marka} {self._tipus} ({self._rendszam}) - {self._berleti_dij} Ft/nap"