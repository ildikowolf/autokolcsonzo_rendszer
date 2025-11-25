from alap_felallas import alap_adatok_betoltese

kolcsonzo = alap_adatok_betoltese()
"""
while True:
    tipus = input("Adja meg a jármű típusát ('személyautó' vagy 'teherautó'): ").lower().strip()

    if tipus in ("személyautó", "szemelyauto", "teherautó", "teherauto"):
        break
    else:
        print("Ismeretlen jármű. Kérem 'személyautó'-t vagy 'teherautó'-t adjon meg.\n")
"""
kolcsonzo.autok_listazasa()