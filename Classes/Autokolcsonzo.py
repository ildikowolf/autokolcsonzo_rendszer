class Autokolcsonzo:
    def __init__(self, nev, tartozkodasi_hely, kapacitas):
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

    # autó hozzáadása
    def auto_hozzaadas(self, auto):
        if len(self._autok) >= self._kapacitas:
            raise ValueError("A kölcsönző megtelt, nem vehető fel több autó.")

        self._autok.append(auto)

    # autók listázása
    def autok_listazasa(self):
        if not self._autok:
            print("Nincs autó a kölcsönzőben.")
        else:
            for auto in self._autok:
                print(auto)

    def __str__(self):
        return f"{self._nev} ({self._tartozkodasi_hely}) — {len(self._autok)}/{self._kapacitas} autó"