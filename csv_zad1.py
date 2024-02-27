# csv - dane oddzielone znakiem odziału (,; spacja, tab)
# Zenek, Marek, Tomek

import csv

# biblioteka do pracy z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

dictionary = dict(zip(fields, row))
print(dictionary)

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '9'},
    {'name': 'tomek', 'branch': 'cos', 'year': '2', 'cgpa': '9.1'},
    {'name': 'marek', 'branch': 'cot', 'year': '1', 'cgpa': '0.8'},
    {'name': 'asia', 'branch': 'coa', 'year': '3', 'cgpa': '0'},

]
filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    # proste uzycie, zapis wiersz po wierszu
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    # zapisanie danych ze słownika
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=';')
    csvwriter.writeheader()
    # zapisanie pojedynczego wiersza
    # csvwriter.writerow(dictionary)
    # zapisanie wielu wierszy z listy słowników
    csvwriter.writerows(dict_list)

# newline='' - ominięcie pustych linii
# delimiter= ";" wskazanie znaku oddzielającego dane
