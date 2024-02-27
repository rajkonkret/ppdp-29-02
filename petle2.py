dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# zwraca klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)
# imie
# nazwisko
# imie
# nazwisko

# zwraca wartośći
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# zwraca pary
for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, "=>", v)
# nazwisko => Kowalski

dictionary2 = {'name': 'imie', "comapany": 'Company'}
print(dictionary2)  # {'name': 'imie', 'comapany': 'Company'}
print({value: key for key, value in dictionary2.items()})
# {'imie': 'name', 'Company': 'comapany'}

d2 = {}
for k, v in dictionary2.items():
    d2[v] = k
print(d2)  # {'imie': 'name', 'Company': 'comapany'}
