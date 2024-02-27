# match case
# python 3.10
lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case 'java':
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:  # default
        print("Nie znam takiego języka")

print(lista)
