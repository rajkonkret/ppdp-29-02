# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# na podstawie warunku wykonywana jest jedna operacja lub druga
# if warunek:
#     instrukcja

odp = False  # fałsz
# odp = True  # prawda

if odp:
    print("Brawo")

print("Dalsza część programu")
# Brawo
# Dalsza część programu

if odp:
    print("Brawo")
else:  # domyslne działąnie
    print("Musisz uczyć sie dalej")
# ctrl / (?) komentarz zaznaczonego kodu
# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek} zł")
# # Dodac podatek 0.2 w przedziale 10000 do 29999

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

# zasymulujemy system logów
# dostaniemy alerty z róznych systemów (console, email)
# alerty mogą miec dodatkowe poziomy błedu (critical, medium, inny)
# standarowy komunikat
# błedy bedziemy zapisywac do listy

lista_bledow = []
alert_system = 'email'
error = 'critical'

error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == "email":
    print("Sytem email")
    # IndentationError: unindent does not match any outer indentation level
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append("inny bład")
else:
    print("Nie znam takiego systemu")

"""
komentarz
wielolinijkowy
"""

print(lista_bledow)
# napisac zadanie przeprowadzające test z historii lub czegokolwiek innego
odp = input("Kiedy zaczęła sie II Wojna Światowa?")
if odp == '1939':  # == - porównanie
    print("Prawidłowo")
else:
    print("Masz w książce na 18 stronie")
