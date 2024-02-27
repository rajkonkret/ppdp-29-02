import chardet

# pip install chardet

file_path = 'test.log'
with open(file_path, "rb") as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)  # {'encoding': 'MacRoman', 'confidence': 0.5746808510638298, 'language': ''}
# Po ododaniu dodatkowych szczególnych znaków
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# Dodane
# Dodane
# Dośdane
# Dośdńźąćśane
