quiz_questions = {
    "What is the capital of France?": "a",
    "Who wrote 'To Kill a Mockingbird'?": "a",
    "What is the smallest prime number?": "a",
    "Which planet is known as the Red Planet?": "a",
    "What is the chemical symbol for water?": "a",
    "Who painted the Mona Lisa?": "a",
    "What is the largest mammal in the world?": "a",
    "In which year did the Titanic sink?": "a",
    "What is the square root of 64?": "a",
    "Who discovered penicillin?": "a"
}

list_of_choices = [
    ["A)Paris", "B)Berlin", "C)Madrid", "D)Rome"],
    ["A)Harper Lee", "B)Jane Austen", "C)Mark Twain", "D)J.K. Rowling"],
    ["A)2", "B)3", "C)5", "D)7"],
    ["A)Mars", "B)Venus", "C)Jupiter", "D)Saturn"],
    ["A)H2O", "B)CO2", "C)O2", "D)NaCl"],
    ["A)Leonardo da Vinci", "B)Vincent van Gogh", "C)Pablo Picasso", "D)Claude Monet"],
    ["A)Blue whale", "B)Elephant", "C)Giraffe", "D)Great white shark"],
    ["A)1912", "B)1905", "C)1898", "D)1923"],
    ["A)8", "B)6", "C)7", "D)9"],
    ["A)Alexander Fleming", "B)Marie Curie", "C)Isaac Newton", "D)Albert Einstein"]
]

users_choices = []
que_num = 0

for quiz in quiz_questions.keys():
    print(f"{quiz.title()}\n========================")
    for i in list_of_choices[que_num]:
        print(i)
    
    print("========================")
    user_input = input("> ")
    users_choices.append(user_input)

    if user_input == quiz_questions[quiz]:
        print("Correct!\n========================")
    else:
        print("Incorrect..\n========================")

    que_num += 1

print("Correct answers:", end=" ")
for y in quiz_questions.values():
    print(y.title(), end=" ")

print("\n")

print("Your answers:", end=" ")
for x in users_choices:
    print(x.title(), end=" ")

print("\nHope you had a great time!")
