import random
import time


class RPG:

    def __init__(self):

       self.characters = {
            "Max the maverick": {"strength": 7, "hp": 450, "attack_moves": {"Thunder punch": 35, "Cyclone kick": 25, "Tornado takedown": 20}},
            "Jake the jester": {"strength": 5, "hp": 400, "attack_moves": {"Jester's jab": 30, "Prankster's pummel": 20, "Fool's fury": 15}},
            "Lily the lightning": {"strength": 6, "hp": 420, "attack_moves": {"Lightning strike": 40, "Thunderbolt": 30, "Storm surge": 25}},
            "Sam the sage": {"strength": 4, "hp": 380, "attack_moves": {"Sage's smite": 25, "Wisdom whack": 20, "Mystic blast": 30}},
            "Ava the ace": {"strength": 8, "hp": 460, "attack_moves": {"Ace's assault": 35, "Victory swipe": 25, "Champion's charge": 30}},
            "Leo the lionheart": {"strength": 9, "hp": 470, "attack_moves": {"Lion's roar": 40, "Heart strike": 35, "Bravery bash": 30}},
            "Mia the mystic": {"strength": 5, "hp": 410, "attack_moves": {"Mystic Mmssile": 30, "Arcane blast": 25, "Enchanted slash": 20}},
            "Eli the enigma": {"strength": 6, "hp": 430, "attack_moves": {"Enigma's edge": 35, "Puzzle punch": 20, "Mystery maul": 25}},
            "Zoe the zephyr": {"strength": 7, "hp": 440, "attack_moves": {"Zephyr's zap": 35, "Gale force": 30, "Wind whip": 25}},
            "Finn the falcon": {"strength": 8, "hp": 450, "attack_moves": {"Falcon's fury": 40, "Talon tackle": 35, "Winged whirl": 30}}
            }
       self.player_char = None
       self.opponent = None
        
    def choose_char(self):

        global random_people

        limit_3 = random.sample(list(self.characters.keys()), 3)
        random_people = random.choice(list(self.characters.keys()))


        for i in limit_3:
            print(i.title())
        print("===================")

        while True:

            users_choice = input("Enter the name of your character: ").capitalize()

            if users_choice in limit_3:
                self.player_char = users_choice
                self.opponent = random_people

                print(f"===================\n{users_choice.title()} Is your character Good luck!\n===================")
                print(f"{self.opponent.title()} is the one you fight!\n===================")

                return
            
            else:
                print("Enter a valid choice\n===================")
                continue


    def battle(self):

        global players_turn

        players_turn = None

        random_coin_toss = random.choice(["Heads", "Tails"])

        coin_toss_choice = input("Heads or Tails?: ").capitalize().strip()

        if coin_toss_choice == random_coin_toss:

            print("You Won the coin toss!\n===================")
            players_turn = True

        else:
            print(f"{random_people} Won the coin toss\n===================")
            players_turn = False

        max_attack_move = max(players_stats["attack_moves"], key=lambda move: players_stats["attack_moves"][move])
        max_attack_value = players_stats["attack_moves"][max_attack_move]
        print(f"Your highest attack move is {max_attack_move} with {max_attack_value} damage.")


        while players_stats["hp"] > 0 and computers_stats["hp"] > 0:


            attack_moves = self.characters[self.player_char].get("attack_moves", {})

            player_moves = self.characters[self.player_char].get("strength", {})
            com_moves = self.characters[self.player_char].get("strength", {})


            if players_turn:

                count = 1

                for name in attack_moves.keys():
                    time.sleep(1.20)
                    print(f"{count}|{name.title()}")
                    count += 1
                print("===================")

                user_input = input("Enter your choice!: ").capitalize()

                if user_input in attack_moves:

                    oops_haha = random.randint(1, 5)

                    if oops_haha == 3:

                        list_of_failed_attacks = [
                            f"{self.player_char}'s attack missed {self.opponent}!",
                            f"{self.opponent} skillfully parried {self.player_char}'s attack.",
                            f"{self.opponent}'s shield blocked {self.player_char}'s attack effortlessly.",
                            f"{self.player_char}'s attack was interrupted by a sudden distraction.",
                            f"{self.player_char} stumbled and their attack went wide.",
                            f"{self.player_char} lost their grip and failed to land the hit.",
                            f"{self.player_char} hesitated, giving {self.opponent} time to dodge.",
                            f"{self.player_char} tripped over their own feet, missing the attack."
                        ]

                        ahh_no = random.choice(list_of_failed_attacks)

                        print(f"{ahh_no}\n===================")

                    else:
                        q = random.choice(["+", "-"])

                        if q == "+":
                            s = lambda x, y: x + y
                        elif q == "-":
                            s = lambda x, y: x - y

                        match player_moves:
                            case 9:
                                random_amount = random.randint(5, 30)
                            case 8:
                                random_amount = random.randint(1, 27)
                            case 7:
                                random_amount = random.randint(1, 24)
                            case 6:
                                random_amount = random.randint(3, 20)
                            case 5:
                                random_amount = random.randint(2, 15)
                            case 4:
                                random_amount = random.randint(3, 13)

                        total = s(attack_moves[user_input], random_amount)

                        computers_stats["hp"] -= total
                        print(f"{self.player_char} used {user_input} causing {total} damage to {self.opponent}.")
                        print(f"{self.opponent}'s Heath: {computers_stats["hp"]}.\n")

                    players_turn = not players_turn

            else:

                oops_haha1 = random.randint(1, 5)

                if oops_haha1 == 3:

                    list_of_failed_attacks = [
                        f"{self.opponent}'s attack missed {self.opponent}!",
                        f"{self.player_char} skillfully parried {self.opponent}'s attack.",
                        f"{self.player_char}'s shield blocked {self.opponent}'s attack effortlessly.",
                        f"{self.opponent}'s attack was interrupted by a sudden distraction.",
                        f"{self.opponent} stumbled and their attack went wide.",
                        f"{self.opponent} lost their grip and failed to land the hit.",
                        f"{self.opponent} hesitated, giving {self.opponent} time to dodge.",
                        f"{self.opponent} tripped over their own feet, missing the attack."
                    ]

                    ahh_no1 = random.choice(list_of_failed_attacks)

                    print(f"{ahh_no1}\n===================")

                    players_turn = True

                else:

                    i = random.choice(["+", "-"])

                    if i == "+":
                        d = lambda x, y: x + y
                    elif i == "-":
                        d = lambda x, y: x - y

                    match com_moves:
                            case 9:
                                random_amount = random.randint(5, 30)
                            case 8:
                                random_amount = random.randint(1, 27)
                            case 7:
                                random_amount = random.randint(1, 24)
                            case 6:
                                random_amount = random.randint(3, 20)
                            case 5:
                                random_amount = random.randint(2, 15)
                            case 4:
                                random_amount = random.randint(3, 13)

                    random_amount1 = random.randint(1, 18)

                    random_attack = random.choice(list(self.characters[self.opponent]["attack_moves"].keys()))

                    damage = self.characters[self.opponent]["attack_moves"][random_attack]

                    total_computer = d(damage, random_amount1)

                    players_stats["hp"] -= total_computer

                    print(f"{self.opponent} used {random_attack} causing {total_computer} damage to {self.player_char}")
                    print(f"{self.player_char}'s Health: {players_stats['hp']}.\n")

                    players_turn = True


        if players_stats["hp"] <= 0:
            print("You lost the battle! better luck next time.\n===================")
        else:
            print("You won the battle!\n===================")

    def show_stats(self):

        global players_stats, computers_stats

        players_stats = self.characters[self.player_char]
        computers_stats = self.characters[self.opponent]

        print(f"Your stats:\nStrength: {players_stats["strength"]}")
        print(f"HP: {players_stats["hp"]}\n===================")

        print(f"{self.opponent}'s stats:\nStrength: {computers_stats["strength"]}")
        print(f"HP: {computers_stats["hp"]}\n===================")


def main():

    try:

        r = RPG()

        r.choose_char()

        r.show_stats()

        r.battle()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()