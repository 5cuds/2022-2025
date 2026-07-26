import random
import time


class MainGame:

    def __init__(self) -> None:
        self.characters = {
            "Max The Maverick": {"strength": 7, "hp": 450, "Defense": 6, "attack_moves": {"Thunder punch": 35, "Cyclone kick": 25, "Tornado takedown": 20}},
            "Jake The Jester": {"strength": 5, "hp": 400, "Defense": 3, "attack_moves": {"Jester's jab": 30, "Prankster's pummel": 20, "Fool's fury": 15}},
            "Lily The Lightning": {"strength": 6, "hp": 420, "Defense": 5, "attack_moves": {"Lightning strike": 40, "Thunderbolt": 30, "Storm surge": 25}},
            "Sam The Sage": {"strength": 4, "hp": 380, "Defense": 6, "attack_moves": {"Sage's smite": 25, "Wisdom whack": 20, "Mystic blast": 30}},
            "Ava The Ace": {"strength": 8, "hp": 460, "Defense": 2, "attack_moves": {"Ace's assault": 35, "Victory swipe": 25, "Champion's charge": 30}},
            "Leo The Lionheart": {"strength": 9, "hp": 470, "Defense": 8, "attack_moves": {"Lion's roar": 40, "Heart strike": 35, "Bravery bash": 30}},
            "Mia The Mystic": {"strength": 5, "hp": 410, "Defense": 6, "attack_moves": {"Mystic Mmssile": 30, "Arcane blast": 25, "Enchanted slash": 20}},
            "Eli The Enigma": {"strength": 6, "hp": 430, "Defense": 4, "attack_moves": {"Enigma's edge": 35, "Puzzle punch": 20, "Mystery maul": 25}},
            "Zoe The Zephyr": {"strength": 7, "hp": 440, "Defense": 4, "attack_moves": {"Zephyr's zap": 35, "Gale force": 30, "Wind whip": 25}},
            "Finn The Falcon": {"strength": 8, "hp": 450, "Defense": 5, "attack_moves": {"Falcon's fury": 40, "Talon tackle": 35, "Winged whirl": 30}}
            }
        self.player = None
        self.computer = None

    def main_fight(self):
        
        print("Coin Toss! in ")
        for i in range(1, 4):
            time.sleep(1)
            print(i)

        players_turn = False
        
        if random.choice(["Heads", "Tails"]) == "Heads": # Picks Whos Gets to start first
            print(f"\n{self.player} Won The Coin Toss!\n")
            players_turn = True
        else:
            print(f"\n{self.computer} Won The Coin Toss!\n")

        while self.characters[self.computer]["hp"] > 0 and self.characters[self.player]["hp"] > 0: # this will stay True if both of the players is over 0 hp
            
            if players_turn:

                attack_moves = self.characters[self.player]["attack_moves"]

                for i, element in enumerate(attack_moves.keys(), start=1):
                    print(f"{i}){element}")

                users_choice = input("\nChoose Your Attack!: ").capitalize()

                if users_choice not in attack_moves:
                    print("\nInvalid Choice PENALTY!")
                else:

                    if random.randint(1, 5) == 3:
                        # list of missed attack moves
                        list_of_failed_attacks = [f"{self.player}'s attack missed {self.computer}!", f"{self.computer} skillfully parried {self.player}'s attack.",
                                    f"{self.computer}'s shield blocked {self.player}'s attack effortlessly.", f"{self.player}'s attack was interrupted by a sudden distraction.",
                                    f"{self.player} stumbled and their attack went wide.",f"{self.player} lost their grip and failed to land the hit.",
                                    f"{self.player} hesitated, giving {self.computer} time to dodge.",f"{self.player} tripped over their own feet, missing the attack."]
                        print(random.choice(list_of_failed_attacks))

                    else:
                        total_hit = attack_moves[users_choice] + random.randint(1, self.characters[self.player]["strength"])
                        total_hit -= random.randint(1, self.characters[self.computer]["Defense"])
                        self.characters[self.computer]["hp"] -= total_hit # users attack damage
                        print(f"\n{self.player} used {users_choice} causing {total_hit} damage to {self.computer}.")
                        print(f"\n{self.computer}'s Heath: {self.characters[self.computer]["hp"]}.\n")
                    players_turn = False
            
            else: # Computer's Turn
                if random.randint(1, 5) == 3:
                    list_of_failed_attacksc = [f"{self.computer}'s attack missed {self.player}!", f"{self.player} skillfully parried {self.computer}'s attack.",
                                    f"{self.computer}'s shield blocked {self.player}'s attack effortlessly.", f"{self.computer}'s attack was interrupted by a sudden distraction.",
                                    f"{self.computer} stumbled and their attack went wide.",f"{self.computer} lost their grip and failed to land the hit.",
                                    f"{self.computer} hesitated, giving {self.player} time to dodge.",f"{self.computer} tripped over their own feet, missing the attack."]
                    print(random.choice(list_of_failed_attacksc))

                else:
                    computers_attack = random.choice(list(self.characters[self.computer]["attack_moves"].keys()))
                    computer_total = self.characters[self.computer]["attack_moves"][computers_attack]
                    computer_total -= random.randint(1, self.characters[self.player]["Defense"])
                    self.characters[self.player]["hp"] -= computer_total
                    print(f"\n{self.computer} used {computers_attack} causing {computer_total} damage to {self.player}.")
                    print(f"\n{self.player}'s Heath: {self.characters[self.player]["hp"]}.\n")
                players_turn = True


        if self.characters[self.player]["hp"] == 0:
            print(f"\n{self.computer.upper()} WON THE BATTLE!!\n- You Lose!")
        else:
            print(f"\n{self.player.upper()} WON THE BATTLE!!\n- You Won!")
        print("\nThanks For Playing!")
        exit()

    def choice_of_char(self):

        random_chars = random.sample(sorted(self.characters.keys()), 3)

        for i in random_chars:
            print(i)
            
        while True:
        
            choice = input("\nChoose Your Character!: ").title()

            if choice not in random_chars:

                print("Enter a Valid Choice!\n")
                continue

            else:
                self.player = choice
                self.computer = random.choice(sorted(self.characters.keys())) # computer picks a random char

                print(f"Your Character: {self.player}\nComputer's Character: {self.computer}\n")

                print(f"{self.computer}'s Stats:\n- Strength: {self.characters[self.computer]["strength"]}\n- Defense: {self.characters[self.computer]["Defense"]}\n- HP: {self.characters[self.computer]["hp"]}\n")
                print(f"{self.player}'s Stats:\n- Strength: {self.characters[self.player]["strength"]}\n- Defense: {self.characters[self.player]["Defense"]}\n- HP: {self.characters[self.player]["hp"]}\n")

                start_fight = input("Start (Yes/No): ").lower().strip()
                if start_fight != "yes":
                    exit()
                self.main_fight()
                

def main():
    try:
        c = MainGame()
        c.choice_of_char()
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
