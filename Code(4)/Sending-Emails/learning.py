import requests

# API endpoint
url = "https://uselessfacts.jsph.pl/random.json?language=en"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    fact = response.json().get("text")
    print("Random Fact:", fact)
else:
    print("Failed to retrieve fact.")


# API endpoint
url = "https://icanhazdadjoke.com/"

# Make a GET request to the API with headers specifying JSON response
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    joke = response.json().get("joke")
    print("Dad Joke:", joke)
else:
    print("Failed to retrieve joke.")


# Specify the category or get a random joke from any category
url = "https://v2.jokeapi.dev/joke/Any"  # "Any" can be replaced with "Programming", "Miscellaneous", etc.

# Customize to exclude NSFW jokes, etc.
params = {
    "format": "json",
}

response = requests.get(url, params=params)

if response.status_code == 200:
    joke_data = response.json()
    # Some jokes are in two parts (setup and delivery), others are single
    if joke_data["type"] == "twopart":
        print("Joke:", joke_data["setup"])
        print("Punchline:", joke_data["delivery"])
    else:
        print("Joke:", joke_data["joke"])
else:
    print("Failed to retrieve joke.")


print("Hello "+input("Name: ").capitalize())

