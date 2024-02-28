numbers = [1, 2, 3, 4, 5]

# tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")  # Squared: [1, 4, 9, 16, 25]

# filtrowanie listy
even_number = [num for num in numbers if num % 2 == 0]
print(f"Even: {even_number}")  # Even: [2, 4]

# modyfikacja w zależności od warunku
modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"Zmodyfikowane: {modifed_numbers}")  # Zmodyfikowane: [1, 4, 3, 8, 5]

# parzysta - nieparzysta
even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(f"Even - Odd: {even_odd}")  # Even - Odd: ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

#
squared_numbers = [x ** 2 for x in range(1, 6)]
print(f"Kwadraty liczb z  zakresu {squared_numbers}")  # Kwadraty liczb z  zakresu [1, 4, 9, 16, 25]

# abs() - wartośc bezwzględna
number2 = [-1, -2, 3, -4, 5]
absolute = [abs(x) for x in number2]
print(f"Wartości absolutne: {absolute}")  # Wartości absolutne: [1, 2, 3, 4, 5]

word = "Python"
letters = [letter for letter in word]
print(f"Literki: {letters}")  # Literki: ['P', 'y', 't', 'h', 'o', 'n']

# rozpakowanie sekwencji
print(list(word))  # ['P', 'y', 't', 'h', 'o', 'n']

lista1 = [word]
print(lista1)  # ['Python']
