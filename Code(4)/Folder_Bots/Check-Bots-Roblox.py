import time, datetime, requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



# Div ID: card-item


class Main:
    def __init__(self):
        self.game = None
        self.amount_of_players_scaned = 0
        self.bots = 0
        self.game_dev = None

        # I feel like a clown by doing this by hand :(
        self.bot_pfps = (
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-3C4FCD594FD42985940B352399CCB5F5-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-B0BC377DD12E2C376DB60257EF722B70-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-3754C57A7F59F2C3E5E7F6B139BA3834-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-BF48E8C1886F82D41660085301CA3156-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-9FA002152204E8967EE38A77894FFA6E-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-899C22C773F6FADC09C671A69E925D51-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-B4BBE062FEDC1CA9FF6C74611D9159C0-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-2D3850B685FA78BFAAAB043AAF1F4476-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-FB02C93190E2EAA926BF05FE338A54C8-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-F4E257BB13870A53DB6E3D24FC1D4D65-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-9ADEEBC874F8DA124659EFB5D81D24F9-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-292DFAF213DC839F116ABE0B1E6FCA46-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-0A4833DCEDF770265E7BB55B87E3AAB9-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-6D5ECF5B1D1905FC742E6EF84DFBAAF8-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-6F0AA45157282264409E88F7D74F8A4D-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-B8D0CD7D3686FB6F74342DF497695029-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-5A8291932C39874193F3620D0855937B-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-D4A3C9349427CFD2223583B979B516A9-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-4A19286D4D59BF7E8A3D7DA7E4D55240-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-8D86A5CF750F66AEA0C66EC217A6B512-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-81F4466FE1C4916092B7A976A2608583-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-6D99B8177969BEE3145344B42788B9E9-Png/150/150/AvatarHeadshot/Webp/noFilter",
            "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-55C67281189D3FBAE3B42AAB8D1FA631-Png/150/150/AvatarHeadshot/Webp/noFilter"
        )
        

    def add_game_to_check_for_bots(self):
        print("Enter An Roblox Game.")
        print("Example: https://www.roblox.com/games/12345678/GameName")
        print("Type 'exit' to return.\n====================")

        while True:
                try:
                    # Get the input
                    get_url = input("Enter The Games URL: ").upper()

                    # check if the user input is valid
                    if not get_url:
                        print("Please Enter A Valid URL!")
                        continue
                    elif get_url == "EXIT":
                        return
                    elif "ROBLOX.COM" not in get_url:
                        print("This doesn't look like a valid Roblox game URL. Please try again.")
                        #continue
                    
                    # Starts checking the game
                    self.check_for_bots(get_url)

                except Exception as e:
                     print(f"(Exception): {e}")
                     

    def calculate(self):
        pass

    def check_for_bots(self, gimme_url):
            url = gimme_url


            try:
                
                driver = webdriver.Chrome()
                driver.get(url)

                time.sleep(15)
                
                soup = BeautifulSoup(driver.page_source, "html.parser")

                for i in soup.find_all("img"):
                    print(i.get("src"))

            except Exception as err:
                 print(f"(Exception): {err}")
                 return


    def view_stats(self):
        print(f"(========= {self.game} =========)")
        print(f" Game By {self.game_dev}")


def main():
    d = Main()
    d.add_game_to_check_for_bots()

if __name__ == "__main__":
    main()