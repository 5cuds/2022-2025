capitals = {
    "USA": "Washington d.c.",
    "India": "New delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

while True:
    correct = 0
    incorrect = 0

    for c, cap in capitals.items():
        print(f"What's the Capital of {c}")
        print("==============")
        for i, element in enumerate(capitals.values(), start=1):
            print(f"{i}){element}")
        user_input = input("==============\nEnter here: ").capitalize().strip()
        if user_input == cap:
            print("Correct!\n==============")
            correct += 1
        else:
            print("Incorrect\n==============")
            incorrect += 1
    print(f"Correct answers: {correct}\nIncorrect answers: {incorrect}")
    break
