import json
import datetime
import time
import re
from termcolor import colored


with open("data.json", "w") as file:
        json.dump({"Food": [], "Entertainment": [], "Transport": [], "Utilities/bills": [], "Other": [],
        "Income": 60000, "Budget": 15000}, file, indent=2)


class MainProgram:

    def __init__(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        
        self.budget = data["Budget"]

    def add_expense(self):
        while True:
            try:
                enter_price = float(input("Price: $"))
            except ValueError:
                print(colored("Error! Enter Numbers ONLY!", "red"))
                continue

            if enter_price <= 0:
                print(colored("Enter a valid amount.", "red"))
                continue
            elif enter_price > self.budget:
                print(colored("Insufficient Funds!", "red"))
                return
            else:
                with open("data.json", "r") as file:
                    data = json.load(file)
                

                input_expense = input("Purchase: ").capitalize().strip()


                print("====================)")

                for count,i in enumerate(data):
                    if i in ("Budget", "Income"):
                        continue
                    print(f"{count}){i}")
                    time.sleep(0.32)

                print("====================)")

                while True:

                    cat_input = input("Enter a category: ").capitalize().strip()

                    if cat_input in data:

                        self.budget -= enter_price
                        data[cat_input].append(f"{input_expense} - ${enter_price:.2f} | Date: {datetime.date.today()}")

                        print(colored(f"Added! Date: {datetime.date.today()} Total: ${enter_price}", "green"))

                        with open("data.json", "w") as file:
                            json.dump(data, file)
                        
                    else:
                        print(colored("Invalid category. Try again", "red"))
                        continue
                    return
    

    def delete_expense(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
                print("File not found!")


        print("====================)")
        count = 0

        for i in data:
            if i in ("Budget", "Income"):
                continue

            print(f"{count}) {i}")
            count += 1
            time.sleep(0.32)

        print("====================)")
        while True:

            enter_category = input("Enter a category: ").capitalize().strip()
                
            if enter_category in data:
                
                count_display = 0
                for i in data[enter_category]:
                    print(f"{count_display}){i}")
                    time.sleep(0.32)
                    count_display += 1

                while True:
                    try:
                        delete_index = int(input("Enter the index of the purchase: "))
                    except ValueError:
                        print(colored("Enter valid numbers!", "red"))
                        continue

                    if delete_index > count_display or delete_index < 0:
                        print(colored("Invalid Index!", "red"))
                        continue
                    else:
                        del data[enter_category][delete_index]

                        with open("data.json", "w") as file:
                            json.dump(data, file)
                            
                        return

            else:
                mainmenu_que = input("Invalid category! Would you like to return to the main menu? (Y/N): ").lower().strip()
                if mainmenu_que != "y":
                    continue
                return

    def calculate_expenses(self):
        with open("data.json") as file:
            data = json.load(file)

        expenses = {} 
        total_expenses = 0  
        for category in data:
            if category in ("Budget", "Income"):
                continue  

            
            category_total = 0
        
            for expense in data[category]:
                match = re.search(r'\d+(\.\d+)?', expense)  

                if match:
                    
                    amount = float(match.group())
                    category_total += amount
                    total_expenses += amount  
            expenses[category] = category_total

        if total_expenses > 0:
            print("Category-wise Expense Percentages: ")
            for category, total in expenses.items():
                percent = (total / total_expenses) * 100
                print(f"{category} - {percent:.2f}%")
        else:
            print(colored("No expenses found", "yellow"))

        return
    
    def view_expenses(self):
        with open("data.json", "r") as file:
            data = json.load(file)

        for num, i in enumerate(data, start=1):
            if i in ("Budget", "Income"):
                continue
            print(f"{num}){i}")
            time.sleep(0.25)

        while True:
            try:
                input_users_cat = input(f"Enter The Category (Type All to View al): ").capitalize().strip()
                print("====================)")
                if input_users_cat in data:
                    for i in data[input_users_cat]:
                        print(i)
                        time.sleep(0.30)
                    return

                elif input_users_cat == "All":
                    for cat in data:
                        for expense in data[cat]:
                            print(expense)
                            time.sleep(0.30)
                        
                else:
                    print(colored("Enter a invalid choice!", "red"))
                    continue
                
            except ValueError:
                print("Invalid Choice!")
                self.view_expenses()
                
    def settings(self):
        with open("data.json", "r") as file:
                data = json.load(file)

        print("====================)")
        print(f"{colored("1)Add a new Category", "light_green")}\n{colored("2)Delete a Category", "red")}\n{colored("3)Set new budget", "yellow")}\n4)Return\n=================")

        users_choice_of_set = int(input("> "))

        if users_choice_of_set == 1:
            new_cat = input("Category: ").capitalize()

            data[new_cat] = []

            print(colored(f"Added! {new_cat}", "green"))

            with open("data.json", "w") as file:
                json.dump(data, file)

            return

        elif users_choice_of_set == 2:
            del_cat = input("Category: ").capitalize()
            del data[del_cat]

            print(colored(f"Deleted {del_cat}!", "red"))
            with open("data.json", "w") as file:
                        json.dump(data, file)
            return
        elif users_choice_of_set == 3:
            while True:
                enter_new_budget = int(input("New Budget: $"))

                if enter_new_budget > self.budget:
                    print(colored("insufficient funds.", "red"))
                    continue
                else:
                    data["Budget"] = enter_new_budget
                    print(f"Updated Budget!\n")
                    with open("data.json", "w") as file:
                        json.dump(data, file)
                    return
        else:
            return

    def stats(self):
        with open("data.json", "r") as file:
            data = json.load(file)

        biggest_purchase = 0
        for i in data:
            for x in i: 
                match = re.search(r'\d+(\.\d+)?', x)  

                if match:
                    amount1 = float(match.group())
                    
                    if amount1 > biggest_purchase:
                        biggest_purchase = amount1

        print(f"Biggest Purchase: ${biggest_purchase}")

             
        
def main():
    print("|+==Python Expense Tracker!==+|\n====================)")

    with open("data.json", "r") as file:
        data = json.load(file)

    while True:
        try:
            program = MainProgram()
            print(f"Budget: ${program.budget}\nIncome: ${data["Income"]}\n====================)")
            print("1)Add A Expense 🛒\n2)Delete A Expense 😒\n3)View Expenses 🔎\n4)Calculate Expenses 🖩\n5)Settings ⚙\n6)See Stats 🌟")
            print("====================)")

            user_input_of_choice = int(input("> "))

            if user_input_of_choice == 1:
                program.add_expense()
            elif user_input_of_choice == 2:
                program.delete_expense()
            elif user_input_of_choice == 3:
                program.view_expenses()
            elif user_input_of_choice == 4:
                program.calculate_expenses()
            elif user_input_of_choice == 5:
                program.settings()
            elif user_input_of_choice == 6:
                program.stats()
            else:
                print(colored("Invalid choice!", "red"))
                continue

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
