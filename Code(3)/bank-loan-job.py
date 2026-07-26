import requests
key = "17d678349374714a0cb8702690a57526"

city = "moscow"

link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

r = requests.get(link).json()
print(r)

# if r.status_code == 200:
    # data = r.json()