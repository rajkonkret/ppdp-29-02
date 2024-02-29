import pandas as pd

df = pd.DataFrame(
    {'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
     'wynik': [18, 25, 67]}
)


def sprawdz_wynik(wynik):
    if wynik > 19:
        return 'Zdany'
    else:
        return 'Oblany'


print(df)
df.wynik = df.wynik.apply(sprawdz_wynik)
print(df)
#                   Osoba   wynik
# 0          Michał Jakub  Oblany
# 1              Ewa Noga   Zdany
# 2  Krzysztof Zawierucha   Zdany
