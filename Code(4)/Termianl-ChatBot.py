import google.generativeai as genai
import pyttsx3


def TTS(text):
    """This func mades the voice"""
    talking_thing_somethin_idk = pyttsx3.init()
    talking_thing_somethin_idk.say(text)
    talking_thing_somethin_idk.runAndWait()


def command(message):
    genai.configure(api_key='AIzaSyAxbJdBKwpbJm58Ff6q8KFnO45A54Qb9Rk')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    print(f"Gemini: {response.text}\n")
    TTS(str(response.text).strip("*"))


def main():
    print("Python Gemini API Termianl Bot!\nEnter 'CTP' to close the program.\n")
    while True:
        user_input = str(input("You: ")).lower()
        match user_input:
            case "ctp":
                break
            case _:
                command(user_input)

if __name__ == "__main__":
    main()

    