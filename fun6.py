# napisac funkcje obliczjącą średnią (np.: ocen)
def liczby(name=None, *cyfry):  # * przyjmuje argumenty pozycyjne
    print(cyfry)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    suma = 0
    count = len(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:  # gdy nie było błedu
        print(f"Średnia ocen ucznia {name} wynosi {avg}")
    finally:
        print("Koniec działania")


liczby("Radek", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
liczby("Tomek", 1, 2, 3, 4)
liczby()
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Średnia ocen ucznia Radek wynosi 5.5
# Koniec dizałania
# (1, 2, 3, 4)
# Średnia ocen ucznia Tomek wynosi 2.5
# Koniec dizałania
# ()
# Bład division by zero
# Koniec działania
