print()  # wydrukuj/wypisz
# ctrl alt l - formatowanie programu wg zasad PEP8
print("Radek")
# ctrl - d  kopiowanie lini
print("Radek")
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# type() - wypisanie typu danej
print(type("Radek"))  # <class 'str'>  dane typu tekstowego
# 11:30

print(39)
print(type(39))  # <class 'int'> - liczby całkowite

print("39" + "15")  # konktenacja tekstów (łączenie) 3915
print(39 + 14)  # 53

print(5 * "4")  # 44444
# print(5 + "4")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# silne typowanie - nie zamienia sam typów danych
print(str(5) + "4")  # str() - rzutowanie na str (zamina)  54
print(5 + int(4))  # 9

imie = "Radek"
print(imie)  # wyswietlenie zawartości zmiennej
print(type(imie))  # <class 'str'>

# typowanie dynamiczne
# w każdej chwili możemy umiescic w zmiennej dowolny typ

imie = 39
print(imie)
print(type(imie))  # <class 'int'>

imie: str = "Radek"  # hinty
imie: str = 39
print(imie)  # <class 'int'>
print(type(imie))  # <class 'int'>

wiek = 45
print(imie + wiek)  # 84

imie = "Radek"
# print(imie + wiek)  # TypeError: can only concatenate str (not "int") to str
