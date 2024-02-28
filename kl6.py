class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Menedzer(Pracownik):
    """
    Klasa Menedzer
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: wynagrodzenie {wyn_prac}")

menago = Menedzer("Anna", "Nowak", 8000, 3000)
menago.przedstaw_sie()
wyn_menago = menago.oblicz_pensje()
print(f"Wynagrodzenie dla menadżera {menago.imie} {menago.nazwisko}: wynagrodzenie {wyn_menago}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika Jan Kowalski: wynagrodzenie 5000
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla menadżera Anna Nowak: wynagrodzenie 11000
