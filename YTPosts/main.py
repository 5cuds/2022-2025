from playwright.sync_api import sync_playwright
from playwright._impl._errors import TimeoutError as PlayTE
from bs4 import BeautifulSoup
import time
import requests
import os
import json


def turn_handles_to_urls(channelHandles: list) -> list: 
    list_of_urls = []
    for handle in channel_handles:
        url = f"https://www.youtube.com/{handle}/posts"
        list_of_urls.append(url)

    return list_of_urls


def get_handles_from_file(file_path: str) -> list:
    with open(file_path, "r") as file: return file.readlines()


def create_folders(rootfolderpath: str, list_of_handles: list) -> None:
    if not os.path.exists(root_folder_path): os.mkdir(root_folder_path)
    
    handles = list_of_handles
    for handle in handles:
        filepath = os.path.join(root_folder_path, handle.strip("@"))
        if not os.path.exists(filepath): os.mkdir(filepath)
    
    # Create "Config.json" file with pre-set values.
    # with open("config.json", "w") as file: json.dumps()

def scrap_the_image_links(html_data: str) -> list:
    pass


def get_html_contents(url: str) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.get_by_text("Playlists").click()
        page.wait_for_timeout(5000); browser.close()


def download_image(url: str) -> None:
    pass


 


if __name__ == "__main__":
    root_folder_path = r"C:\Users\Windows\Pictures\YTPosts"
    try:
        create_folders(rootfolderpath=root_folder_path, list_of_handles=["@BobGames", "@LukeTheNotable"])
        # get_html_contents(url="https://www.youtube.com/@LukeTheNotable/posts")
    except PlayTE: print("[Playwright]: Timeout.")
    except Exception as e: print(f"[Exception]: {e}")
