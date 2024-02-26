# set (zbiór) - przechowuje niepowtarzające się elementy (unikalne)
# zbior nie zachowuje kolejności przy dodawaniu elementów
# zbiór nie posiada indeksu
lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
print(lista)

zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # pusty zbiór
print(type(zb2))
print(zb2)
# <class 'set'>
# set() - pusty zbiór
# zb3 = {} to nie jest pusty zbior, inny typ

zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # usunie pierwszy element ze zbioru 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # 66
print(zbior.pop())  # 777
print(zbior.pop())  # 11
print(zbior.pop())  # 44
print(zbior)  # {18, 22, 55}

zbior.remove(55)
print(zbior)  # {18, 22}

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}

print(zbior | zbior2)  # suma zbiorów {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior & zbior2)  # część wspólna {18}
print(zbior - zbior2)  # {22}
print(zbior.difference(zbior2))  # {22}
# union zwraca nowy zbior, nie zmienia zbiorów biorących udział w operacji !!!
print(zbior.union(zbior2))  # {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior)  # {18, 22}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}
print("Update")
print(zbior.update(zbior2))  # None
print(zbior)
print(zbior2)
# update zmienia zawartośc zbiorów. zbiory sie zmieniły !!!
# nie zwraca nowego zbioru !!!
# {999, 11, 44, 18, 52, 22, 667, 62}
# {18, 52, 999, 11, 44, 667, 62}
