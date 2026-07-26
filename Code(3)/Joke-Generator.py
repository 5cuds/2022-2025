import pyjokes

def main(): # main function
    print("(====Python Joke Generator!====)")
    while True:

        try:
            user_input = input("\nGet A Joke (Yes/No): ").lower().strip() # asking user if they want a joke

            if user_input == "yes":

                amount = int(input("========================\nHow Many Jokes Do You Want? (MAX: 10, MIN: 1): ")) # asking user how many jokes they want

                if amount > 10 or amount < 1:
                    print("Amount must be between 1 and 10.")
                    continue

                else:
                    print("========================")
                    for i in range(amount): # for loop to get the amount of jokes the user wants
                        print(f"Joke: {pyjokes.get_joke()}\n========================")

            else:
                
                break

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()