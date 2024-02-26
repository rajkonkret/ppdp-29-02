import sys

user = "Tomek"  # str
wiek = 39  # int - liczby całkowite
wersja = 3.900001  # float - zmiennoprzecinkowe
liczba = 134567890321  # int
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300,
# str_digits_check_threshold=640)

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# sprawdza typ danych
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, "wiek": wiek})
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 39 lat

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.
print("Witaj {}, masz teraz {} lat.".format(wiek, user))  # Witaj 39, masz teraz Tomek lat.

print("Uzywamy wersji python %i" % 3)  # Uzywamy wersji python 3

print("Uzywamy wersji python %f" % 3.9)  # Uzywamy wersji python 3.900000
print("Uzywamy wersji python %.1f" % 3.9)  # Uzywamy wersji python 3.9
print("Uzywamy wersji python %.2f" % 3.9)  # Uzywamy wersji python 3.90
print("Uzywamy wersji python %.f" % 3.9)  # Uzywamy wersji python 4  - zaokrągla podczas wyświetlania
print("Uzywamy wersji python %.0f" % 3.9)  # Uzywamy wersji python 4
a = 3.9
print("a= %.0f" % a)  # a= 4 - zaokrągla do wyswietlania
print("a=", a)  # a= 3.9  - ale nie zmienia wartości zmiennej

print("Uzywamy wersji Python {:.1f}".format(wersja))
print("Uzywamy wersji Python {}".format(wersja))
# Uzywamy wersji Python 3.9
# Uzywamy wersji Python 3.900001
# ctrl / - komentarz zanzaczonego bloku
print(f"Używamy pythona {wersja:.1f}")
print(f"Używamy pythona {wersja:.2f}")
print(f"Używamy pythona {wersja:.0f}")
# Używamy pythona 3.9
# Używamy pythona 3.90
# Używamy pythona 4

print(len(user))
print(f"{user:>10}")  # "     Tomek"
print(f"{user:>20}")  # "               Tomek"
print(f"{user:<30}")  # "Tomek                         "
print(f"{user:^20}")  # "       Tomek        "
print(f"{user:^20}".replace(" ", "0"))  # "0000000Tomek00000000"

print(liczba)  # 134567890321
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,890,321
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134,567,890,321
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134,567,890,321
# Nasza duża liczba 134.567.890.321
# Nasza duża liczba 134 567 890 321
# 13:30
