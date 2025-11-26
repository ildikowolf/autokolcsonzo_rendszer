from Classes.Berles import Berles
from alap_felallas import alap_adatok_betoltese

kolcsonzo = alap_adatok_betoltese()

print("\nAutókölcsönző Rendszer by ildikowolf")

kolcsonzo.autok_listazasa()

def menu():
    print("\nVálasszon az alábbi opciók közül:")
    print("1 - Autó bérlése")
    print("2 - Bérlés lemondása")
    print("3 - Bérlések listázása")
    print("4 - Kilépés")

while True:
    menu()
    valasztas = input("\nVálasztás: ").strip()

    if valasztas == "1":
        rendszam = input("Adja meg a bérelni kívánt autó rendszámát: ").strip().upper()
        kolcsonzo_berles = Berles(kolcsonzo)
        kolcsonzo_berles.berles_felvetele(rendszam)

    elif valasztas == "2":
        pass

    elif valasztas == "3":
        pass

    elif valasztas == "4":
        print("Viszontlátásra!")
        break

    else:
        print("Érvénytelen bemenet!")