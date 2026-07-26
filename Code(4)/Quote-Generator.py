import requests
import random
from winotify import Notification, audio

def main():
    try:
        url = "https://api.forismatic.com/api/1.0/"
        params = {
            'method': 'getQuote',
            'format': 'json',
            'lang': 'en'
        }

        req = requests.get(url, params=params)

        if req.status_code == 200:
            data = req.json()
            listof_imgs = ["eee.webp", "rrr.png", "bbb.jfif"]

            message = Notification(app_id="Nihal's Quote Generator!", title="Quote Of The Day!",
                                        msg=f"{data['quoteText']} — {data['quoteAuthor']}", duration="long",
                                            icon=f"C:\\Users\\Windows\\Documents\\QUO IMAGES\\{random.choice(listof_imgs)}")
            
            message.set_audio(audio.LoopingAlarm3, loop=False)
            message.show()
            
            exit()

        else:
            print(f"Status Error! {req.status_code}")
            exit()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()