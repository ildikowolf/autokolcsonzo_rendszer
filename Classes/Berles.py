from Classes.Szemelyauto import Szemelyauto
from Classes.Teherauto import Teherauto

class Berles:
    def __init__(self, kolcsonzo):
        self._kolcsonzo = kolcsonzo

    def auto_felvetel(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
        try:
            if tipus == 'személyautó':
                auto = Szemelyauto(rendszam, marka, tipus, szin, evjarat, berleti_dij)
            elif tipus == 'teherautó':
                auto = Teherauto(rendszam, marka, tipus, szin, evjarat, berleti_dij)
            else:
                raise ValueError("Hibás jármű adat!")
            
            self._kolcsonzo.auto_hozzaadas(auto)
            return auto
        
        except Exception as e:
            print(f"Ismeretlen hiba: {e}")