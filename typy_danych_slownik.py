# słownik - typ danych para klucz - wartość
#  {'user': "Radek", "wiek": 38}
# odpowiednik jsona
dict = {}  # pusty słownik
print(dict)  # {} - pusty słownik
print(type(dict))  # <class 'dict'>

# dodanie elemnetu do slownika
dict['imie'] = "Radek"
print(dict)  # {'imie': 'Radek'}
dict['wiek'] = 39
print(dict)  # {'imie': 'Radek', 'wiek': 39}

# odczytanie wartosci dla klucza w słowniku
print(dict['wiek'])  # 39

print(dict.keys())  # dict_keys(['imie', 'wiek'])
print(dict.values())  # dict_values(['Radek', 39])
print(dict.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)])

dict.update({"date": "12-12-2024"})
print(dict)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2024'}

dictionary = {'x': 2}
print(dictionary)
dictionary.update([('y', 3), ("z", 0)])
print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}

# gdy brak klucza w słownik
# print(dict['wzrost'])  # KeyError: 'wzrost'
print(dict.get('wzrost'))  # None nie ma takiego klucza
print(dict.get('wzrost', 'default'))  # default

# napisac aplikacje słownik
dict_translate = {'imie': 'name', 'kot': 'cat', 'pies': 'dog'}
print(dict_translate['imie'])  # name
# input() - pobieranie danych od użytkownika, zwraca str
key = input("Podaj słowo do przetłumaczenia")
print(dict_translate[key.lower().replace(" ", '')])

a = int(input("Podaj pierwsza liczbę"))
b = input("Podaj drugą liczbę")
print(a + float(b))  # 11.0
