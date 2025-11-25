from Classes.Szemelyauto import Szemelyauto
from Classes.Teherauto import Teherauto

class Berles:
    def __init__(self):
        self.autok = []

    def auto_felvetel(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
        if tipus == 'személyautó':
            return Szemelyauto(rendszam, marka, tipus, szin, evjarat, berleti_dij)
        elif tipus == 'teherautó':
            return Teherauto(rendszam, marka, tipus, szin, evjarat, berleti_dij)