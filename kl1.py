# klasy - element programowania obiektowego
# klasa - szablon, przepis na obiekt (stempelek)
# cechy - pola
# funkcje - funkcje mozliwe do wykonania na obiekcie
# obiekt - stworzyne wg przepisu (odcisk stempla) - instancja klasy
# abstrakcja, hermetyzacja(enkapsulacja), dziedziczenie, polimorfizm

# deklaracja klasy - tu sie nie wykunuje
class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # wypisze wiek obiektu
    def podaj_wiek(self):
        print(f"Masz {self.wiek} lat.")


print(Human.__doc__)  # Klasa Human opisująca człowieka w Pythonie
cz1 = Human()  # tworzenie obiektu, moemnt uruchomienia klasy
print(cz1)  # <__main__.Human object at 0x00000214B27C58B0>
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
#
# None
cz1.imie = "Anna"
cz1.wiek = "38"
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
# Anna
# 38
cz1.powitanie()  # Nazywam się Anna
# stworzyc inny obiekt odmiennej płci
# nadac imie, wiek, płeć

cz2 = Human()
cz2.plec = "m"
cz2.imie = "Stefan"
cz2.wiek = 47
print(cz2.plec)
print(cz2.imie)
print(cz2.wiek)
cz2.powitanie()
# m
# Stefan
# 47
# Nazywam się Stefan
cz2.podaj_wiek()  # Masz 47 lat.
