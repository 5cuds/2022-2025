import pandas as pd
import datetime, json
import matplotlib.pyplot as plt

'''
columns = ["Category", "Date", "Amount", "Note"]
dff = pd.DataFrame(columns=columns)
dff.to_csv("expense_data.csv", sep="|", index=False)
'''


class MainApp:

    def __init__(self):
        self.categorys = ["Food","Other","Entertainment","Transport","Utilities/bills"]
        self.df = pd.read_csv("expense_data.csv", sep="|")
        self.budget = None

    def Add_expense(self):
        for num, i in enumerate(self.categorys):
            print(f"{num}){i}")
        print("="*25)

        while True:
            category = int(input("Enter Index Of The Category: "))
            if category > len(self.categorys) or category < 0:
                print("Error Invalied Index")
                return
            else:
                while True:
                    amount = int(input("Amount: $"))
                    take_note = str(input("Would you like to leave a note for yourself? (Y/N): ")).lower().strip()
                    if take_note == "y":
                        note = str(input("Note: "))
                    else:
                        note = None

                    self.df = pd.concat([self.df, pd.DataFrame([{"Category": self.categorys[category], "Date": datetime.date.today(),"Amount": amount, "Note": note}])], ignore_index=True)
                    self.df.to_csv("expense_data.csv", sep="|", index=False)
                    return

    def Update_monthly_budget(self):
        pass

    def Settings(self):
        pass

    def delete_expense(self):

        view_cat = input("Would You Like To View The Categorys?: (Y/N): ").lower().strip()
        if view_cat != "n":
            for num, i in enumerate(self.categorys):
                print(f"{num}){i}")

            enter_cat = int(input("Category (Index): "))

            if enter_cat < 0 or enter_cat > len(self.categorys):
                print("Invalied Choice!")
                return
            
            print(self.df[self.df["Category"] == self.categorys[enter_cat]])

        while True:
            del_row = int(input("Enter The Row To Delete: "))
            
            if del_row < 0:
                print("Invalied Choice!")
                return
            else:
                self.df.drop(index=del_row, inplace=True)
            self.df.to_csv("expense_data.csv", sep="|", index=False)
            return
        

    def view_expenses(self):
        thingys = ["View Pie Chart", "Categorys", "Total"]

        for num, i in enumerate(thingys):
            print(f"{num}){i}")

        try:
            choice = int(input("Enter Your Choice (Index): "))
            
            group = self.df.groupby("Category")
            match thingys[choice]:
                case "View Pie Chart":

                    group_sum = group["Amount"].sum()
                    amounts = group_sum.tolist()
                    categories = group_sum.index.tolist()

                    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
                    plt.title('Expenses by Category')
                    plt.show()
                    
                case "Categorys":
                    for num, i in enumerate(self.categorys):
                        print(f"{num}){i}")
                    while True:

                        get_cat = int(input("Enter Your Choice (Index): "))

                        if get_cat > len(self.categorys) or get_cat < 0:
                            print("Invalied Index")
                            return
                        print(self.df.query("@self.df.Category == @self.categorys[@get_cat]"))

                        return_to_menu = input("Return to main menu? (Y/N): ").lower().strip()
                        if return_to_menu != "y":
                            self.view_expenses()
                        return

                case "Total":
                    group_sm = group["Amount"].sum()
                    x = group_sm.tolist()
                    y = group_sm.index.tolist()

                    for amount, cat in zip(x, y):
                        print(f"{cat}: ${amount}")

                    print(f"\nBiggest Expense: {max(x)}")

            return

        except Exception as e:
            print(f"(Exception): {e}")
            return

def main():
    app = MainApp()
    app.view_expenses()

if __name__ == "__main__":
    main()
