import time
import random
from WithinvestingProgram import level2, level3, level1

class Investing:
    random_amount = random.randint(500, 5000)

    def __init__(self):
        self.amount = 0
        self.users_inv = []
        self.items = {}
    
    def starting_menu(self):
        print("(===============Invest===============)\nTry to invest on random items to see")
        time.sleep(1)
        print("If they go up in prices or down\nYou have 30 days")
        time.sleep(1)

        print(f"Goal: {self.random_amount}\n(====================Difficulty====================)")
        print("2)Medium Mode - Starting amount = 500 - Items = 30\n1)Easy Mode - Starting amount = 700 - Items = 24")
        print("3)Hard Mode - Starting amount = 200 - Items = 64")
        print("(====================================================)")

        users_choice = int(input("> "))

        if users_choice == 1:
            self.items = level1
            self.amount = 700

        elif users_choice == 2:
            self.items = level2
            self.amount = 500

        else:
            self.items = level3
            self.amount = 200
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def store(self):
        items1 = []
        count = 1

        print("==============================")

        for i in range(3):
            ran_choice = random.choice(list(self.items.keys()))
            items1.append(ran_choice)

            if self.items[ran_choice] <= 0:
                print(f"{count}) {ran_choice.capitalize()} - FREE")

            else:
                print(f"{count}) {ran_choice.capitalize()} - ${self.items[ran_choice]:.2f}")

            count += 1

        while True:
            buy = input("==============================\n> ").lower().strip()

            if buy in items1:
                item_price = self.items[buy]
                if item_price <= 0:
                    self.users_inv.append(buy)
                    print(f"Purchased {buy} for FREE.")
                    return

                elif self.amount >= item_price:
                    self.users_inv.append(buy)
                    self.amount -= item_price
                    print(f"Purchased {buy} for ${item_price:.2f}. Remaining balance: ${self.amount:.2f}")
                    return

                else:
                    print("You don't have enough money to buy this item.")
                    return

            else:
                print("Enter a valid choice!")

    def news(self):
        print("==============================")
        self.up_or_down()

    def up_or_down(self):
        amount_of_items = random.randint(1, 14)

        for i in range(amount_of_items):

            random_up = random.randint(1, 4)
            random_item = random.choice(list(self.items.keys()))
            random_price = self.items[random_item]
            times = random.randint(1, 5)
            time_ = random.randint(1, 14)

            if random_up == 1:
                upper = random_price * times
                self.items[random_item] = upper
                print(f"{random_item.capitalize()} has increased in price\n")
                time.sleep(0.45)

            elif random_up == 2:

                choice_y_n = random.randint(1, 2)

                if choice_y_n == 1:

                    upper1 = random_price * times

                    self.items[random_item] = upper1

                print(f"{random_item.capitalize()} shows signs of increasing in price\n")
                time.sleep(0.45)

            elif random_up == 3:
                
                upper2 = random_price - time_

                self.items[random_item] = upper2

                print(f"{random_item.capitalize()} has decreased in price\n")
                time.sleep(0.45)

            else:
                choice_y_n_ = random.randint(1, 2)
                if choice_y_n_ == 1:
                    upper3 = random_price - time_
                    self.items[random_item] = upper3
                print(f"{random_item.capitalize()} shows signs of decreasing in price\n")
                time.sleep(0.45)

    def trading(self):
        
        people = [
            "John Smith - 👨🏼", "Kaylee Schmidt - 👩‍🦱", "Griffin Arias - 👩🏼", "Alfredo Walton - 👦🏼",
            "Drew Cole - 👨‍", "Jay Walls - 👦️", "Jax Sosa - 👩🏾‍🦰", "Lyric Shannon - 🎵",
            "Hank McClojure - 🧒🏽", "Queen Li - 👱🏽‍♀️👑", "Johnson - 👨🏾"
        ]

        ran_people = random.choice(people)
        print("==============================")

        if not self.users_inv:
            print("You don't have anything to trade..")
            return

        y_n = input(f"{ran_people} Wants to trade! (Y/N): ").lower().strip()

        if y_n == "y":
            items_bot = []
            users_trade = []

            ran_amount_items = random.randint(1, 3)

            for _ in range(ran_amount_items):
                random_item = random.choice(list(self.items.keys()))
                items_bot.append(random_item)

            print(ran_people, end=" ")
            print(' | '.join(items_bot))

            while True:
                print("==============================")

                user_8 = input("Enter an item to trade\n> ").lower().strip()

                if user_8 == "":
                    print("Enter an item")
                    continue

                if user_8 not in self.users_inv:
                    print("==============================")
                    print("You don't have this item in your inventory")
                    continue
                else:
                    users_trade.append(user_8)

                    people_choice = random.randint(1, 3)

                    if people_choice == 1:
                        print(f"{ran_people} Accepted your trade!")

                        print("==============================")
                        print("Items you lost:")
                        for x in users_trade:
                            print(x)

                        print("-----------------")
                        print("Items you got: ")
                        for yay in items_bot:
                            print(yay)

                        for Accept in items_bot:
                            self.users_inv.append(Accept)

                        for Accept1 in users_trade:
                            self.users_inv.remove(Accept1)
                        return

                    elif people_choice == 2:
                        print(f"{ran_people} Declined your trade..")
                        return

                    elif people_choice == 3:
                        print(f"{ran_people} says that your item isn't worth his")
                        continue

        else:
            print(f"Declined {ran_people} trade")
            return

    def sell(self):
        print("Type q to quit")
        print("(==========Sell==========)")

        for i in self.users_inv:
            item_price = self.items.get(i, 0.0)
            print(f"{i.capitalize()} - ${item_price:.2f}")
            time.sleep(0.30)

        while True:
            print('==============================\nType "sell all" to sell all of the items\nType "menu" to stop')

            user_sell = input("Enter the item you want to sell: ").strip().lower()

            if user_sell == "menu" or user_sell == "q":
                return

            elif user_sell == "sell all":
                total_amount = sum(self.items.get(item, 0.0) for item in self.users_inv)
                self.amount += total_amount
                self.users_inv.clear()
                print(f"All items were sold successfully for ${total_amount:.2f}. New balance: ${self.amount:.2f}")
                return

            elif user_sell not in self.users_inv:
                print("You don't have the item in your inventory. Try again.")

            else:
                item_price = self.items.get(user_sell, 0.0)
                self.amount += item_price
                self.users_inv.remove(user_sell)
                print(f"The item '{user_sell}' was sold successfully for ${item_price:.2f}.")
                print(f"New balance: ${self.amount:.2f}")

    def show(self):
        print("==============================")
        for i in self.users_inv:
            item_price = self.items.get(i, 0.0)
            print(f"{i.capitalize()} - ${item_price:.2f}")
            time.sleep(0.30)


def main():
    i= Investing()
    i.starting_menu()
    days = 1
    news_times = 0
    while True:
        try:
            if i.amount == i.random_amount:
                print("You Won!")
                exit()
            elif days == 30 and i.amount != i.random_amount:
                print("You failed..")
                exit()
            elif i.amount <= 10:
                print("You Lose! You used all of your money.")
                exit()

            print("==============================")
            print(f"Day: {days}\nCurrent balance: ${i.amount:.2f}\nGoal: {i.random_amount}")
            print("==============================")
            print("1|Store\n2|Show inventory\n3|News\n4|Trading\n5|Sell items")
            print("Type 30 to pass a day")
            print("==============================")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                i.store()
            elif user_input == 2:
                i.show()
            elif user_input == 3:
                if news_times == 1:
                    print("You can only use the news 1 time a day")
                else:
                    news_times += 1
                    i.news()
            elif user_input == 4:
                i.trading()
            elif user_input == 5:
                i.sell()
            elif user_input == 30:
                if days == 30 and i.amount != i.random_amount:
                    print("You failed..")
                    break
                else:
                    i.up_or_down()
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    news_times -= 1
                    days += 1
            else:
                print("Enter a valid choice")
        except (ValueError, KeyError):
            print("Error!")
if __name__ == '__main__':
    main()
