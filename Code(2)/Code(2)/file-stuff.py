import os

path = "C:\\Users\\Windows\\Documents\\passwords.txt"
folder = "C:\\Users\\Windows\\Documents\\DON'T OPEN"

if os.path.exists(path):
    print("Your file is in your pc")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.exists(folder):
        print("That is a folder")
else:
    print("that file is not on your pc")

    test = "David i will say this a again i dont give a shit about your kid dying just give me my pay"
    teats2 = "C:\\Users\\Windows\\Documents\\tea.txt"

    with open("C:\\Users\\Windows\\Documents\\tea.txt") as file:
        print(file.read())