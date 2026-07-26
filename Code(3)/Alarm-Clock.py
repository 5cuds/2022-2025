import time
import datetime

def clock(set_time):

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Time: {now}", end="\r")

        if now == set_time:
            print("WAKE UP 😴")
            break

        time.sleep(1)

if __name__ == "__main__":
    while True:
        user_input = input("Set an Alarm (HH:MM:SS): ")

        if user_input < datetime.datetime.now().strftime("%H:%M:%S"):
            print("That time has Passed. Try again.")
            continue
        else: clock(user_input)