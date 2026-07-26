import random
import time


class Math:

    correct_answers = 0
    incorrect_answer = 0

    corn = 0
    incorn = 0

    count = 0
    random_limit = random.randint(5, 10)
    limit = random_limit

    def random_math(self):
        print("Welcome to the Python Random Math Problems\nTry to enter the correct answer and you will get points!")
        print("For every correct answers Good luck! (911 to quit)")
        print("(-----Difficulty-----)\n1)Easy mode [1 - 25] [+ -]\n2)Medium mode [1 - 50] [+ - *]")
        print("3)Hard mode [1 - 75] [+ - * %]")
        user_choice = input("> ").strip().lower()
        print("--------------")
        while True:
            try:

                if user_choice == "1":
                    a = random.randint(1, 25)
                    b = random.randint(1, 25)
                    random_syms = ["+", "-"]
                elif user_choice == "2":
                    a = random.randint(1, 50)
                    b = random.randint(1, 50)
                    random_syms = ["+", "-", "*"]
                else:
                    a = random.randint(1, 75)
                    b = random.randint(1, 75)
                    random_syms = ["+", "-", "*", "%"]
                random_sym = random.choice(random_syms)

                if random_sym == "+":
                    correct = a + b
                    printer = f"{a} + {b} = "
                elif random_sym == "-":
                    correct = a - b
                    printer = f"{a} - {b} = "
                elif random_sym == "%":
                    correct = a % b
                    printer = f"{a} % {b} = "
                elif random_sym == "*":
                    correct = a * b
                    printer = f"{a} * {b} = "

                user_answer = int(input(printer))

                if user_answer == correct:
                    print("Correct!\n--------------")
                    self.correct_answers += 1
                elif user_answer == 911:
                    total = self.correct_answers + self.incorrect_answer
                    print(f"Correct answers: {self.correct_answers}\nIncorrect answers: {self.incorrect_answer}")
                    print(f"Total: {total}")
                    main()
                else:
                    print(f"Incorrect.. correct answer was {correct}\n--------------")
                    self.incorrect_answer += 1

            except ValueError:
                print("Only enter Numbers!\n--------------")

    def think(self):
        print("(----911 to Quit----)")
        try:
            while True:
                a = random.randint(1, 25)
                b = random.randint(1, 25)
                random_sym = random.choice(["+", "-", "%", "*"])
                if random_sym == "+":
                    correct_1 = a + b
                    print1 = f"{a} + ? = {correct_1}"
                elif random_sym == "-":
                    correct_1 = a - b
                    print1 = f"{a} - ? = {correct_1}"
                elif random_sym == "%":
                    correct_1 = a % b
                    print1 = f"{a} % ? = {correct_1}"
                elif random_sym == "*":
                    correct_1 = a * b
                    print1 = f"{a} * ? = {correct_1}"

                print(print1)
                user_7 = int(input("> "))
                if user_7 == b:
                    print("Correct!\n--------------")
                    self.corn += 1
                elif user_7 == 911:
                    total = self.corn + self.incorn
                    print(f"Correct answers: {self.corn}\nIncorrect answers: {self.incorn}\nTotal: {total}")
                    main()
                else:
                    print(f"Incorrect correct answer was {b}\n--------------")
                    self.incorn += 1
        except ValueError:
            print("Enter a valid choice")

    def guess(self):
        print("==========================================")
        print("Welcome to the Python Number Guessing Game!\nHere you have to GUESS a random number!")
        print("And you have a random amount of trys\nGood luck!\n=====================")

        print("(-----Difficulty-----)\n1)Easy mode [1 - 20] \n2)Medium mode [1 - 50]\n3)Hard mode [1 - 100]")
        difficulty_level = int(input("> "))
        if difficulty_level == 1:
            b_number = 20
            random_number = random.randint(1, 20)
        elif difficulty_level == 2:
            random_number = random.randint(1, 50)
            b_number = 50
        else:
            random_number = random.randint(1, 100)
            b_number = 100

        print(f"You have {self.limit} trys")

        while self.count < self.limit:
            try:
                user_input = int(input("===============\nGuess the number: "))

                if self.count == self.limit:
                    print(f"Correct number was {random_number}")
                elif user_input > b_number:
                    print("Choice out of range!")
                    continue

                if user_input == random_number:
                    print(f"Correct! {random_number} was the correct answer!")
                    break
                else:
                    print("Incorrect try again..")
                    if user_input > random_number:
                        print("Your Guess is a bit high try a new number!")
                    elif user_input < random_number:
                        print("Your Guess is a bit low try a new number!")
                    self.count += 1

            except ValueError:
                print("Enter a valid choice!")


def calculator():
    print("Welcome To The Python Calculator!\n(Type 911 to quit)")
    print("=================================")
    try:
        while True:
            user_input_ = int(input("Number(1): "))
            if user_input_ == 911:
                main()
            things = ["-", "+", "*", "%"]
            print(things)

            things_more = input("===============\nOperators: ")
            if things_more not in things:
                print("Enter a valid choice")
                print("============================")

            user_input1 = int(input("===============\nNumber(2): "))
            print("===============")

            if things_more == "-":
                printer = lambda x, y: x - y
            elif things_more == "+":
                printer = lambda x, y:  x + y
            elif things_more == "%":
                printer = lambda x, y: x % y
            elif things_more == "*":
                printer = lambda x, y: x * y

            print(f"{user_input_} {things_more} {user_input1} = {printer(user_input_, user_input1)}")
            print("===============")

    except ValueError:
        print("(ONLY NUMBERS AND OPERATORS)")
        print("=================================")


def math_1():
    user_input12 = int(input("Enter a Number: "))
    for i in range(user_input12, 11):
        for b in range(1, 11):
            if i > user_input12:
                main()
            else:
                answer = i + b
                print(f"{i} + {b} = {answer}")


def math_2():
    user_input12 = int(input("Enter a Number: "))
    for i in range(user_input12, 11):
        for b in range(1, 11):
            if i > user_input12:
                main()
            else:
                answer = i - b
                print(f"{i} - {b} = {answer}")


def math_3():
    user_input12 = int(input("Enter a Number: "))
    for i in range(user_input12, 11):
        for b in range(1, 11):
            if i > user_input12:
                main()
            else:
                answer = i * b
                print(f"{i} * {b} = {answer}")


def math_4():
    user_input12 = int(input("Enter a Number: "))
    for i in range(user_input12, 11):
        for b in range(1, 11):
            if i > user_input12:
                main()
            else:
                answer = i % b
                print(f"{i} % {b} = {answer}")


def timer():
    user_input1 = int(input("Enter a Number (Secs): "))
    secs = 0
    secs += user_input1
    print(f"Secs: {secs}")
    for _ in reversed(range(1, secs)):
        time.sleep(1)
        secs -= 1
        print(f"Secs: {secs}")


def main():

    math = Math()
    while True:
        try:
            print("(-----Python Math Program!-----)")
            print("1)Math\n2)Lists\n3)Calculator\n4)Timer\n5)Exit\n--------------")

            user_input = int(input("> "))

            if user_input == 1:
                print("--------------\n1)Random Math Quiz\n2)Incomplete Equations\n3)Guess the Number!")
                print("4)Back to main menu\n--------------")
                user_8 = int(input("> "))

                if user_8 == 1:
                    print("==========================================")
                    math.random_math()
                elif user_8 == 2:
                    print("==========================================")
                    math.think()
                elif user_8 == 3:
                    math.guess()
                elif user_8 == 4:
                    main()
                else:
                    print("Enter a valid choice!")
            elif user_input == 2:
                print("--------------\n1)Plus\n2)Subtraction\n3)Times\n4)Division\n5)Back to main menu\n--------------")
                usr_4 = int(input("> "))
                if usr_4 == 1:
                    math_1()
                elif usr_4 == 2:
                    math_2()
                elif usr_4 == 3:
                    math_3()
                elif usr_4 == 4:
                    math_4()
                elif usr_4 == 5:
                    main()
                else:
                    print("Enter a valid choice!")

            elif user_input == 3:
                calculator()
            elif user_input == 4:
                timer()
            else:
                exit()

        except ValueError:
            print("Enter a valid choice!")


if __name__ == '__main__':
    main()
