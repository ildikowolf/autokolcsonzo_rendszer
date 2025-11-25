from Classes.Autokolcsonzo import Autokolcsonzo
from Classes.Berles import Berles

def alap_adatok_betoltese():
    kolcsonzo = Autokolcsonzo("BudaRent", "Budapest", 10)
    berles = Berles(kolcsonzo)

    berles.auto_felvetel(
        tipus="személyautó",
        rendszam="ABC-123",
        marka="Toyota Corolla",
        szin="piros",
        evjarat=2018,
        berleti_dij=8000
    )

    berles.auto_felvetel(
        tipus="teherautó",
        rendszam="XYZ-555",
        marka="Ford Transit",
        szin="fehér",
        evjarat=2020,
        berleti_dij=15000
    )

    berles.auto_felvetel(
        tipus="személyautó",
        rendszam="JHG-777",
        marka="Volkswagen Minivan",
        szin="kék",
        evjarat=2016,
        berleti_dij=9000
    )

    berles.auto_felvetel(
        tipus="teherautó",
        rendszam="TRK-220",
        marka="MAN eTGS",
        szin="szürke",
        evjarat=2019,
        berleti_dij=18000
    )

    berles.auto_felvetel(
        tipus="személyautó",
        rendszam="MNO-444",
        marka="BMW 320",
        szin="fekete",
        evjarat=2022,
        berleti_dij=20000
    )

    berles.auto_felvetel(
        tipus="teherautó",
        rendszam="FGT-902",
        marka="Mercedes Sprinter",
        szin="sárga",
        evjarat=2017,
        berleti_dij=16000
    )

    berles.auto_felvetel(
        tipus="személyautó",
        rendszam="KLP-330",
        marka="Honda Civic",
        szin="fehér",
        evjarat=2021,
        berleti_dij=11000
    )

    return kolcsonzo