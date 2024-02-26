# krotka - kolekcja, niezmienna, niemutowalne
# tupla moze miec zero elementów
# jeden element
# nieskończenie wiele (ograniczone pamięcią)
# (999, 687, 22, 12.34)
# tupla1 = ["Radek"] - lista jednoelementowa
tupla1 = ("Radek")
print(type(tupla1))  # <class 'str'>
print(tupla1)  # Radek
# wyznacznikiem tupli jest przecinek (,)
tupla2 = "Radek",
print(type(tupla2))  # <class 'tuple'>
print(tupla2)  # ('Radek',) PEP zaleca przy tupli jednoelementowej uzyc () i , obowiazkowo
tupla3 = ("Radek",)  # tupla jednoelementowa wypełnia znamiona zmiennej
tupla4 = "Radek"  # str

tupla5 = "Radek", "Asia", 'Zbyszek', "Tomek"
print(tupla5)
print(type(tupla5))
# ('Radek', 'Asia', 'Zbyszek', 'Tomek')
# <class 'tuple'>

tupla6 = 43, 55, 22.34, 11, 200
print(type(tupla6))  # <class 'tuple'>

# tupla jest niezmienna
# tupla6[2] = 0  # TypeError: 'tuple' object does not support item assignment

print(tupla5.index("Tomek"))
print(tupla5.count("Tomek"))
# 3
# 1
# sortowanie krotki zwraca listę
print(sorted(tupla5))  # ['Asia', 'Radek', 'Tomek', 'Zbyszek']

a, b = 1, 2
print(a, b)  # 1 2
a, b = b, a
print(a, b)  # 2 1

tp = 1, 2, 3
print(type(tp))  # <class 'tuple'>
# a, b = tp  # ValueError: too many values to unpack (expected 2)
# rozpakowanie tupli
a, *b = tp
print(a, b)  # 1 [2, 3], * worek na pozostałe dane
print(len(tupla5))  # 4
print(tupla5)  # ('Radek', 'Asia', 'Zbyszek', 'Tomek')
*imie1, imie2, imie3 = tupla5
print(imie1, imie2, imie3)
imie1, *imie2, imie3 = tupla5
print(imie1, imie2, imie3)
imie1, imie2, *imie3 = tupla5
print(imie1, imie2, imie3)
# ['Radek', 'Asia'] Zbyszek Tomek
# Radek ['Asia', 'Zbyszek'] Tomek
# Radek Asia ['Zbyszek', 'Tomek']

lista = list(tupla5)
print(lista)
print(type(lista))
# ['Radek', 'Asia', 'Zbyszek', 'Tomek']
# <class 'list'>
