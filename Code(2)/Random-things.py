import random
# import time


class Larry:

    hungry = 50
    fun = 70
    balance = 40.0
    love = 69
    clean = 20
    foods = ["pizza", "hamburger", "taco", "cat food", "hotdog", "sandwich"]

    def walk(self):
        print("You took Larry on a walk. I think she loves it!")
        self.fun += 40
        self.balance += 20
        self.love += 10
        self.clean -= 30

    def play(self):
        print("You played with Larry. Look at her she's having so much fun!")
        self.fun += 60
        self.balance += 15
        self.love += 50
        self.clean -= 20

    def toys(self):
        print("You got toys for Larry. Larry is having so much fun!")
        self.fun += 20
        self.balance += 12
        self.love += 20

    def buy(self):
        user_2 = input("Go To Store? (Y/N): ").lower().strip()
        if user_2 == "y":
            dict_foods = {
                "pizza": 4.99,
                "hamburger": 5,
                "taco": 3,
                "hotdog": 4,
                "cat food": 8.99,
                "sandwich": 4.66
            }
            cart = []
            total = 0.00
            for food, prices in dict_foods.items():
                print(f"{food} - ${prices}")
            while True:
                print("===========================")
                user_food = input("Add Food to the cart (Show) and (Q = quit): ").lower().strip()
                if user_food in dict_foods:
                    print("Added to Cart!")
                    cart.append(user_food)
                    self.foods.append(user_food)

                    total += dict_foods[user_food]

                elif user_food == "show":
                    print(cart)
                elif user_food == "q":
                    print("Things You got!\n", cart)
                    print(f"Total: ${total:.2f}")
                    print("==================================")
                    if self.balance < total:
                        print("insufficient funds")
                        exit()
                    else:
                        self.balance -= total
                        main()

                elif user_food not in dict_foods:
                    print("Invalid choice")

    def feed(self):
        open_or_nah = input("Open fridge? (Y/N): ").upper().strip()
        if open_or_nah == "Y":
            for i in self.foods:
                print(i)
            user_1 = input("=================\nWhat Would you like to feed larry?: ").lower().strip()
            random_texts = [
                "Larry likes That!",
                "Larry hates that...",
                "Larry thinks that is a bit meh but ok",
                "it's ok.. that's what Larry said...",
                "Larry LIKES IT SO MUCH!!"
            ]
            printer = random.choice(random_texts)
            if user_1 in self.foods:
                self.foods.remove(user_1)
                print(f"Successfully fed Larry {user_1}")
                print(printer)
                if user_1 == "pizza":
                    self.hungry += 20
                elif user_1 == "hamburger":
                    self.hungry += 50
                elif user_1 == "taco":
                    self.hungry += 15
                elif user_1 == "cat food":
                    self.hungry += 30
                elif user_1 == "hotdog":
                    self.hungry += 20
                elif user_1 == "sandwich":
                    self.hungry += 30
                main()
        else:
            main()

    def open_fridge(self):
        user_fridge = input("Open fridge(Y/N)?: ").lower().strip()
        if user_fridge == 'y':
            print("(--------Fridge--------)")
            for i in self.foods:
                print("|", i)
        else:
            main()

    def bath(self):
        print("You took larry to a bath! he's lovin' it")
        print("Clean | + 40\nLove | 20\nBalance | 0")
        self.clean += 40
        self.love += 20

    def pool(self):
        print("You took Larry to the pool")
        print("Clean | + 50\nLove | 40\nBalance | 0")
        self.clean += 50
        self.love += 40

    def vet(self):
        print("You took larry to the vet! not sure why you needed to do that but ok")
        print("Clean | + 20\nLove | 0\nBalance | - 20")
        self.clean += 20
        self.love += 0
        self.balance -= 20


def main():

    larry = Larry()

    print("1)Clean\n2)Fun\n3)Hungry\n4)Status")
    print("==================================")
    user_input = int(input("Enter your choice: "))
    # CLEANLINESS
    if user_input == 1:
        while True:
            print("==================================")
            user_clean = int(input("1)Bath\n2)Pool\n3)Vet\n4)Back to Main Menu\n> "))
            print("==================================")
            if user_clean == 1:
                larry.bath()
            elif user_clean == 2:
                larry.pool()
            elif user_clean == 3:
                larry.vet()
            elif user_clean == 4:
                main()
            else:
                print("Invalid choice")
    # FUN
    elif user_input == 2:
        while True:
            user_fun = int(input("1)Walk\n2)PLay\n3)Buy toys\n4)Back to Main Menu\n> "))
            print("==================================")
            if user_fun == 1:
                larry.walk()
            elif user_fun == 2:
                larry.play()
            elif user_fun == 3:
                larry.toys()
            elif user_fun == 4:
                main()
            else:
                print("Invalid choice")
    # HUNGRY
    elif user_input == 3:
        while True:
            print("=================================")
            user_hun = int(input("1)Buy food\n2)Open fridge\n3)Feed Larry\n4)Back to Main Menu\n> "))
            print("==================================")
            if user_hun == 1:
                larry.buy()
            elif user_hun == 2:
                larry.open_fridge()
            elif user_hun == 3:
                larry.feed()
            elif user_hun == 4:
                main()
            else:
                print("Invalid choice")
    elif user_input == 4:
        print(f"He's love for you ♥: {larry.love}")
        print(f"Clean: {larry.clean}")
        print(f"Hungry: {larry.hungry}")
        print(f"Fun: {larry.fun}")
        print(f"Balance: {larry.balance}")
    else:
        print("Enter a valid choice!")


if __name__ == '__main__':
    main()
