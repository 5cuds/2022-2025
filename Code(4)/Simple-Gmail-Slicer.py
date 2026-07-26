import requests
import random
from winotify import Notification, audio


def main():
    try:
        # Use full image paths or ensure they are in the same directory as your script
        listof_imgs = ["C:\\path\\to\\images\\uuu.webp", "C:\\path\\to\\images\\eee.webp", 
                       "C:\\path\\to\\images\\rrr.png", "C:\\path\\to\\images\\ddd.png", 
                       "C:\\path\\to\\images\\bbb.jfif"]

        # Fetching quote of the day
        req1 = requests.get("https://api.quotable.io/random")

        if req1.status_code == 200:
            data = req1.json()

            # Ensure the response has the expected structure
            if 'contents' in data and 'quotes' in data['contents']:
                quote = data['contents']['quotes'][0]

                # Create the notification
                message = Notification(
                    app_id="Nihal's Quote Generator!",
                    title="Quote Of The Day!",
                    msg=f"{quote['quote']} — {quote['author']}",
                    duration="short",
                    icon=random.choice(listof_imgs)  # Select random image
                )

                # Set the audio for the notification
                message.set_audio(audio.LoopingAlarm3, loop=False)

                # Show the notification
                message.show()

            else:
                print("Unexpected response format from API")

        else:
            print(f"Failed to fetch quote, status code: {req1.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
