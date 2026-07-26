import random

while True:
    a = random.randint(1, 15)

    b = random.randint(1, 15)

    operation=random.choice(["+", "-"])

    if operation == "+":
        correct_answer = a + b
        prompt= f"{a} + {b} = "
    elif operation == "-":
        correct_answer = a - b
        prompt= f"{a} - {b} = "

    c=int(input(prompt))

    if (c == correct_answer) or (correct_answer == 0 and c == 0):
        print("Correct!")
        print("-----------------------")
    else:
        print("Incorrect")
        print("Correct answer was", correct_answer)
        print("-----------------------")
