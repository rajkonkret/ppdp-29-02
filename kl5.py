# dziedziczenie
# mamy klase ogolnie opisujaca obiekt
# podklasy, które uszczegółowiają (np.: dzielą na typy)
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczenie po klasie Pojazd
    """
    Klasa samochód
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # wywołanie kontruktora z klasy wyzszej(super) obowiązkowe
        self.marka = marka

    def info(self):
        super().info()  # opcjonalnie - wywołanie metody z klasy wyzszej
        print(f"Marka: {self.marka}")


poj = Pojazd("Zielony")
poj.info()

sam = Samochod("Czerwony", "Ford")
sam.info()

# Kolor: Zielony
# Kolor: Czerwony
# Marka: Ford

lista = [poj, sam]
for i in lista:
    i.info()
# polimorfizm - obiekty roznych kals posiadają wspólne cechy i funkcje. mozemy te same operacje wykonac na obiektach
