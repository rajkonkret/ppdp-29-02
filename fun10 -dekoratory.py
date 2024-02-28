# dekoratory
# działają na zasadzie funkcji wewnętrznej
def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew  # adres funkcji


@dekor
def hej():
    print("Hej")


@dekor
def dodawanie():
    print(1 + 2)


hej()
dodawanie()
# Dekorujemy
# Hej
# Dekorujemy
# 3
