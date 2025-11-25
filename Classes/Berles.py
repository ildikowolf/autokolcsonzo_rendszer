from Classes.Szemelyauto import Szemelyauto
from Classes.Teherauto import Teherauto

class Berles:
    def __init__(self):
        self._kolcsonzo = kolcsonzo

    def auto_felvetel(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
        try:
            if tipus == 'személyautó':
                return Szemelyauto(rendszam, marka, tipus, szin, evjarat, berleti_dij)
            elif tipus == 'teherautó':
                return Teherauto(rendszam, marka, tipus, szin, evjarat, berleti_dij)
            else:
                raise ValueError("Hibás autótípus!")
            
            self._kolcsonzo.auto_hozzaadas(auto)
            return auto
        
        except Exception as e:
            print(f"Ismeretlen hiba történt: {e}")