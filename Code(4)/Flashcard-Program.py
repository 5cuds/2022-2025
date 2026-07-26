import random
import time


class FlashcardProgram:

    def __init__(self):
        self.flashcards = {}

    def main_menu(self):
        print("(======== MAIN MENU ========)\n1)Random Math FlashCards\n2)Create Flashcards\n3)View Flashcards\n================")
        user_input = int(input("> "))

        if user_input == 1:
            self.random_math_flashcards()
        elif user_input == 2:
            self.create_flashcards()
        else:
            self.view_flashcards()

    def random_math_flashcards(self):
        print("Welcome to the Random Math Flashcards Program\nChoose A Difficulty!\n1)Easy\n2)Medium\n3)Hard\n================")
        choice = int(input("> "))

        if choice == 1:
            obers = ["+", "-"]
            range_number = 50
        elif choice == 2:
            obers = ["+", "-", "*"]
            range_number = 100
        else:
            obers = ["+", "-", "*", "/"]
            range_number = 200

        correct_answers = 0

        for i in range(10):
            num1 = str(random.randint(1, range_number))
            num2 = str(random.randint(1, range_number))
            ob = random.choice(obers)
            
            user_answer = input(f"{num1} {ob} {num2} = ")
            correct_answer = eval(num1+ob+num2)
            print(correct_answer)

            if user_answer == correct_answer:
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect!")

        print(f"Correct Answers: {correct_answers}")
        return
            

    def create_flashcards(self):

        make_card = input("FlashCard: ").title()

        if make_card in self.flashcards:
            print(f"That card already exists!")
            return
        
        else:
            answer = input(f'Correct Answer For "{make_card}": ').lower()

            self.flashcards[make_card] = answer
        return
    
    def view_flashcards(self):
        for i, x in self.flashcards.items():
            print(f"{i}: Answer: {x}")
            time.sleep(0.35)
        return
    

def main():
    program = FlashcardProgram()
    program.main_menu()
if __name__ == "__main__":
    main()