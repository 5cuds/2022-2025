import random
import time


class Club:

    def __init__(self) -> None:

        self.list_of_clubs = [
            "Barcelona", "Real Madrid", "Manchester United", "Liverpool", "Chelsea", "Bayern Munich", "Paris Saint-Germain",
            "Juventus", "Milan", "Inter Milan", "Arsenal", "Manchester City", "Atlético Madrid", "Borussia Dortmund",
            "Tottenham Hotspur", "Roma", "Ajax Amsterdam", "Benfica", "Porto", "Galatasaray", "Celtic", "Rangers",
            "SL Benfica", "Valencia", "Marseille", "Shakhtar Donetsk", "Zenit St. Petersburg", "Napoli", "Everton",
            "Lazio", "Sevilla", "Portimonense", "Villarreal", "Real Sociedad", "Wolverhampton Wanderers", "Monaco",
            "Real Betis", "Sporting", "Fenerbahçe", "Besiktas", "Boca Juniors", "River Plate", "Club América",
            "Chivas Guadalajara", "Santos Laguna", "Cruz Azul", "Pumas UNAM", "Atalanta", "Bologna", "Hellas Verona",
            "Lille", "Lyon", "Saint-Étienne", "Strasbourg", "Bordeaux", "Braga", "Marítimo", "Belenenses",
            "Tigres UANL", "Monterrey", "Atlas", "Toluca", "Juárez", "Pachuca", "Xolos", "Palmeiras", "Sao Paulo",
            "Internacional", "Grêmio", "Flamengo", "Fluminense", "Atlético Mineiro", "Vasco da Gama", "Botafogo", "Corinthians",
            "Cruzeiro", "Santos", "Nacional", "Peñarol", "Defensa y Justicia", "Independiente", "Racing Club", "San Lorenzo",
            "Argentinos Juniors", "Colón", "Universitario", "Alianza Lima", "Universidad de Chile", "Emelec", "Barcelona SC",
            "Liga de Quito", "Delfín", "Deportivo Cali", "Atlético Junior", "Millonarios", "Santa Fe", "Once Caldas", "Huila"
        ]
       



        self.off_club = None

        self.players = [
            "Lionel Messi - 🇦🇷", "Cristiano Ronaldo - 🇵🇹", "Neymar Jr. - 🇧🇷", "Kylian Mbappé - 🇫🇷", "Mohamed Salah - 🇪🇬",
            "Kevin De Bruyne - 🇧🇪", "Luka Modrić - 🇭🇷", "Harry Kane - 🇬🇧", "Bruno Fernandes - 🇵🇹", "Eden Hazard - 🇧🇪",
            "Paul Pogba - 🇫🇷", "Raheem Sterling - 🇬🇧", "Sadio Mané - 🇸🇳", "Bernardo Silva - 🇵🇹", "Phil Foden - 🇬🇧",
            "Jadon Sancho - 🇬🇧", "Antoine Griezmann - 🇫🇷", "Marcus Rashford - 🇬🇧", "Karim Benzema - 🇫🇷", "Thomas Müller - 🇩🇪",
            "Jack Grealish - 🇬🇧", "Mason Mount - 🇬🇧", "Heung-min Son - 🇰🇷", "Joshua Kimmich - 🇩🇪", "Paulo Dybala - 🇦🇷",
            "Luis Suárez - 🇺🇾", "Virgil van Dijk - 🇳🇱", "Manuel Neuer - 🇩🇪", "Sergio Ramos - 🇪🇸", "Gareth Bale - 🇬🇧",
            "Zlatan Ibrahimović - 🇸🇪", "Robert Lewandowski - 🇵🇱", "Ederson - 🇧🇷", "Casemiro - 🇧🇷", "Jorginho - 🇮🇹",
            "Frenkie de Jong - 🇳🇱", "Son Heung-min - 🇰🇷", "N’Golo Kanté - 🇫🇷", "Jan Oblak - 🇸🇮", "João Félix - 🇵🇹",
            "Mauro Icardi - 🇦🇷", "Kante - 🇫🇷", "James Rodríguez - 🇨🇴", "Lautaro Martínez - 🇦🇷", "Ciro Immobile - 🇮🇹",
            "Thiago Alcântara - 🇪🇸", "Marco Reus - 🇩🇪", "Hakim Ziyech - 🇲🇦", "Lucas Hernández - 🇫🇷", "Timo Werner - 🇩🇪",
            "Gianluigi Donnarumma - 🇮🇹", "Dani Carvajal - 🇪🇸", "Álvaro Morata - 🇪🇸", "Kasper Schmeichel - 🇩🇰", "Christian Pulisic - 🇺🇸",
            "Angel Di María - 🇦🇷", "David De Gea - 🇪🇸", "Alejandro Balde - 🇪🇸", "Riyad Mahrez - 🇩🇿", "Jules Koundé - 🇫🇷"
        ]


    def choice(self):

        print('Pick a Club!\n===================')
        limit_3 = random.sample(self.list_of_clubs, 3)

        for i in limit_3:
            print(i)

        while True:
            club = input("===================\n> ").title()
            if club not in limit_3:
                print("Enter a Valid club!")
                continue
            else:
                self.off_club = club
                return


    def Main_Match(self):

        d = random.randint(1, 15)
        print("\nWaiting For a Match..")

        time.sleep(d)

        random_club = random.choice(self.list_of_clubs)

        print(f"Match Found!\n{self.off_club} VS {random_club}\n")

        time.sleep(1.25)
        print(f"Match started!\n0 - {self.off_club}|00:00|{random_club} - 0\n")

        score_team1 = 0
        score_team2 = 0
        time_set = 1

        if time_set == 90:

            print(f"Match Ended!\n{score_team1} - {self.off_club}|{score_timer}:{secs_score_time}|{random_club} - {score_team2}")
            if score_team1 > score_team2:
                print(f"{self.off_club} Won the Match!")

            elif score_team1 == score_team2:
                    print("Is a Draw")

            else:
                print(f"{random_club} Won the Match!")
            return

        while True:
            random_happeings = random.choice(["Free Kick", "Goal", "Penalty", "Foul"])


            score_timer = random.randint(time_set, 90)
            secs_score_time = random.randint(1, 59)
            time.sleep(score_timer)


            if random_happeings == "Goal":


                if random.choice(["Heads", "Tails"]) == "Heads":
                    print(f"YOUR TEAM SCORED! \nGOAL BY {random.choice(self.players)}!\n")

                    score_team1 += 1

                else:

                    print(f"Your Team Got Scored on! \nGOAL BY {random.choice(self.players)}!\n")

                    score_team2 += 1

            elif random_happeings == "Free Kick":

                if random.choice(["Heads", "Tails"]) == "Heads":
                    print("Your Team Got a Freekick!\n")

                    miss_or_goal = random.randint(1, 5)
                    if miss_or_goal == 3:

                        print(f"{random.choice(self.players).upper()} SCORED THE FREEKICK!\n")
                        score_team1 += 1
                    else:
                        print(f"{random.choice(self.players).upper()} Missed!\n")
                else:
                    print(f"{random_club} Got a Freekick!\n")
                    miss_or_goal1 = random.randint(1, 5)
                    if miss_or_goal1 == 3:

                        print(f"{random.choice(self.players).upper()} SCORED THE FREEKICK!\n")
                        score_team2 += 1
                    else:
                        print(f"{random.choice(self.players).upper()} Missed!\n")

            elif random_happeings == "Penalty":

                if random.choice(["Heads", "Tails"]) == "Heads":

                    taker = random.choice(self.players)
                    print(f"{random.choice(self.players)} Fouled {random.choice(self.players)} In the Penalty box!\nIt is a Penalty.\n")

                    time.sleep(0.45)
                    print(f"Penalty Taker is {taker}.")

                    if random.randint(1, 4) == 2:
                        print(f"{taker} SCORED THE PENALTY!\n")
                        score_team1 += 1

                    else:

                        msg = ["GOALKEEPER SAVED IT!", f"{taker} Missed the penalty..\n"]
                        print(random.choice(msg))
                else:
                    print(f"{random.choice(self.players)} Fouled {random.choice(self.players)} In the Penalty box!\nIt is a Penalty.\n")

                    if random.randint(1, 4) == 2:
                        print(f"{random.choice(self.players)} SCORED THE PENALTY!\n")
                        score_team2 += 1
                    else:
                        msg1 = ["GOALKEEPER SAVED IT!", f"{random.choice(self.players)} Missed the penalty..\n"]
                        print(random.choice(msg1))

            else:
                yellow_cards = 0
                yellow_team = 0
                if random.choice(["Heads", "Tails"]) == "Heads":
                    print(f"{random.choice(self.players)} tacked {random.choice(self.players)}!\n")
                    time.sleep(1.25)
                    print("Ref Going to the VAR..")
                    time.sleep(1.25)
                    if random.choice(["Red card", "Yellow Card"]) == "Red Card":
                        print(f"It's A RED CARD! -1 Goal!\n")
                        score_team1 -= 1
                    else:
                        if yellow_cards == 2:
                            print("IT'S SEC YELLOW!\n")
                            score_team1 -= 1
                            yellow_cards = 0
                        else:
                            print("It's a Yellow Card!\n")
                            yellow_cards += 1
                else:
                    print(f"{random.choice(self.players)} tacked {random.choice(self.players)}\n!")
                    time.sleep(1.25)
                    print("Ref Going to the VAR..")
                    time.sleep(1.25)
                    if random.choice(["Red card", "Yellow Card"]) == "Red Card":
                        print(f"It's A RED CARD! -1 Goal! ")
                        score_team1 -= 1
                    else:
                        if yellow_cards == 2:
                            print("IT'S SEC YELLOW!\n")
                            score_team1 -= 1
                            yellow_team = 0
                        else:
                            print("It's a Yellow Card!\n")
                            yellow_team += 1
                        
                    

            print(f"{score_team1} - {self.off_club}|{score_timer}:{secs_score_time}|{random_club} - {score_team2}\n")
            time_set = score_timer
            continue

def main():
    club = Club()
    club.choice()
    club.Main_Match()
if __name__ == "__main__":
    main()

