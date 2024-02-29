import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl&units=metric'
page = requests.get(url)
print(page.text)
json = page.json()
print(json)  # 8.83
temp = json['main']['temp']
print(temp)  # 8.83

