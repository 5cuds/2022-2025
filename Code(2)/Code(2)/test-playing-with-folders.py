import time
import os
while True:
    print("===========================")
    print("1)Send a text\n2)Read a text\n3)Delete all the text\n===========================")
    c = int(input("> "))
    if c == 1:
        print("(---------Send a text---------)")
        commend = input("> ")
        with open("tea.txt", "w") as file:
            print("Sending text...")
            time.sleep(1)
            print("The text has been Sent!")
            file.write(commend)
    elif c == 2:
        print("(---------Read a text---------)")
        with open("tea.txt") as file1:
            print("Loading text...")
            time.sleep(1)
            print(file1.read())
    elif c == 3:
        print("(---------Delete text---------)")
        print("Deleting all of the text...")
        time.sleep(1)
        file_path = "tea.txt"
        if os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")
                print("Deleted all the text!")
    else:
        print("Enter a valid number")
