import random  # biblioteka do liczb pseudolosowych

# help(random)  # wypisanie dokumentacji

print(random.randint(1, 100))  # int 1 ..100
print(random.random())  # float 0.. 0,9999999
print(random.random() * 10)  # float 0.. 9,999999
print(random.randrange(7))  # int 0..6
print(random.randrange(1, 100))  # int 1..99

lista = [1, 2, 3, 45, 57, 68, 79]
print(random.choice(lista))

lista_kula = list(range(1, 50))  # 1..49
for i in range(6):
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    print(wyn)

print(random.choices(lista_kula, k=6))  # [39, 21, 23, 2, 2, 31] losuje z powtórzeniami
print(random.sample(lista_kula, 6))
print(random.sample(lista_kula, k=6))  # [44, 30, 29, 47, 31, 15]
