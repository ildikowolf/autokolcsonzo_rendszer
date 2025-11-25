from Classes.Berles import Berles

jarmu = Berles()

auto1 = jarmu.auto_felvetel(
        tipus="személyautó",
        rendszam="ABC-123",
        marka="Toyota",
        szin="piros",
        evjarat=2018,
        berleti_dij=8000
    )

auto2 = jarmu.auto_felvetel(
        tipus="teherautó",
        rendszam="XYZ-555",
        marka="Ford",
        szin="fehér",
        evjarat=2020,
        berleti_dij=15000
    )

print(auto1)
print(auto2)