import random
import time


class Cooking:

    def __init__(self):

        self.ingredients = {"Pizza dough": 5,"Tomato sauce": 5,"Pepperoni": 5,"Olives": 5,"Mozzarella cheese": 5,
                            "Burger bun": 5,"Beef patty": 5,"Lettuce": 5,"Tomato slices": 5,"Cheese": 5,
                            "Sliced bread": 5,"Turkey": 5,"Cheese": 5,"Lettuce": 5,"Tomato slices": 5,
                            "Hotdog bun": 5,"Hotdog sausage": 5,"Mustard": 5,"Ketchup": 5,"Onions": 5,
                            "Potatoes": 5,"Olive oil": 5,"Salt": 5,"Pepper": 5,"Paprika": 5}
        self.total = 0
        self.total_dishs = 0
        self.total_dish_day = 0

    def cook(self):
        print('Type "Exit" to be back to the main menu\n')
        while True:
            random_food = random.randint(1, 5)

            if random_food == 1:
                amount_pay = 5.85
                food_to_make = ["Potatoes", "Olive oil", "Salt", "Pepper", "Paprika"]
                food = "Fries"

            elif random_food == 2:

                amount_pay = 3.50
                food_to_make = ["Burger bun", "Beef patty", "Lettuce", "Tomato slices", "Cheese"]
                food = "Burger"

            elif random_food == 3:

                amount_pay = 6.40
                food_to_make = ["Sliced bread", "Turkey", "Cheese", "Lettuce", "Tomato slices"]
                food = "Sandwich"

            elif random_food == 4:

                amount_pay = 3.99
                food_to_make = ["Hotdog bun", "Hotdog sausage", "Mustard", "Ketchup", "Onions"]
                food = "Hotdog"

            else:
                amount_pay = 4.99
                food = "Pizza"
                food_to_make = ["Pizza dough", "Tomato sauce", "Pepperoni", "Olives", "Mozzarella cheese"]


            print(f"ORDER: {food}\n==================")

            users_food = []

            for _ in range(len(food_to_make)):


                user_input = input("Add ingredients: ").capitalize()

                if user_input == "Exit":
                    return
                
                elif self.ingredients[user_input] == 0:
                    print(f"We dont have any {user_input} left try to ask some or buy some\n================")
                    return
                
                elif user_input not in food_to_make:
                    print("Incorrect ingredient! try to add the correct ingredients this time\n================")
                    return

                else:

                    users_food.append(user_input)
                    self.ingredients[user_input] -= 1

                    print(f"Added {user_input}!\n==================")


            print("Cooking..")
            time.sleep(5)

            if sorted(users_food) == sorted(food_to_make):
                print(f"Great you made {food}!\n==================")
                self.total += amount_pay
                self.total_dish_day += 1

            else:
                print("You messed up the order!\n================")
    
    def recipes(self):
        
        print("Fries: Potatoes, Olive oil, Salt, Pepper, Paprika\n")
        print("Burger: Burger bun, Beef patty, Lettuce, Tomato slices, Cheese\n")
        print("Sandwich: Sliced bread, Turkey, Cheese, Lettuce, Tomato slices\n")
        print("Hotdog: Hotdog bun, Hotdog sausage, Mustard, Ketchup, Onions\n")
        print("Pizza: Pizza dough, Tomato sauce, Pepperoni, Olives, Mozzarella cheese\n================")
        return

    def store_ingredients(self):
        
        for element, element2 in self.ingredients.items():
            time.sleep(0.28)
            print(f"{element} - {element2}\n")
        return

    def store(self):

        foods = {"Pizza dough": 5.99,"Tomato sauce": 4.99,"Pepperoni": 5.42,"Olives": 4.99,"Mozzarella cheese": 10,
                "Burger bun": 3,"Beef patty": 7.20,"Lettuce": 6.01,"Cheese": 5.90,
                "Sliced bread": 3,"Turkey": 5,"Tomato slices":2.99,
                "Hotdog bun": 3,"Hotdog sausage": 3.99,"Mustard": 10,"Ketchup": 1.99,"Onions": 10,
                "Potatoes": 2.25,"Olive oil": 2.75,"Salt": 3.50,"Pepper": 3.50,"Paprika": 5}
        
        total1 = 0
        cart = []

        while True:
    
            enter_item = input("Enter the item you want to buy [Type 'SH' to search] [Type exit to quit]: ").capitalize()

            if enter_item == 'Sh':
                search = input("Enter the item you want to search: ").capitalize()
                if search in foods:
                    print(f"{search} - ${foods[search]}")
                    continue
                else:
                    continue
            elif enter_item == "Exit":
                print("----Things you got!----")
                for i in cart:
                    print(i)
                if self.total == 0:
                    print("You dont have any money Game Over!\n================")
                    break
                else:
                    print(f"Total: ${total1}")
                    self.total -= total1
                    print(f"Total balance: {self.total}")
                return
            
            elif enter_item not in foods.keys():
                print("Enter a valid item")
                continue
            else:
                self.ingredients[enter_item] += 1
                cart.append(enter_item)
                total1 += foods[enter_item]
                print("Added to cart!")
                continue
            
    

    def pass_day(self):

        print("You passed the day here's your stats for today!")

        self.total_dishs += self.total_dish_day

        print(f"Total dishs (Today): {self.total_dish_day}")
        time.sleep(1.25)

        print(f"Balance: {self.total}")
        time.sleep(1.25)

        print(f"Total dishs made: {self.total_dishs}\n================")
        time.sleep(2)

        self.total_dish_day = 0

        return

    
    def ask_ingredients(self):
        print("You asked for some ingredients\n================")

        print("They got:")

        items = random.randint(1, 10)

        for i in range(items):
            
            c = random.choice(list(self.ingredients.keys()))
            c_amount = random.randint(1, 5)

            self.ingredients[c] += c_amount

            print(f"{c} - {c_amount}")
            time.sleep(0.23)

        return
    
def main():
    c = Cooking()
    day = 1
    while True:
        try:
            print(f"Day {day}\n================")
            print("1)Cook\n2)Store\n3)Recipes\n4)Ingredients\n================\nType 69 to pass a day.\n================")
            user_input = int(input("> "))
            if user_input == 1:
                c.cook()
            elif user_input == 2:
                c.store()
            elif user_input == 3:
                c.recipes()
            elif user_input == 4:
                user_choice = int(input("================\n1)Ask for ingredients\n2)Show ingredients\n================\n> "))
                if user_choice == 1:
                    c.ask_ingredients()
                else:
                    c.store_ingredients()
            else:
                day += 1
                c.pass_day()
                time.sleep(5)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
