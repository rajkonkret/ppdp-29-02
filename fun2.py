# funkcje zwracające wynik

def dodaj(a, b):
    return a + b  # zwróc wynik obliczenia


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 4))  # 9
wyn = dodaj(6, 7)
print(f"Wynik działania funkcji {wyn}")  # Wynik działania funkcji 13
print(dodaj(5, 6) + dodaj(8, 7))  # 26

print(oblicz_vat(1000, 7))
print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(vat=8, cena=2000))  # 2160.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0

if zm == 1230:
    print("Prawidłowo")  # Prawidłowo
