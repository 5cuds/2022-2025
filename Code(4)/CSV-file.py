import time
import requests
from bs4 import BeautifulSoup

class Main:
    def __init__(self):
        self.game = None
        self.amount_of_players_scanned = 0
        self.bots = 0
        self.game_dev = None

        # List of known bot profile picture URLs
        self.bot_pfps = [
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-3C4FCD594FD42985940B352399CCB5F5-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-B0BC377DD12E2C376DB60257EF722B70-Png/150/150/AvatarHeadshot/Webp/noFilter",
            # Add the rest of the bot profile picture URLs here...
        ]

        div_tags = soup_yummy.find_all('div', class_="card-item")
                    print(div_tags)
                    for div in div_tags:
                        inner_divs = div.find_all('div')
                        for inner_div in inner_divs:
                            spans = inner_div.find_all('span')
                            for span in spans:
                                inner_spans = span.find_all('span')
                                for inner_span in inner_spans:
                                    img_tags = inner_span.find_all('img')
                                    for img in img_tags:

                                        print(img)
                                        if str(img) in self.bot_pfps:
                                            self.bots += 1
                                        self.amount_of_players_scaned += 1

                    print("Scanned", self.amount_of_players_scaned)
                    print("Bots", self.bots)

    def add_game_to_check_for_bots(self):
        print("Before You Enter The Game URL\nWe Need The URL Of It!")
        print("Example: https://www.roblox.com/games/12345678/GameName")
        print("Type 'exit' to return.")
        
        while True:
            try:
                get_url = input("> ").strip()
                
                if not get_url:
                    print("Please enter a valid URL!")
                    continue
                
                if get_url.lower() == "exit":
                    return
                
                if "roblox.com/games/" not in get_url:
                    print("This doesn't look like a valid Roblox game URL. Please try again.")
                    continue
                
                self.check_for_bots(get_url)
            
            except Exception as e:
                print(f"(Exception): {e}")

    def check_for_bots(self, url):
        # Correct the URL if it includes "#!/about"
        url = url.replace("#!/about", "#!/game-instances")
        
        try:
            # Fetch the game instances page
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error fetching the page. Status code: {response.status_code}")
                return
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all 'card-item' divs
            card_items = soup.select(".card-item")
            if not card_items:
                print("No players found on the page. Make sure the URL is correct.")
                return
            
            for card in card_items:
                img_tags = card.select("img")
                for img in img_tags:
                    img_url = img.get("src")
                    if img_url in self.bot_pfps:
                        self.bots += 1
                    self.amount_of_players_scanned += 1
            
            print(f"Scanned {self.amount_of_players_scanned} players.")
            print(f"Bots found: {self.bots}")
            
            # Fetch the game info
            self.fetch_game_info(url)
        
        except Exception as e:
            print(f"(Exception): {e}")

    def fetch_game_info(self, url):
        # Fetch the "about" page for game info
        about_url = url.replace("#!/game-instances", "#!/about")
        response = requests.get(about_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            self.game = soup.find("h1", class_="game-name").text.strip() if soup.find("h1", class_="game-name") else "Unknown Game"
            self.game_dev = soup.find("a", class_="text-name text-overflow").text.strip() if soup.find("a", class_="text-name text-overflow") else "Unknown Developer"
            self.view_stats()
        else:
            print(f"Failed to fetch game info. Status code: {response.status_code}")
    
    def view_stats(self):
        print("\n========= Game Stats =========")
        print(f"Game: {self.game}")
        print(f"Developer: {self.game_dev}")
        print(f"Total Players Scanned: {self.amount_of_players_scanned}")
        print(f"Total Bots Found: {self.bots}")
        print("==============================")

def main():
    app = Main()
    app.add_game_to_check_for_bots()

if __name__ == "__main__":
    main()
