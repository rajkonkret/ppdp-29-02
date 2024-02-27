# funkcja - wydzielony blok kodu
# mozliwosc wywołania w dowolnej chwili
# mozliwosc uruchamiania wielokrotnie
# funkcja jest deklarowana. nie wykonuje się w miejscu deklaracji
# wykonuje się w miejscu wywołania funkcji
a = 4
b = 8


# deklarcja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a: int, b):  # funkcja ma obowiązkowe dwa argumenty
    print(a + b)


def dodaj3(a, b, c=0):  # z argumentem domyslnym
    print(a + b + c)


def odejmij(a, b, c=0):
    print(a - b - c)


dodaj()  # 12
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# argumenty pozycyjne (brane do funkcji wg pozycji)
dodaj2(5, 4)  # 9

dodaj3(1, 2, 3)  # 6
dodaj3(1, 2)  # 3
odejmij(1, 2, 3)  # -4
# parametry nazwane (brane wg nazwy argumentu)
odejmij(c=3, a=1, b=2)  # -4
odejmij(7, c=8, b=9)  # -10 mieszane, pozycyjny musi byc przed nazwanymi
print(a, b)  # 4 8 wartoscci zmiennych globalnych nie sa zmieniane wewnątrz funkcji
