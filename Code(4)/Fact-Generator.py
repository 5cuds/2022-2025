import requests
import pyttsx3

def TTS(text):
    talking_thing_somethin_idk = pyttsx3.init()
    talking_thing_somethin_idk.say(text)
    talking_thing_somethin_idk.runAndWait()


def get_useless_func():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        useless_fact = response.json()["text"]
        print(f"Fun Fact: {useless_fact}")
        TTS(useless_fact)
    else:
        print(response.status_code)


if __name__ == "__main__":
    get_useless_func()