# wyjątki - błędy podczas działania programu
# przerywają działąnie programu

# print(2 / 0)
# print("Dalsza część programu")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\Desktop\AG\ppdp-29-02\wyjatki.py", line 4, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1
# przechwytywanie i obsługa wyjątków (błędów)
# try except [else, finally]
try:
    print(2 / 0)
except ZeroDivisionError:
    print("Nie dziel przez zero")
print("Dalsza częśc programu")
# Nie dziel przez zero
# Dalsza częśc programu

# aplikacja kalkulator
# powinna dac do wyboru działania
# pobrac liczby
# wyswietlic łądnie wynik działania 1 + 3 = 4
# spróbowac wygenerowac błedy i je obsłużyc

# menu z opcjami
# pobrac rodzaj działania
# pobrać liczby
# wykonać działanie
# wyswietlic
# obsłuzyc możliwosc zakonczenia programu

print("""
1.Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
5. Koniec
""")
odp = input("Podaj operacje do wykonania")
try:
    a = int(input("Podaj pierwszą liczbę"))
    b = int(input("Podaj druga liczbę"))
    if odp == '1':
        print(f'Wynik działania {a} + {b} = {a + b}')
    elif odp == '2':
        print(f'Wynik działania {a} - {b} = {a - b}')
    elif odp == '3':
        print(f'Wynik działania {a} * {b} = {a * b}')
    elif odp == '4':
        print(f'Wynik działania {a} / {b} = {a / b}')
except ValueError as e:
    print("Błąd wartości", e)
except TypeError as e:
    print("Błąd typu", e)
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)
except Exception as e:
    print("Błąd", e)
else:
    print("Wykona się gdy nie ma błedu")
finally:
    print("Wykona sie zawsze niezależnie czy bład sie pojawi czy nie")
# ValueError
