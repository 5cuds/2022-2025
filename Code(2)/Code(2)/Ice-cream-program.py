import random
import time


class Math:

    correct_answers = 0
    incorrect_answer = 0
    done = 0
    computer_done = 0

    def random_math(self):
        print("Welcome to the Python Random Math Problems\nTry to enter the correct answer and you will get points!")
        print("For every correct answers Good luck!")
        print("(-----Difficulty-----)\n1)Easy mode [1 - 25] \n2)Medium mode [1 - 50]\n3)Hard mode [1 - 75]")
        user_choice = input("> ").strip().lower()
        print("--------------")
        while True:
            try:
                random_sym = random.choice(["+", "-", "%", "*"])

                if user_choice == "1":
                    a = random.randint(1, 25)
                    b = random.randint(1, 25)
                elif user_choice == "2":
                    a = random.randint(1, 50)
                    b = random.randint(1, 50)
                else:
                    a = random.randint(1, 75)
                    b = random.randint(1, 75)

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

    def computer(self):
        print("Welcome to the Python Math mini game you play against a computer!")
        print("And your goal is to WIN against the computer you and the computer\nHave 30 seconds Good luck!")
        print("also forgot to say this you have 10 math problems so do the computer")
        user_start = input("Start (Y/N): ").lower().strip()
        if user_start == "y":
            while True:
                computer_time = random.randint(3, 13)
                for com in range(10):
                    time.sleep(computer_time)
                    print("done")
                    self.computer_done += 1
                    if self.computer_done == 10:
                        print("The Computer has won!\nBetter luck next time")
                    else:

                        a_number = random.randint(1, 30)
                        b_number = random.randint(1, 30)
                        random_things_at_this_point_im_just_bored = random.choice(["+", "-", "*"])

                        if random_things_at_this_point_im_just_bored == "+":
                            correc = a_number + b_number
                            printe = f"{a_number} + {b_number} = "
                        elif random_things_at_this_point_im_just_bored == "-":
                            correc = a_number - b_number
                            printe = f"{a_number} - {b_number} = "
                        elif random_things_at_this_point_im_just_bored == "*":
                            correc = a_number * b_number
                            printe = f"{a_number} * {b_number} = "

                        user_3 = int(input(printe))
                        if user_3 == correc:
                            print("Correct!")
                            self.done += 1
                        elif self.done == 10:
                            print("You WON!")
                        else:
                            print("Incorrect..")

        else:
            main()


def math_1():
    user_input = int(input("Enter a Number: "))
    for i in range(user_input, 11):
        for b in range(1, 11):
            if i > user_input:
                main()
            else:
                answer = i + b
                print(f"{i} + {b} = {answer}")


def math_2():

    user_input = int(input("Enter a Number: "))
    for i in range(user_input, 11):
        for b in range(1, 11):
            if i > user_input:
                main()
            else:
                answer = i - b
                print(f"{i} - {b} = {answer}")


def math_3():
    user_input = int(input("Enter a Number: "))
    for i in range(user_input, 11):
        for b in range(1, 11):
            if i > user_input:
                main()
            else:
                answer = i - b
                print(f"{i} - {b} = {answer}")


def math_4():
    user_input = int(input("Enter a Number: "))
    for i in range(user_input, 11):
        for b in range(1, 11):
            if i > user_input:
                main()
            else:
                answer = i - b
                print(f"{i} - {b} = {answer}")


def main():
    math = Math()
    math.computer()


if __name__ == '__main__':
    main()
