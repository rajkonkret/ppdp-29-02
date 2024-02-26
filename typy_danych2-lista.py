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


