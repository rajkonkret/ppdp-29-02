import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    print(dialect.delimiter, dialect.quotechar, dialect.escapechar)
    file.seek(0)  # ustawienie odczytu ponownie na początek pliku
    # csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x00000236386D1C00>

    fields = next(csvreader)
    for row in csvreader:
        # print(row
        rows.append(row)

print(fields)
print(rows)
# [['radek', 'coe', '3', '9'],
#  ['tomek', 'cos', '2', '9.1'],
#  ['marek', 'cot', '1', '0.8'],
#  ['asia', 'coa', '3', '0']]
# , " None
# <_csv.reader object at 0x00000187BF2311E0>
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'coe', '3', '9'], ['tomek', 'cos', '2', '9.1'], ['marek', 'cot', '1', '0.8'], ['asia', 'coa', '3', '0']]
#
# Process finished with exit code 0
