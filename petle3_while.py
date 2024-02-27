# while - sterowana warunkiem
licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat!!!!")
    if licznik > 10:
        break  # przerywa bieżącą pętle

print(licznik)  # 11

licznik = 0
while licznik < 10:
    print("komunikat 2!!!")
    licznik += 1

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # ['1', '2', '3', '4', '5']
print(lista2)  # [1, 2, 3, 4, 56, 7, 8, 9]
