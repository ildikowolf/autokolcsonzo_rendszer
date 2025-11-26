from Classes.Szemelyauto import Szemelyauto
from Classes.Teherauto import Teherauto

class Berles:
    def __init__(self, kolcsonzo):
        self._kolcsonzo = kolcsonzo

    """
    # ez nem is ide kell
    def auto_felvetel(self, rendszam, marka, tipus, szin, evjarat, berleti_dij):
        while True:
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
    """    
            
    def berles_felvetele(self, rendszam):
        for auto in self._kolcsonzo.autok:
            if auto._rendszam == rendszam:
                ar = auto.auto_berles()
                if ar is not None:
                    print(f"A bérleti díj: {ar} Ft/nap")
                return
                   
        print("Ilyen rendszámú autó nincs a kölcsönzőben.")