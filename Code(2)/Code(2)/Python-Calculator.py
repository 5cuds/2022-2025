print("Welcome To The Python Calculator!\n(Type 911 to quit)")
print("=================================")
while True:
    try:
        user_input = int(input("Number(1): "))

        if user_input == 911:
            print("=================================\nHope you had great using the python calculator!")
            exit()

        things = ["-", "+", "*", "%"]
        print(things)

        things_more = input("===============\nOperators: ")
        if things_more not in things:
            print("Enter a valid choice")
            print("============================")

        user_input1 = int(input("===============\nNumber(2): "))
        print("===============")

        if things_more == "-":
            func = lambda x, y: x - y
        elif things_more == "+":
            func = lambda x, y: x + y
        elif things_more == "*":
            func = lambda x, y: x * y
        elif things_more == "%":
            func = lambda x, y: x % y

        print(f"{user_input} {things_more} {user_input1} = {func(user_input, user_input1)}")
        print("===============")

    except ValueError:
        print("(ONLY NUMBERS AND OPERATORS)")
        print("=================================")
