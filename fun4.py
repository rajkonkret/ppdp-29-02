# funkcja zagnieżdzona, funkcja wewnętrzna
# dekorator (@) wykorzystuje mechanizm funkcji zagniezdzonej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    print(fun2)  # <function fun1.<locals>.fun2 at 0x000001A1D48A98A0>
    return fun2  # zwrocenie adresu funkcji


xFun = fun1()  # To jest fun1
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000296026398A0>
print(type(xFun))  # <class 'function'>
# uruchomienie funkcji -> nazwa funkcji i nawiasy okrągłę (ew. parametry)
xFun()  # To jest fun2

