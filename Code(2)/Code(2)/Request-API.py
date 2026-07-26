import requests


def status(msg):
    url = "https://pokeapi.co/api/v2/"
    full_url = f"{url}/pokemon/{msg}"

    bals = requests.get(full_url)

    if bals.status_code == 200:
        data = bals.json()
        return data

    else:
        print("404 Not found")


user_input = input("Enter the name of the Pokémon: ").lower().strip()
print("==================")

base_stat = status(user_input)

print(f"Name: {base_stat["name"].capitalize()}\nID: {base_stat["id"]}\nHeight: {base_stat["height"]}")
print(f"Weight: {base_stat["weight"]}")
