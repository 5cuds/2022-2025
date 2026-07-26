print("Welcome to the Python guess the line")
print("Guess the line correctly and your win!")
print("You have three trys!")

count = 0
limit = 3

while count < limit:
    print("==============\nI feel sooo ____")
    user_1 = input("Enter here: ").lower().strip()
    if user_1 == "good":
        print("==============\nI feel soo good\nCorrect!")
        while count < limit:
            print("==============\nWhat the ____")
            user_2 = input("Enter here: ").strip().lower()
            if user_2 == 'flip':
                print("==============\nWhat the flip\nCorrect!")
                while count < limit:
                    print("==============\nJoe ____")
                    user_3 = input("Enter here: ").lower().strip()
                    if user_3 == "mama":
                        print("==============\nJoe mama\nCorrect!")
                        while count < limit:
                            print("==============\nWow that was so ____")
                            user_4 = input("Enter here: ").lower().strip()
                            if user_4 == "cool":
                                print("==============\nWow that was so cool\nCorrect!")
                                while count < limit:
                                    print("==============\nOh ___")
                                    user_5 = input("Enter here: ").lower().strip()
                                    if user_5 == 'man':
                                        print("==============\nOh man\nCorrect!\n==============")
                                        print("You Won!")
                                        exit()
                                    else:
                                        print("Incorrect")
                                        count += 1
                            else:
                                print("Incorrect")
                                count += 1
                    else:
                        print("Incorrect")
                        count += 1
            else:
                print("Incorrect")
                count += 1

    else:
        print("Incorrect")
        count += 1

    if count == 3:
        print("==============\nYou Lose!")
        exit()

