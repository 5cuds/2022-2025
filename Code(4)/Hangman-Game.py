import random
from RandomWords import words, hangart


def MainGame():
    """
    Main game function that will start the game and handle user interactions.
    """

    word = random.choice(words)

    word_letters = set(word)
    used_words = set()  

    lives, incorrect_guesses = 6, 0

    while len(word_letters) > 0 and lives > 0:

        print(hangart[incorrect_guesses])
        
        # Print lives left, used words and the current word with blanks
        print(f"\nLives: {lives}\nYour Guessed Letters: {"".join(used_words).upper()}")

        print("Word: ", " ".join([letter if letter in used_words else "_" for letter in word]).upper())

        # Get user input
        user_input = input("\nGuess A Letter!: ").lower().strip()

        if user_input in word_letters:
            # If the letter is correct add it to the used words set
            print(f"Correct Guess!. Added {user_input}")

            used_words.add(user_input)

            word_letters.remove(user_input)
                     
        elif user_input in used_words:
            # If the letter has been guessed before, tell the user
            print("Your Guessed That Letter Before. Try Again.")
            
        else:
            # If the letter is incorrect add it to the used words set and decrease lives
            used_words.add(user_input)
            print("Incorrect. Try Again!")
            incorrect_guesses += 1
            lives -= 1


    if lives == 0:
        # Game over, print the correct word
        print(f"\nYou Lose!\nCorrect Word was: {word}")
    else:
        # Game won, print a win message
        print("\nYou Won!")
    exit()
        
if __name__ == "__main__":
    try:
        MainGame()
    except Exception as e:
        print(f"\nError: {e}")