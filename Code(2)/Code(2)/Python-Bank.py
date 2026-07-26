class Bank:
    balance = 0.00

    def deposit(self):
        user_input = float(input("Deposit: $"))
        if user_input <= 0:
            print("Amount must be greater then 0")
        else:
            print(f"Successfully deposited the funds.")
            self.balance += user_input

    def withdraw(self):
        user_input0 = float(input("Withdraw: $"))
        if user_input0 > self.balance:
            print("insufficient funds")
        elif user_input0 <= 0:
            print("Amount must be greater then 0")
        else:
            print(f"Withdrawn was successful.")
            self.balance -= user_input0


def main():
    bank = Bank()
    print("(----Python Bank!----)")
    while True:
        try:
            print("======================\n1)Show balance\n2)Deposit\n3)Withdraw\n4)Exit\n======================")
            user_input1 = int(input("> "))
            if user_input1 == 1:
                print(f"Balance: ${bank.balance:.2f}")
            elif user_input1 == 2:
                bank.deposit()
            elif user_input1 == 3:
                bank.withdraw()
            elif user_input1 == 4:
                break
            else:
                print("Enter a valid Choice!")

        except ValueError:
            print("Error!")


if __name__ == '__main__':
    main()
