# petle - pozwlją wielokrotnie wykonac kod

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
