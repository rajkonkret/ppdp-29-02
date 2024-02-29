# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # dziedziczy po klasie B i A
    """
    Klasa C dziedziczy po klasie B i A
    """


class D(A, B):
    """
    Klasa D dziedziczy po klasie A i B
    """

    def method(self):
        super().method()  # dziedziczy po klasie nadrzednej (A)


class E(B, A):
    def method(self):
        print("Metoda z klasy E")


class G(A, B):
    def method(self):
        B.method(self)  # dziedziczy po klasie B - wyraźne wskazanie


class H(A, B):
    def method(self):
        super().method()  # dziedziczy (A)
        B.method(self)  # dziedziczy po klasie B - wyraźne wskazanie
        print("Metoda z klasy H")


a = A()
a.method()

b = B()
b.method()
# Metoda z klasy A
# Metoda z klasy B

c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # Metoda z klasy A

e = E()
e.method()  # Metoda z klasy E

g = G()
g.method()  # Metoda z klasy B

h = H()
h.method()
# Metoda z klasy A
# Metoda z klasy B
# Metoda z klasy H
print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
