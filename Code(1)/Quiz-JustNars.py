questions = (
    "What is JustNars first ever minecraft account: ",
    "When did JustNars start playing on gamster.org?: ",
    "When did JustNars started playing minecraft?: ",
    "What is JustNars favorite Gamemode?: ",
    "When did JustNars made his new account: "
)

options = (
    ("A. Ballshiter4000", "B. NGMgamer15", "C. NGMgamerMC", "D. Justin14"),
    ("A. 2021", "B. 2020", "C. 2017", "D. 2022"),
    ("A. 2019", "B. 2012", "C. 400 BC", "D. 2024"),
    ("A. Skywars", "B. Bedwars", "C. Builduhc", "D. Boxing"),
    ("A. 2021", "B. 2020", "C. 2023", "D. 2018")
)

answers = ["B", "A", "A", "B", "C"]
guesses = []
score = 0
question_num = 0

for question in questions:
    print("=====================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Ender (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1

    else:
        print("Incorrect")
        print(f"Correct answer was {answers[question_num]}")

    question_num += 1

print("=====================\n     YOUR RESULT\n=====================")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Score: {score}%")
