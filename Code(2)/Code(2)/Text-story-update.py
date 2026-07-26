import time

print("Well hello there user! welcome to JustNar's python text based game!")
print("You play as the game character Jordan Try to get all of the ending of this game")
print("Theres many endings to this game try to get them all Good luck!")
print("=============================================================")


def starting():
    lists1 = [
        "\nSunday, 2:30 AM\nAlex's Phone:\n======================================",
        "Alex: Hey, just got back. Crazy party, huh? 😅\n",
        "Jordan: Yeah, man! It was wild. Glad we got home safe.\n",
        "Alex: Me too. Did you see that guy who almost fell into the pool? 😂\n",
        "Jordan: LOL, yes! That was hilarious. You heading to bed soon?\n",
        "Alex: Not yet. Gonna grab a snack first.\n",
        "Jordan: Cool, cool. Text me if you need anything.\n",
        "Alex: Will do. Night, bro.\n",
        "Sunday, 3:00 AM\nAlex's Phone:\n======================================",
        "Alex: Yo, Jordan.\n",
        "Jordan: What's up? Thought you were going to bed.\n",
        "Alex: Yeah, just wanted to chat a bit more. You ever get that feeling someone’s watching you?\n",
        "Jordan: Uh, no? You okay, man?\n",
        "Alex: Yeah, just a bit paranoid I guess. Anyway, what did you think of Emma's outfit?\n",
        "Jordan: It was nice, I guess. Why?\n",
        "Alex: Just curious. You think she likes me?\n",
        "Jordan: Alex, why are you being weird? You never cared about this stuff.\n",
        "Alex: People change, Jordan.\n"
    ]

    for i in lists1:
        print(i)
        time.sleep(2)


def choice1():
    lists2 = [
        "Sunday, 3:15 AM\nJordan's phone:\n======================================",
        "Jordan: Dude, seriously, are you okay? You’re acting really strange.\n",
        "Alex: Haha, just messing with you. Goodnight for real this time.\n",
        "Jordan: Alright. Night.\n======================================",
    ]
    for i in lists2:
        print(i)
        time.sleep(2)

    user_choice1 = int(input("1)Ignore the strange texts and go to bed.\n2)Call Alex to check on him.\n> "))

    if user_choice1 == 1:
        lists3 = [
            "\nSunday, 4:00 AM\nAlex's Phone:\n======================================",
            "Alex: Jordan, help me.\n",
            "Jordan: What?? What’s wrong?\n",
            "Alex: There’s someone in my house.\n",
            "Jordan: Call the police! I’m coming over.\n",
            "Alex: Too late..",
        ]
        for i in lists3:
            print(i)
            time.sleep(2)
            if i == lists3[5]:
                time.sleep(5)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Ending: Too late.. ending")
                print("=====================\nMaybe you should have checked on him early..")
                exit()
    else:
        lists4 = [
            "\nSunday, 3:20 AM\nJordan's Phone:\n======================================",
            "Jordan: Calling Alex...\n",
            "Phone rings but no answer.\n",
            "Jordan: (texts) Alex, pick up. I'm worried.\n",
            "Alex: Sorry, man. Was in the bathroom. All good here.\n",
            "Jordan: Okay, just making sure. You seemed off earlier.\n",
            "Alex: Nah, just tired. Thanks for checking in. Night.\n",
            "Sunday, 4:00 AM\nJordan's Phone:\n======================================",
            "Alex: Jordan, help me.\n",
            "Jordan: What?? What’s wrong?\n",
            "Alex: There’s someone in my house.\n",
            "Jordan: Call the police! I’m coming over.\n",
            "Jordan: Hello?"
        ]
        for y in lists4:
            print(y)
            time.sleep(2)
            if y == lists4[11]:
                time.sleep(5)


def choice4():
    print("======================================")
    print("1)Enter the house.\n2)wait for the police to enter.\n3)Jordan leaves the scene, fearing for his own safety.")
    user_choice4 = int(input("> "))

    if user_choice4 == 1:
        print("\nSunday, 4:35 AM\nJordan's Phone:\n======================================")
        lists9 = [
            "Jordan: I’m inside. Where are you?\n",
            "Jordan hears a noise from the basement.\n",
            "Alex: Downstairs. Hurry.\n",
        ]
        for t in lists9:
            print(t)
            time.sleep(2)
            if t == lists9[2]:
                user_input = input("Go to the basement? (Y/N): ").lower().strip()
                if user_input == "y":
                    print("\nJordan confronts the person in the basement")
                    time.sleep(2)
                    print("\nSunday, 4:40 AM\n======================================")
                    time.sleep(2)
                    print("Jordan: I’m in the basement. Where are you?\n")
                    time.sleep(2)
                    print("A shadowy figure emerges\n")
                    time.sleep(2)
                    print("Unknown: Right here.\n")
                    time.sleep(2)
                    print("Jordan realizes it's not Alex and tries to escape but it's too late.\n")
                    time.sleep(5)
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("Ending: Trap ending..")
                    print("=====================\nTwo best friend are now together again..")
                    exit()
                else:
                    print("Jorden thinks this might be a trap.\n")
                    time.sleep(2)
                    print("So jordan tries to find another way into the basement.\n")
                    time.sleep(2)
                    print("\nSunday, 4:40 AM\n======================================")
                    time.sleep(2)
                    print("Jordan: Trying another way in. Hang on.\nJordan finds a side entrance.\n")
                    time.sleep(2)
                    print("Alex: Hurry, Jordan!\n")
                    time.sleep(2)
                    print("Jordan enters and sees Alex tied up. He manages to free him before the killer returns.\n")
                    time.sleep(5)
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("Ending: Good ending!\n=====================\nNothing beat the power of friendship!")
                    exit()

    elif user_choice4 == 2:
        print("Jordan lets the police handle the situation.")
        time.sleep(2)
        print("\nSunday, 4:40 AM\nJordan's Phone:\n======================================")
        time.sleep(2)
        print("Jordan: The police are handling it. Where are you?\nAlex: Too late for that now\n.")
        time.sleep(2)
        print("Police apprehend the unknown person, but it’s clear Alex is gone.")
        time.sleep(5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Ending: Killed ending..\n=====================\nNo note..")
        exit()
    else:
        print("Sunday, 4:45 AM\nJordan's Phone:\n======================================")
        time.sleep(2)
        print("Jordan: I’m sorry, Alex. I had to go.")
        print("Alex: Coward.")
        print("Jordan regrets his decision, haunted by the loss of his friend and the mystery of what really happened.")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Ending: Mystery ending..\n=====================\nStill a Mystery :O")
        exit()


def choice3():
    print("======================================")
    print('1)Talk to the police in person.\n2)Confront "Alex" and insists on proof')
    print("3)Wait for the police and keeps texting to stall.")
    user_choice3 = int(input("> "))

    if user_choice3 == 2:
        lists7 = [
            "\nJordan: If you’re really Alex, tell me what we promised each other last summer.\n",
            "Alex: Uh... that we'd always have each other’s back?\n",
            "Jordan: Wrong. Who are you?\n",
            "Alex: Fine. You caught me. But it’s too late for Alex now.\n",
            "Jordan: I’m coming in.\n",
        ]
        for r in lists7:
            print(r)
            time.sleep(2)
        choice4()

    elif user_choice3 == 1:
        print("Jordan informs the police about the situation.\n")
        time.sleep(2)
        print("A police officer came near the house and told him.\n")
        time.sleep(2)
        print("Stay away from the house for his safety, so he did.\n")
        time.sleep(2)
        print("Later, the police told him they found nothing.\n")
        time.sleep(5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Ending: Safety ending")
        print("=====================\nIt cost your friend’s life.")
        exit()
    else:
        lists8 = [
            "Jordan: Okay, maybe I’m being paranoid. Just stay on the line with me.\n",
            "Alex: Sure, what do you want to talk about?\n",
            "Jordan: Remember our trip last summer?\n",
            "Alex: Of course, best trip ever.\n",
            "Jordan: What was the name of that place we stayed?\n",
            "Alex: Uh, it was... Pinewood Lodge?\n",
            "Jordan: Wrong. Police are almost there.\n",
            "Alex: Clever, but it won’t help Alex now.\n",
            "\nSunday, 4:30 AM\nJordan's Phone:\n======================================",
            "Jordan: The police are here. You’re done.\n",
            "Alex: Game over.\n",
        ]
        for u in lists8:
            print(u)
            time.sleep(2)
            if u == lists8[10]:
                time.sleep(5)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Ending: ...")
                exit()


def choice2():
    print("======================================")
    user_choice2 = int(input("1)Rush to Alex's house immediately.\n2)Call the police first.\n> "))

    if user_choice2 == 1:
        lists5 = [
            "\nSunday, 4:15 AM\nJordan's Phone:\n======================================",
            "Jordan: Alex? Are you there?\n",
            "Jordan: Alex, please respond!\n",
            "Jordan: I’m at your place. Where are you?\n",
            "Alex: Hello, Jordan.\n",
            "Jordan: Who is this?\n",
            "Alex: Alex, of course. Who else?\n",
            "Jordan: Something’s off. You’re not acting like yourself.\n",
            "Alex: Just stressed. Sorry if I worried you.\n",
            "Jordan: Prove it. What did we talk about at the party?\n",
            "Alex: Uh, we talked about... Emma’s outfit?\n",
            "Jordan: Lucky guess. What else?\n",
            "Alex: Chill, man. Why so suspicious?\n",
            "Jordan: Because my best friend doesn’t talk like this.\n",
            "Alex: You’re being paranoid.\n",
        ]
        for g in lists5:
            print(g)
            time.sleep(2)
        choice3()

    else:
        lists6 = [
            "\nSunday, 4:10 AM\nJordan's Phone:\n======================================",
            "Jordan: Calling the police...\n",
            "Jordan informs the police about the situation.\n",
            "Jordan: (texts) Hang in there, Alex. Police are on their way.\n",
            "Alex: No time. You need to come now.\n",
            "Alex: Hello, Jordan.\n",
            "Jordan: Who is this?\n",
            "Alex: Alex, of course. Who else?\n",
            "Jordan: Something’s off. You’re not acting like yourself.\n",
            "Alex: Just stressed. Sorry if I worried you.\n",
            "Jordan: Prove it. What did we talk about at the party?\n",
            "Alex: Uh, we talked about... Emma’s outfit?\n",
            "Jordan: Lucky guess. What else?\n",
            "Alex: Chill, man. Why so suspicious?\n",
            "Jordan: Because my best friend doesn’t talk like this.\n",
            "Alex: You’re being paranoid.\n",
        ]
        for f in lists6:
            print(f)
            time.sleep(2)
        choice3()


def main():
    try:
        user_1 = input("Start? (Y/N): ").lower().strip()
        if user_1 != "y":
            exit()
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            starting()
            choice1()
            choice2()
            choice3()
            choice4()
    except ValueError:
        print("Dont add chars ok?")


if __name__ == '__main__':
    main()
