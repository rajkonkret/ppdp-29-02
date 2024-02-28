def allparams(a, b, /, c=42, d=256):
    print("a, b", a, b)
    print("c, d", c, d)


def allparams2(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


# ile minimum arg?
allparams(1, 2)
# jak dolożyc c?
allparams(1, 2, 3)
allparams(1, 2, c=3)  # a i b -  positional-only
# allparams(b=4,a=7,c=8)
# TypeError: allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
# a i b -  positional-only  - moga byc tylko pozycyjnie przekazane
# / - oddziela arumenty ktore musza byc przekazene pozycyjnie od argumentów,
# które mogą byc przekazane pozycyjnie lub po nazwie
allparams(1, 2, d=7, c=0)  # c, d 0 7

print("------")
allparams2(1, 2, 3)
allparams2(1, 2, c=8)
allparams2(1, 2, c=8, d=0)  # c, d 8 0
# d przekazujemy po nazwie, bo jest po *args
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, d=90)
# args (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# jesli chcemy przekazac do argsów wartosci, c musi byc po pozycji
# allparams2(1, 2, c=3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, d=90)  # SyntaxError: positional argument follows keyword argument

allparams2(1, 2, 3, 4, 5, 6, d=90, name="Radek")  # kwargs {'name': 'Radek'}
allparams2(1, 2, 3, 4, 5, 6, d=90, name="Radek", a=10, nazwa_uzytkownika="Radek")
# kwargs {'name': 'Radek', 'a': 10, 'nazwa_uzytkownika': 'Radek'}

d2 = {}
d2['nazwa uzytkownika'] = "Radek"
print(d2)  # {'nazwa uzytkownika': 'Radek'}
