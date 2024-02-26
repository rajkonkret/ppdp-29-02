# lista - kolekcja do przechowywania danch
# zachowuje kolejnośc przy dodawaniu danych
lista = []  # deklarcja pustej listy
print(type(lista))  # <class 'list'>
print(lista)  # []

lista.append("Radek")
lista.append("Maciek")
lista.append("Tomek")
lista.append("Tadek")
lista.append("Zenek")
print(lista)  # ['Radek', 'Maciek', 'Tomek', 'Tadek', 'Zenek']
# listy sa mutowalne
# dokunujemy operacji na bazowej kolekcji
# indeksy numerowane od 0

print(lista[0])  # Radek, indeks 0 - pierwszy element listy
print(lista[3])  # Tadek
print(lista[-1])
print(lista[len(lista) - 1])
# Zenek
# Zenek
# ['Radek', 'Maciek', 'Tomek', 'Tadek', 'Zenek']
#     0         1        2         3       4
#     -5        -4       -3        -2      -1

print(lista[-0])
print(lista[-4])
# slicowanie
print(lista[0:3])  # 0, 1, 2 ['Radek', 'Maciek', 'Tomek']
# print(lista[10])  # IndexError: list index out of range
print(lista[3:10])  # ['Tadek', 'Zenek']
print(lista[9:10])  # []

# nadpisanie elementu na indeksie 2
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Tadek', 'Zenek']

# dodanie element na zadanym miejscu (indeksie)
lista.insert(1, "Anna")
print(lista)  # ['Radek', 'Anna', 'Maciek', 'Mikołaj', 'Tadek', 'Zenek']

# usniecie lementu z listy
lista.remove("Maciek")
print(lista)  # ['Radek', 'Anna', 'Mikołaj', 'Tadek', 'Zenek']

element = lista.pop(2)
print(lista)  # ['Radek', 'Anna', 'Tadek', 'Zenek']
print(element)  # Mikołaj

indeks = lista.index("Tadek")
print(indeks)  # 2

print(lista)
lista.append('Tadek')
print(lista)
lista.remove('Tadek')
print(lista)
# ['Radek', 'Anna', 'Tadek', 'Zenek']
# ['Radek', 'Anna', 'Tadek', 'Zenek', 'Tadek']
# ['Radek', 'Anna', 'Zenek', 'Tadek']
# usunął pierwszego napotkanego

a = 7
b = 9
b = a
print(a)  # 7
a = 10
print(b)  # 7

# lista = a
# lista2 = b
lista_copy = lista.copy()  # kopiowanie elementów do drugiej listy
lista2 = lista  # kopiowanie referencji, kopiowanie adresu gdzie znajduje się lista
print(lista)
print(lista2)
lista.clear()  # usunięcie wszystkich elementów z listy
print(lista)
print(lista2)
print(id(lista))  # 2306648625536
print(id(lista2))  # 2306648625536
print(lista_copy)  # ['Radek', 'Anna', 'Zenek', 'Tadek']
print(id(lista_copy))  # 2406548485824

print("Radek" in lista_copy)  # True

liczby = [54, 999, 34, 22, 12.34, 687]
liczby2 = [54, 999, 34, 22, 12.34, 687, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 687]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]
# liczby2.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

osoby = ['radek', 'ola', 'agata']
osoby.sort()
print(osoby.sort())  # None
print(osoby)  # ['agata', 'ola', 'radek']

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22, 12.34]
liczby.sort(reverse=True)  # posortowane i odwrócone
print(liczby)  # [999, 687, 54, 34, 22, 12.34]

liczby[3] = 6666
print(liczby)

print(liczby[0:3])
print(liczby[-2])
print(liczby[-2:0])  # []
# [999, 687, 54, 34, 22, 12.34]
#   0    1    2   3   4     5
#   -6   -5   -4  -3  -2    -1
print(liczby[-2:5])  # [22]

indeks = liczby.index(6666)
print(indeks)
print(liczby.pop(indeks))  # 6666
print(liczby)  # [999, 687, 54, 22, 12.34]

# usuniecie po elemencie
liczby.remove(54)
print(liczby)  # [999, 687, 22, 12.34]

print(len(liczby))  # 4

krotka = tuple(liczby)
print(krotka)  # (999, 687, 22, 12.34)
print(type(krotka))  # <class 'tuple'>
