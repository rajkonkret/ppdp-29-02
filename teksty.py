tekst = "Witaj świecie"
print(tekst)
print(type(tekst))  # <class 'str'>
tekst.upper()  # funkcj zwraca wynik, nie zamienie bazowych danych
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj świecie
# teksty sa niemutowalne
print(tekst.upper())  # wyswietlamy wynik działania funkcji WITAJ ŚWIECIE
tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE
print(tekst.count("a"))
print(tekst.count("a", 0, 4))  # Wita  4 poza zakresem 0123 - 4 poza zakresem
# indeksy numerowane o 0
print(len(tekst))

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - binarnie (bajtowo)
# \x - w postaci szesnastkowej
print(type(encoded_s))  # <class 'bytes'>

print(encoded_s.decode('utf-8'))  # Witaj świecie

imie = "Radek"
print("Imie:", imie)  # Imie: Radek

tekst_format = f"Mam na imię {imie} i lubię pythona."
# f - fstring
print(tekst_format)  # Mam na imię Radek i lubię pythona.

starszy = "Witaj %s"
print(starszy % imie)  # Witaj Radek

print("Witaj {}".format(imie))  # Witaj Radek

print("""
    Tekst
wielolinijkowy""")
#     Tekst
# wielolinijkowy

print("Tekst"
      " wielolinijkowy")
# Tekst wielolinijkowy
print("\tTekst\nwielolinijkowy")
# 	Tekst
# wielolinijkowy
# \t tabulator
# \n nowa linia
# \b backspace
print("Radek.\b")  # Radek
