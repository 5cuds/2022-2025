import random
import time
import threading

balance = 0.00
love = 50
fun = 75
hunger = 100
cleanliness = 65
foods = ["hamburger", "pizza", "cat food"]


def walk():
    global fun, balance, love, hunger, cleanliness
    print("You took larry on a walk i think she loves it!")
    fun += 40
    balance += 30
    love += 20


def play():
    global fun, balance, love, hunger, cleanliness
    print("You played with larry Look at her. shes having soo much fun!")
    fun += 30
    balance += 30
    love += 30


def toys():
    global fun, balance, love, hunger, cleanliness
    print("You got toys for larry! she's gonna love it!")
    fun += 10
    balance -= 15
    love += 10

def buy():
    global fun, balance, love, hunger, cleanliness, foods

    user_2 = input("Go To Store? (Y/N): ").lower().strip()

    if user_2 == "y":
            
        if foods == []:
            print("It looks like theres nothing left! would you like to buy some food for larry now?")
            love -= 50
            user_yes_no = input("(Y/N): ").lower()
            if user_yes_no == 'y':
                buy()
            else:
                love -= 30
                return
        else:
            print("===========================")
            dict_foods = {
                "Pizza": 4.99,
                "Hamburger": 5,
                "Taco": 3,
                "Hotdog": 4,
                "Cat food": 8.99,
                "Sandwich": 4.66
            }

            cart = []
            total = 0.00

            for food, prices in dict_foods.items():
                time.sleep(0.33)
                print(f"{food} - ${prices}")

            while True:

                print("===========================")
                user_food = input("Add Food to the cart (Show) and (Q = quit): ").capitalize()

                if user_food in dict_foods:
                    print("Added to Cart!")

                    cart.append(user_food)

                    foods.append(user_food)

                    total += dict_foods[user_food]

                elif user_food == "Show":
                    print(cart)

                elif user_food == "Q":
                    print("Things You got!\n", cart)
                    print(f"Total: ${total:.2f}")

                    balance -= total
                    return
                
                else:
                    print("Invalid choice")
                    continue

    else:
        return


def feed():
    global fun, balance, love, hunger, cleanliness

    random_texts = [
        "Larry likes That!",
        f"Larry hates that...",
        f"Larry thinks that is a bit meh but ok",
        f"it's ok.. that's what Larry said...",
        f"Larry LIKES IT SO MUCH!!"
    ]
    printer = random.choice(random_texts)

    open_or_nah = input("Open fridge? (Y/N): ").upper().strip()
    if open_or_nah == "Y":
        print("(===========FRIDGE===========)")
        for i in foods:
            time.sleep(0.33)
            print(i)
        user_1 = input("What Would you like to feed larry?: ").lower().strip()
        if user_1 in foods:
            foods.remove(user_1)
            print(f"Successfully fed Larry {user_1}\n{printer}")
            if user_1 == "pizza":
                hunger += 20
            elif user_1 == "hamburger":
                hunger += 50
            elif user_1 == "taco":
                hunger += 30
            elif user_1 == "hotdog":
                hunger += 20
            elif user_1 == "sandwich":
                hunger += 30
        else:
            return


def open_fridge():
    user_fridge = input("Open fridge(Y/N)?: ").lower().strip()
    if user_fridge == 'y':
        print("(===========FRIDGE===========)")
        for i in foods:
            time.sleep(0.33)
            print(f"|{i}")
    else:
        return


def vet():
    global fun, balance, love, hunger, cleanliness
    print("You took larry to the vet not sure why you needed to do that but ok.")
    love -= 20
    fun -= 50
    cleanliness += 10
    balance -= 20


def bath():
    global fun, balance, love, hunger, cleanliness
    print("You took Larry to a bath!")
    love += 20
    fun += 10
    cleanliness += 40


def pool():
    global fun, balance, love, hunger, cleanliness
    print("You took Larry to the pool she didn't really like it..")
    cleanliness += 50
    fun -= 30


def timer():
    global fun, balance, love, hunger, cleanliness
    while True:
        if fun == 0:
            print("Larry died of boredom...\nGame over!")
            exit()
        elif hunger == 0:
            print("Larry died of low levels of hunger..\nGame over!")
            exit()
        elif cleanliness == 0:
            print("Great Larry got sick EDIT: larry has died of ligma...\nGame over!")
            exit()
        else:
            time.sleep(5)
            fun -= 1
            time.sleep(7)
            hunger -= 1
            time.sleep(5)
            cleanliness -= 1


def main():
    print("This is Larry. She's your python cat! Take good care of him!🐱")
    print("There are many things you can do with him! Like take him for a walk, feed him, and etc..")
    print("Give her some love <3")
    threading.Thread(target=timer).start()
    while True:
        try:
            print("=======================")
            print("1)Fun\n2)Hunger\n3)Cleanliness\n4)Status\n5)Exit\n=======================")
            user_input = int(input("> "))

            if user_input == 1:
                print("1)Walk\n2)Play\n3)Buy some toys\n4)Back to main menu\n=======================")
                user_1 = int(input("> "))
                if user_1 == 1:
                    walk()
                elif user_1 == 2:
                    play()
                elif user_1 == 3:
                    buy()
                else:
                    main()
            elif user_input == 2:
                print("1)Feed\n2)Buy Food\n3)Open fridge\n4)Back to main menu\n=======================")
                user_2 = int(input('> '))
                if user_2 == 1:
                    feed()
                elif user_2 == 2:
                    buy()
                elif user_2 == 3:
                    open_fridge()
                else:
                    main()
            elif user_input == 3:
                print("1)Bath\n2)Pool\n3)Vet\n4)Back to main menu\n=======================")
                user_3 = int(input("> "))
                if user_3 == 1:
                    bath()
                elif user_3 == 2:
                    pool()
                elif user_3 == 3:
                    vet()
                else:
                    main()
            elif user_input == 4:
                print(f"Fun: {fun}\nHunger: {hunger}\nCleanliness: {cleanliness}\nLove: {love}\nBalance: ${balance}")
            else:
                print("Hope you had a Great time taking care of larry!\nGoodbye!")

        except ValueError:
            print("Error!")


if __name__ == '__main__':
    main()
