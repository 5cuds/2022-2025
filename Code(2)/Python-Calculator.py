print("Welcome To The Python Calculator!")
print("=================================")


def mathcool():
    try:
        user_input = int(input("Number(1): "))
        things = ["-", "+", "*", "%"]
        print(things)

        things_more = input("===============\nOperators: ")
        if things_more not in things:
            print("Enter a valid choice")
            print("============================")
            mathcool()

        user_input1 = int(input("===============\nNumber(2): "))
        print("===============")

        if things_more == "-":
            answer = user_input - user_input1
            printer = f"{user_input} - {user_input1} = {answer}"

        elif things_more == "+":
            answer = user_input + user_input1
            printer = f"{user_input} + {user_input1} = {answer}"

        elif things_more == "*":
            answer = user_input * user_input1
            printer = f"{user_input} * {user_input1} = {answer}"

        elif things_more == "%":
            answer = user_input % user_input1
            printer = f"{user_input} % {user_input1} = {answer}"

        print(printer)
        print("===============")
        mathcool()

    except ValueError:
        print("(ONLY NUMBERS AND OPERATORS)")
        print("=================================")
        mathcool()


mathcool()
