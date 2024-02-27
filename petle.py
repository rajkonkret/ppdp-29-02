# petle - pozwlją wielokrotnie wykonac kod
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    pass
    # print(_)

for i in range(10):
    print(i * 2)

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)
# 11:30

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']

for p in imiona:
    print(p)
# Radek
# Asia
# Zbyszek
# Marcin

# wyswietlic te elemnty razem z indeksem
# 0 Radek...
licznik = 0
for p in imiona:
    print(licznik, p)
    licznik += 1
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

# enumerate() - numeruje kolekcje i zwraca indeks i element
for p in enumerate(imiona):
    print(p)

# (0, 'Radek')
# (1, 'Asia')
# (2, 'Zbyszek')
# (3, 'Marcin')

for p, w in enumerate(imiona):
    print(p, w)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin
#   sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for p, w in enumerate(imiona):
    print(p, w, sep=":")
# 0:Radek
# 1:Asia
# 2:Zbyszek
# 3:Marcin
for p, w in enumerate(imiona):
    print(p, w, sep=":", end=" ")
# 0:Radek 1:Asia 2:Zbyszek 3:Marcin
print('Tekst')
print('Tekst2')
# 0:Radek 1:Asia 2:Zbyszek 3:Marcin Tekst
# Tekst2

# ludzie = ['Radek', 'Zenek', 'Asia', 'Tomek']
ludzie = ['Radek', 'Zenek', 'Asia', 'Tomek', 'Jarek']  # IndexError: list index out of range
wiek = [47, 67, 34, 32]
# Radek 47
# 0 Radek 47

# for i in range(len(ludzie)):
#     print(ludzie[i], wiek[i])
# # Radek 47
# # Zenek 67
# # Asia 34
# # Tomek 32
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])
# 0 Radek 47
# 1 Zenek 67
# 2 Asia 34
# 3 Tomek 32

# zip() - łaczenie kolekcji w jedną
for p in zip(ludzie, wiek):
    print(p)
# ('Radek', 47)
# ('Zenek', 67)
# ('Asia', 34)
# ('Tomek', 32)
for o, w in zip(ludzie, wiek):
    print(o, w)
# Radek 47
# Zenek 67
# Asia 34
# Tomek 32
for o in enumerate(zip(ludzie, wiek)):
    print(o)  # (3, ('Tomek', 32))
a, b = (3, ('Tomek', 32))
print(a, b)  # 3 ('Tomek', 32)
c, d = b
print(a, c, d)  # 3 Tomek 32
for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)
# 0 Radek 47
# 1 Zenek 67
# 2 Asia 34
# 3 Tomek 32

zipped = zip_longest(ludzie, wiek, fillvalue='Nan')
print(zipped)  # <itertools.zip_longest object at 0x0000024F86F8D5D0>
zipped_list = list(zipped)  # wysyci generator
for item in zipped_list:
    print(item)
# ('Radek', 47)
# ('Zenek', 67)
# ('Asia', 34)
# ('Tomek', 32)
# ('Jarek', 'Nan')
print("------")
for item in zipped_list:
    print(item)
# <itertools.zip_longest object at 0x0000027636EDD5D0>
# ('Radek', 47)
# ('Zenek', 67)
# ('Asia', 34)
# ('Tomek', 32)
# ('Jarek', 'Nan')
# ------
# ('Radek', 47)
# ('Zenek', 67)
# ('Asia', 34)
# ('Tomek', 32)
# ('Jarek', 'Nan')

for i in range(0, 10, 2):  # start, stop, step (krok)
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -1):  # ujemny krok, petla do tyłu
    print(i)
print("------")
for i in range(10, 0, 1):  # źle ustawione parametry. Pętla się nie wykona
    print(i)
