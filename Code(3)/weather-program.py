import requests


def main():
    try:

        key = "17d678349374714a0cb8702690a57526"
        city = input("======================)\nEnter a name of a ctiy\n>  ")

        link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

        r = requests.get(link)

        if r.status_code == 200:
            data = r.json()
            print(data)

            print(f"======================)\nCity Name: {city.title()}\nCountry: {data['sys']['country']}")
            print("======================)")
            print(f"Temp: {data["main"]["temp"]}")
            print(f"Feels like: {data["main"]["feels_like"]}")
            print(f"Pressure: {data["main"]["pressure"]}")
            print(f"Humidity: {data["main"]["humidity"]}")
            print(f"Temp (MIN): {data["main"]["temp_min"]}\nTemp (MAX): {data["main"]['temp_max']}")

        else:
            print("404 Not Found!")

        main()

    except ValueError:
        print("Error!")
        main()

if __name__ == "__main__":
    main()
