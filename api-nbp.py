# REST API
# Interfejsy API są najpopularniejszym sposobem interakcji programów i urządzeń
# w nowoczesnych technologiach obliczeniowych.
# API to zestaw reguł opisujących,
# jak jeden program może się łączyć oraz komunikować z innym.
# Jak sama nazwa wskazuje, API REST przekazuje na każde żądanie stan każdej transakcji,
# co daje korzyści związane z opracowaniem, wydajnością i zasobami
# json, xml
# metody html
# get, post, delete, patch/put, head, [options, trace, connect]

# Działanie	Instrukcja SQL	HTTP	            DDS
# Create	        INSERT	PUT / POST	        write
# Read (Retrieve)	SELECT	GET	                read / take
# Update	        UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	DELETE	            dispose
import requests as re

# url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = re.get(url)
print(response.status_code)  # 200
print(response)  # <Response [200]>
# 2xx - Success
# 3xx - Redirect - przekierownia
# 4xx - Client Error - 404 - brak zasobu, 400 Bad Request - nieprawidłowe parametry, 401 - błąd autoryzacji
print(response.text)
data = response.json()
print(data)
print(type(data))  # <class 'dict'>

# wypisac wszystkie klucze
# wypisac walute
# wypisac kurs
for k in data.keys():
    print(k)
# table
# currency
# code
# rates
print(f"Waluta: {data['currency']}")
mid = data['rates'][0]['mid']
print(f"Kurs: {mid}")
# Waluta: euro
# Kurs: 4.3116
# 11:25
# 12:00
