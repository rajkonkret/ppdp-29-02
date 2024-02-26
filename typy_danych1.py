import sys

wiek = 47
rok = 2023
temp = 36.6  # float
wiek2 = 37.5  # float
# 36,6 - to nie jest float

print(wiek)
print(type(wiek))  # <class 'int'>
print(type(wiek2))  # <class 'float'>

print(5 * "Radek")  # RadekRadekRadekRadekRadek

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # int / int = float
# 2070
# -1976
# 95081
# 0.023232822540781017  - float
print(wiek // rok)  # częśc całkowita z dzielenie 0
print(wiek % rok)  # reszta z dzielenia, modulo  47
print(5 / 2)  # 2.5 2 całe
print(2 * 2)  # 4
print(5 - 4)  # 1

print(wiek ** rok)
print(len(str(wiek ** rok)))  # liczba ma 3383 znaków

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - (5 * 43) + (4 / 2 + 4) / 2)
# -157.0
# -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# przy float wystepuje bład zaokrąglenia
# przechowywane w pamieci jako mantysa i wykładnik
# x * 10 ^ y -> x * 2 ^ y
# sa przechowywane z okresloną dokładnością
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
wynik = 0.2 + 0.7
print(f"{wynik:.1f}")  # 0.9
print(wynik)  # 0.8999999999999999
print(f"Sprawdzanie zmmiennej temp {wiek} {temp}")

print(f"""
{temp}
    {wiek}
""")
# 36.6
#     47

print(type(4 / 2))  # <class 'float'>
print(type(4 // 2))  # <class 'int'>

# str, int, float

# typ logiczny
# True, False - prawda, fałsz
czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python))  # <class 'bool'>
print(int(True))  # 1
print(int(False))  # 0

x = 1
print(bool(x))  # True

x = 100
print(bool(x))  # True

x = -10
print(bool(x))  # True

x = "Radek"
print(bool(x))  # True

x = 0
print(bool(x))  # False

x = ''
print(bool(x))  # False

x = None  # odpowiednik nulla, nic, stan nieokreślony
print(bool(x))  # False

a = 14
b = 3

print(f"Wynik porównania {a} > {b}", a > b)
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)  # == - porównanie
print(f"Wynik porównania {a} != {b}", a != b)
# Wynik porównania 14 > 3 True
# Wynik porównania 14 < 3 False
# Wynik porównania 14 == 3 False
# Wynik porównania 14 != 3 True

# and -> i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or -> lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

print(True & True)  # porównanie bitowe
