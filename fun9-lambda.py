# funkcja lambda
# skrócony zapis funkcji
# funkcja anonimowa
# mozliwosc deklaracji w miejscu wykonania funkcji
from functools import reduce


def odejmij2(a, b):
    return a - b


print(odejmij2(5, 6))

odejmij = lambda a, b: a - b  # return - lambda zwraca wynik
print(odejmij(4, 5))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(10))
print(wiek(17))
print(wiek(18))
print(wiek(25))
# -1
# -1
# 1230.0
# 1080.0
# dziecko
# nastolatek
# nastolatek
# dorosły
# dorosły

lista = [1, 2, 3, 4, 24, 45, 50, 100, 500]

l = []
for i in lista:
    l.append(i * 2)

print(l)  # m[2, 4, 6, 8, 48, 90, 100, 200, 1000]
print([i * 2 for i in lista])  # [2, 4, 6, 8, 48, 90, 100, 200, 1000]
print(i * 2 for i in lista)  # <generator object <genexpr> at 0x00000213FC7836B0>


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 48, 90, 100, 200, 1000]
# funkcje wyzszego rzędu

# map() - pobiera elemnt z kolekcji, wykonuje podana funkcję na nim
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 48, 90, 100, 200, 1000]

# zastosowanie lambdy jako funkcji anonimowej, wykonanie w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 48, 90, 100, 200, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map(): [4, 8, 12, 16, 96, 180, 200, 400, 2000]

# filtrowanie danch
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)

print(l3)  # [1, 2]

# filter() - pobiera elemnt z kolekcji, sprawdza wg warunku zadanego funkcja i zwraca spełniający waunek
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1, 2]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 20, lista))}")
# Zastosowanie filter: [24, 45, 50, 100, 500]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3 and x < 50, lista))}")
# Zastosowanie filter: [4, 24, 45]
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 50, lista))}")
# Zastosowanie filter: [4, 24, 45]


# reduce()
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).
lista_reduce = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, lista_reduce))  # 15
# 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
print(reduce(lambda a, b: a * b, lista_reduce))  # 120
# 10:40
