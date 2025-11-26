from Classes.Autokolcsonzo import Autokolcsonzo
# from Classes.Berles import Berles
from Classes.Szemelyauto import Szemelyauto
from Classes.Teherauto import Teherauto

def alap_adatok_betoltese():
    kolcsonzo = Autokolcsonzo("BudaRent", "Budapest", 10)
    # berles = Berles(kolcsonzo)

    auto1 = Szemelyauto(
        tipus="személyautó",
        rendszam="ABC-123",
        marka="Toyota Corolla",
        szin="piros",
        evjarat=2018,
        berleti_dij=8000
    )

    auto2 = Teherauto(
        tipus="teherautó",
        rendszam="XYZ-555",
        marka="Ford Transit",
        szin="fehér",
        evjarat=2020,
        berleti_dij=15000
    )

    auto3 = Szemelyauto(
        tipus="személyautó",
        rendszam="JHG-777",
        marka="Volkswagen Minivan",
        szin="kék",
        evjarat=2016,
        berleti_dij=9000
    )

    auto4 = Teherauto(
        tipus="teherautó",
        rendszam="TRK-220",
        marka="MAN eTGS",
        szin="szürke",
        evjarat=2019,
        berleti_dij=18000
    )

    auto5 = Szemelyauto(
        tipus="személyautó",
        rendszam="MNO-444",
        marka="BMW 320",
        szin="fekete",
        evjarat=2022,
        berleti_dij=20000
    )

    auto6 = Teherauto(
        tipus="teherautó",
        rendszam="FGT-902",
        marka="Mercedes Sprinter",
        szin="sárga",
        evjarat=2017,
        berleti_dij=16000
    )

    auto7 = Szemelyauto(
        tipus="személyautó",
        rendszam="KLP-330",
        marka="Honda Civic",
        szin="fehér",
        evjarat=2021,
        berleti_dij=11000
    )

    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto1)
    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto2)
    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto3)
    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto4)
    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto5)
    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto6)
    kolcsonzo.auto_hozzaadas_kolcsonzohoz(auto7)

    return kolcsonzo