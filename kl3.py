class Car:
    """
    Klasa opisująca samochód w Pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole jest prywatne

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f'Prędkość wynosi {self.__predkosc} km/h')

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):  # metoda prywatna
        print("Zmien bieg")


car1 = Car("Saab", 2024)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu pola predkosc jako prywatne mamy bład:
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)  # 50
car1.licznik()  # Prędkość wynosi 50 km/h
car1.__predkosc = 0  # przypadkowo nadajemy pole publiczne o tej samej nazwie
car1.licznik()  # Prędkość wynosi 50 km/h
print(car1.__predkosc)  # 0
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
# Prędkość wynosi 50 km/h
# Prędkość wynosi 50 km/h
# 0
# Zmien bieg
# Zmien bieg
# Zmien bieg
# Zmien bieg
# Zmien bieg
# Prędkość wynosi 0 km/h
