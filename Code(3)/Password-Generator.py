import random

def main():
    try:

        user_input = input("(=====Python Password=====)\nGenerate Password? (Y/N): ").lower().strip()
        if user_input != "y":
            exit()

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ["!", "@", "#", "$", "%", "&", "*", "+", "-", "=", "_", "?"]

        print("\n1)Simple Passwords (Letters, Numbers)\n2)Number Passwords(Numbers)")
        print("3)Complex Passwords (Letters, Numbers, Symbols)\n")

        choice = int(input("Choose Your Password type: "))
        while True:
            long = int(input("\nHow Long Will Your Password Be?: "))
            if long < 5:
                print("Password Must Be 5 Chars Long.")
                continue
            else:
                print(f"\nPassword:", end=" ")

            if choice == 1:

                ff = letters + numbers
                full_password = []

                for i in range(long):

                    password = random.choice(ff)

                    full_password.append(password)
                random.shuffle(full_password)

                for i in full_password:
                    print(i, end="")

            elif choice == 2:

                print(f"\nPassword:", end=" ")
                for i in range(long):
                    print(random.randint(1, 10), end="")

            else:

                ff = letters + numbers + symbols
                full_password = []

                for i in range(long):
                    password = random.choice(ff)

                    full_password.append(password)
                random.shuffle(full_password)
                
                for i in full_password:
                    print(i, end="")
            exit()

    except ValueError as e:
        print(f"Error: {e} ")
        main()

if __name__ == "__main__":
    main()
            