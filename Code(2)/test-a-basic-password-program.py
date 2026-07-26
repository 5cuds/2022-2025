import time


def password1():
    print("      (Discord.com)")
    print("(---------Login---------)")
    while True:
        username = input("Username: ").lower()
        password = input("Password: ").lower()
        use = "justnars"
        pas = "nars_?!@"

        if username == "justnars" and password == "nars_?!@":
            print("Processing...")
            time.sleep(1)
            print("Login Successful!")
            print("-------------------")
            quit()
        elif username == use and password not in pas:
            print("Processing...")
            time.sleep(1)
            print("Incorrect Password!")
            print("-------------------")

        elif password == pas and username not in use:
            print("Processing...")
            time.sleep(1)
            print("Incorrect username!")
            print("-------------------")
        else:
            print("Processing...")
            time.sleep(1)
            print("Incorrect")
            print("-------------------")
        time.sleep(1)
        c = input("Want to try again? (Yes/No): ").lower()
        if c == "yes":
            password1()
        else:
            exit()


password1()
