a = 10
b = 10


def dodaj():
    # zmienne lokalne
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # jako a uzywa wewnatrz funkcji globalnej zmiennej a, zmieni jej wartość globalnie
    a = 6
    b = 8
    print(a + b)


print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 10
# funkcja ma LOKALNE zmienne a=6, b=7, wykona działanie dla tych parametrów
dodaj()  # 13
# mimo tych samych nazw nie zmienia się wartośc zmiennej globalnej
print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 10
# ta funkcja użyje waertości globalnych, nie ma zmiennych lokalnych
dodaj2()  # 10
print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 10
dodaj3()  # 14
print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 6
