import time

print("(--Welcome! to the loan Bank!--)")
has_good_income = None
has_criminal_record = None
while True:
    print("----------------------------------")
    good_income = input("Do you have Good income?(Yes/no): ").strip().lower()

    if good_income == "yes":
        print("Great!")
        print("----------------------------------")
        has_good_income = True
        break
    elif good_income == "no":
        print("oof!")
        break
    else:
        print("Enter (Yes/no)")
while True:
    criminal_record = input("Do you have a Criminal Record? (Yes/no): ").strip().lower()

    if criminal_record == "yes":
        print("Hmm.. we will think about that...")
        has_criminal_record = True
        break
    elif criminal_record == "no":
        print("Nice")
        break
    else:
        print("Enter (Yes/no)")
print("----------------------------------")
print("Processing...")
time.sleep(1)
print("----------------------------------")


if has_criminal_record and not has_good_income:
    print("Sorry you cant get a loan...")

elif not has_criminal_record and not has_good_income:
    print("You can get a loan! but with a limit because\n But You don't have good income ")
    print("(LIMIT) $1000 - $30,000")
    while True:
        t = int(input("LOAN: $"))
        if t > 30000:
            print("That's over the limit!")
            print("Try again")
            print("----------------------------------")
        elif t < 0:
            print("Please enter a valid number")
        else:
            print("----------------------------------")
            print("Great everything is Good enjoy your loan ;)")
            print(f"Your Loan: ${t}")
            break

elif has_criminal_record and has_good_income:
    print("You have Good income but you also have a Criminal record So u have a limit")
    print("(LIMIT) $100 - $50,000")
    print("----------------------------------")
    while True:
        c = int(input("LOAN: $"))
        if c > 50000:
            print("That's over the limit!")
            print("Try again")
            print("----------------------------------")
        elif c < 0:
            print("Please enter a valid number")
        else:
            print("----------------------------------")
            print("Great everything is Good enjoy your loan ;)")
            print(f"Your Loan: ${c}")
            break

elif has_good_income and not has_criminal_record:
    print("Great!\nYou can get a loan!")
    print("(LIMIT) $100 - $200,000")
    print("----------------------------------")
    while True:
        loan = int(input("LOAN: $").strip())
        if loan > 200000:
            print("That's over the limit!")
            print("Try again")
            print("----------------------------------")
        elif loan < 0:
            print("Please enter a valid number")
        else:
            print("----------------------------------")
            print("Great, everything is good. Enjoy your loan ;)")
            print(f"Your Loan: ${loan}")
            break
