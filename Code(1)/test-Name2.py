while True:
    command = input("Enter name: ")
    if len(command) < 3:
        print("Name must least 3 characters long.")

    elif len(command) > 50:
        print("Name must be less then 50 characters long.")
    else:
        print("Name lookin' Good")
        break
