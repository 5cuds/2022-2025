print("Welcome to the  python ice Cream maker program! ")
print("Enter your choice of ice cream!")


def vanilla():
    add_some_rainbow_things = False
    add_more_cream = False
    add_some_choco_things = False

    user_input1 = input("Add some rainbow things? (Y/N): ").lower().strip()
    if user_input1 == 'y':
        add_some_choco_things = True
    else:
        add_some_rainbow_things = False
    user_input2 = input("Add more cream? (Y/N): ").lower().strip()
    if user_input2 == 'y':
        add_more_cream = True
    else:
        add_more_cream = False
    user_input3 = input("Add some choco things? (Y/N): ").lower().strip()
    if user_input3 == 'y':
        add_some_choco_things = True
    else:
        add_some_choco_things = False

    if add_some_rainbow_things and add_some_choco_things and add_more_cream:
        print("You made a Vanilla choco chips with rainbow things and with MORE CREAM Ice cream!")
    if add_some_rainbow_things and add_some_choco_things:
        print("You made a Vanilla choco chips and rainbow things Ice cream!")
    if add_some_choco_things and add_more_cream:
        print("You made a Vanilla choco chips ice cream with more cream!")
    if add_some_rainbow_things and add_more_cream:
        print("You made a Vanilla Ice cream with rainbow things with more Cream!")
    if add_some_choco_things:
        print("You made a Vanilla ice cream with choco chips")
    if add_some_rainbow_things:
        print("You made a Vanilla Ice cream with rainbow things!")
    if add_more_cream:
        print("You made a Vanilla ice cream with more cream!")


def chocolate():
    add_some_rainbow_things = False
    add_more_cream = False
    add_some_choco_things = False

    user_input1 = input("Add some rainbow things? (Y/N): ").lower().strip()
    if user_input1 == 'y':
        add_some_choco_things = True
    else:
        add_some_rainbow_things = False
    user_input2 = input("Add more cream? (Y/N): ").lower().strip()
    if user_input2 == 'y':
        add_more_cream = True
    else:
        add_more_cream = False
    user_input3 = input("Add some choco things? (Y/N): ").lower().strip()
    if user_input3 == 'y':
        add_some_choco_things = True
    else:
        add_some_choco_things = False

    if add_some_rainbow_things and add_some_choco_things and add_more_cream:
        print("You made a chocolate choco chips with rainbow things and with MORE CREAM Ice cream!")
    if add_some_rainbow_things and add_some_choco_things:
        print("You made a chocolate choco chips and rainbow things Ice cream!")
    if add_some_choco_things and add_more_cream:
        print("You made a chocolate choco chips ice cream with more cream!")
    if add_some_rainbow_things and add_more_cream:
        print("You made a chocolate Ice cream with rainbow things with more Cream!")
    if add_some_choco_things:
        print("You made a chocolate ice cream with choco chips")
    if add_some_rainbow_things:
        print("You made a chocolate Ice cream with rainbow things!")
    if add_more_cream:
        print("You made a chocolate ice cream with more cream!")


while True:
    user_input = int(input("1)Vanilla\n2)Chocolate\nEnter your choice: "))
    if user_input == 1:
        vanilla()
    elif user_input == 2:
        chocolate()
    else:
        print("Enter a valid choice")


