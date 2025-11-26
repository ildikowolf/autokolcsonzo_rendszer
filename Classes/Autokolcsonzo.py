class Autokolcsonzo:
    def __init__(self, nev, tartozkodasi_hely, kapacitas):
        if kapacitas < 0:
            raise ValueError("A kapacitás nem lehet negatív!")
        
        self._nev = nev
        self._tartozkodasi_hely = tartozkodasi_hely
        self._kapacitas = kapacitas
        self._autok = []

    @property
    def nev(self):
        return self._nev

    @property
    def tartozkodasi_hely(self):
        return self._tartozkodasi_hely

    @property
    def kapacitas(self):
        return self._kapacitas

    @property
    def autok(self):
        return self._autok
    
    """
    # autó hozzáadása
    def auto_hozzaadas(self, auto):
        if len(self._autok) >= self._kapacitas:
            raise ValueError("A kölcsönző megtelt, nem vehető fel több autó.")
        else:
            self._autok.append(auto)
            print("Autó sikeresen hozzáadva a kölcsönzőhöz.")

    # autó törlése
    def auto_torles(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                self._autok.remove(auto)
                print(f"Autó sikeresen törölve.")
            else:
                print("Ilyen rendszámú autó nincs a kölcsönzőben.")
    """

    # autók listázása
    def autok_listazasa(self):
        if not self._autok:
            print("Nincs autó a kölcsönzőben.")
        else:
            print(f"A(z) {self._nev} kölcsönzőben a következő járművek bérelhetők:\n")
            for auto in self._autok:
                print(auto)

        szemelyauto = sum(1 for sz in self._autok
                          if sz._tipus == "személyautó")
        teherauto = sum(1 for t in self._autok
                        if t._tipus == "teherautó")
        
        print(f"\nBérelhető személyautók: {szemelyauto}")
        print(f"Bérelhető teherautók: {teherauto}")

    def __str__(self):
        return f"{self._nev} ({self._tartozkodasi_hely}) — {len(self._autok)}/{self._kapacitas} autó"