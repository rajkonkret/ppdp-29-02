# zrobic klase Dom
# metraz, kolor, liczba_okien
# pola maja byc prywatne
# wystawic metody to odczytu i zapisy tych pól
# dodać metodę prywatna farba() - ma wypisac zabrakło farby i kolor farby
# wywoływac przy zmianie koloru
# dodac komentarz - dokumentacje klasy
class Dom:
    """
    Klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraż {self.__metraz}")

    def mam_okien(self):
        print(f"Mam okien {self.liczba_okien}")

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input("Podaj liczbę okien"))
        self.liczba_okien = odp
        self.mam_okien()

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.mam_kolor()

    def __farba(self):
        print("Zabrakło farby")


do1 = Dom(200, "czerwony", 6)
do1.mam_kolor()  # Mam kolor czerwony
do1.zmien_metraz()
