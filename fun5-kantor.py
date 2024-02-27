# stworzyc funkcji kantor
# ta funkcja mamiec dwie funkcje wewnetrne eur, usd
# w zaleznnosci od waluty ma nam zwracac odpowiednią funkcje
# funkcje wewnetrne beda przeliczac tylko jeden typ waluty wg ich nazwy

def kantor(waluta):
    print("Uruhomienie kantoru")

    def eur(kwota=0):
        print(f'Wymieniam {kwota} eur. Dostajesz {kwota * 4.30} pln')

    def usd(kwota=0):
        print(f'Wymieniam {kwota} usd. Dostajesz {kwota * 4.07} pln')

    if waluta.lower() == 'eur':
        return eur  # bez nawiasów () - zwracamy tylko adres
    else:
        return usd


kantor_eur = kantor("eur")
kantor_eur(1000)  # Wymieniam 1000 eur. Dostajesz 4300.0 pln

kantor_usd = kantor('usd')
kantor_usd(2500)
