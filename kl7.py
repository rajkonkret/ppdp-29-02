from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna, obowiazkowa do nadpisania przy dziedziczeniu
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, 'Ja nie latam')

    def wydaj_odglos(self):
        print("Ko ko ko ko koo")

    def dziobanie(self):
        print(f"Tu {self.gatunek}. Idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("Kier kieeer kir")

    def poluj(self):
        print(f"Tu {self.gatunek}, Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa
    Traceback (most recent call last):
  File "C:\Users\CSComarch\Desktop\AG\ppdp-29-02\kl7.py", line 65, in <module>
    sowa = Sowa("Sowa", 10)
           ^^^^^^^^^^^^^^^^
TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
    """


# Po oznaczeniu metodu jako abstrakcyjna, nie można tworzyc obiektów tej klasy
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\Desktop\AG\ppdp-29-02\kl7.py", line 37, in <module>
#     or1 = Ptak("Orzel Bielik", 45)
#           ^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel Bielik", 45)
# or1.latam()  # Tu Orzel Bielik Lecę z szybkością 45
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()  # Ko ko ko ko koo

or2 = Orzel("Orzeł Bielik", 50)
or2.latam()
or2.wydaj_odglos()  # Kier kieeer kir

# Traceback (most recent call last):
#   File "C:\Users\CSComarch\Desktop\AG\ppdp-29-02\kl7.py", line 65, in <module>
#     sowa = Sowa("Sowa", 10)
#            ^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 10)
