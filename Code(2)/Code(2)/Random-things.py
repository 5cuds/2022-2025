import time
import threading


def timer():
    count = 100

    while True:
        if count == 0:
            break
        else:
            count -= 1
            time.sleep(1)
            print(f"Count: {count}")


x = threading.Thread(target=timer, daemon=True)
x.start()

user_input = input("> ")