import random
print("Welcome To The Basic Math Program!\n(Type 69 to quit)")
print("-----------------------")

correct = 0
incorrect = 0

while True:
    try:
        a = random.randint(1, 25)
        b = random.randint(1, 25)
        operation = random.choice(["+", "-"])

        if operation == "+":
            correct_answer = a + b
            prompt = f"{a} + {b} = "
        elif operation == "-":
            correct_answer = a - b
            prompt = f"{a} - {b} = "

        user_input = int(input(prompt))

        if user_input == correct_answer:
            print("Correct!")
            print("-----------------------")
            correct += 1
        elif user_input == 69:
            total = correct + incorrect
            print("-----------------------")
            print(f"(-----YOUR SCORE-----)\nCorrect answers: {correct}\nIncorrect answers: {incorrect}\nTotal: {total}")
            break
        else:
            print("Incorrect")
            print("Correct answer was", correct_answer)
            print("-----------------------")
            incorrect += 1

    except ValueError:
        print("Enter a Valid number\n-----------------------")
