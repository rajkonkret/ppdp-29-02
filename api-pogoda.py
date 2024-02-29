import requests
url =     'http://api.openweathermap.org/data/2.5/'
    'weather?q=Warszawa&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl&units=metric'
page = requests.get()
