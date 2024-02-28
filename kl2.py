class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print(f"Mam {self.wiek} lat")

    def podaj_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def podaj_plec(self):
        print(f"Jestem {self.plec}")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def __repr__(self):  # reprezentacja obiektu
        return f"{self.imie}, {self.wiek}"


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Anna", 45, 170)
cz1.powitanie()
cz1.podaj_plec()
cz1.podaj_wzrost()
cz1.podaj_wiek()
# Nazywam się Anna
# Jestem k
# Mam 170 cm wzrostu
# Mam 45 lat

cz2 = Human("Radek", 47, 190, "m")
cz2.podaj_wiek()
cz2.powitanie()
cz2.podaj_plec()
cz2.podaj_wzrost()
# Mam 47 lat
# Nazywam się Radek
# Jestem m
# Mam 190 cm wzrostu

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
# del(cz2)
# cz2.powitanie(
# NameError: name 'cz2' is not defined. Did you mean: 'cz1'?

lista = [cz1, cz2]
print(lista)  # [<__main__.Human object at 0x000001F74BBDE9C0>, <__main__.Human object at 0x000001F74B8AA360>]
for i in lista:
    print(i.imie)
# po dodaniu __repr__ obiekt wyswietla sie w sposób czytelny
print(lista)  # [Anna, 45, Radek, 47]
# 14:30
