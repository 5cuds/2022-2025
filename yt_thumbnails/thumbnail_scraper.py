import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import os, requests, time, hashlib


def create_folders_for_images(channels: list) -> None:
    if not os.path.exists(root_folder_path):
        os.mkdir(root_folder_path)
    for channel in channels:
        filepath = os.path.join(root_folder_path, channel.strip("@."))
        if not os.path.exists(filepath): os.mkdir(filepath)


def get_uploads_playlist_id(channel: str) -> str:
    """Returns a dict of playlist id's. DICT: Key\Value (Channel Name: Playlist ID)""" 
    response = youtube.channels().list(
            part="contentDetails",
            forHandle=channel,
            maxResults=50
        ).execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_thumbnail_urls_from_playlist(playlist_Id: str, channelname: str) -> list:
    next_page_token = None
    urls = []
        
    while True:
        response = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_Id,
            maxResults=50,
            pageToken=next_page_token).execute()
        
        for video in response["items"]:
            list_of_res = ("maxres", "standard", "high", "medium", "default")
            for res in list_of_res:
                if res in video["snippet"]["thumbnails"]: urls.append(video["snippet"]["thumbnails"][res]["url"]);break

        if not response.get('nextPageToken'): break
        else: next_page_token = response["nextPageToken"]
    
    return urls


def download_images(channelname: str, urls: list) -> None:
    list_of_urls = urls
    for url in list_of_urls:

        image_content = requests.get(url, timeout=30).content
        folderpath = os.path.join(root_folder_path, channelname.strip("@"))
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
        filepath = os.path.join(folderpath, f"{url_hash[0:5]}.jpeg")

        if not os.path.exists(filepath):
            with open(filepath, "wb") as file: file.write(image_content)

# PLxzM8KCqXhzdCfNyBjinNeMls66d0YZas = Gooner Thumbnails Playlist

if __name__ == "__main__":    
    root_folder_path = r"C:\Users\Windows\Pictures\Downloaded YT Thumbnails"
    channels_downloaded = []
    channels = []
    print("1) Channels\n2) Own Playlists (AuthO 2.0 Required)")

    try:
        if int(input("> ").strip()) == 1:
            api_key = "AIzaSyCf9a2clpqaX4pmSFym-5-0eJ7hZHac19Q"
            youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

            filepath_of_list_of_channels  = str(input("(Enter the path of the text file containing the channels.) => ")).strip()
            with open(filepath_of_list_of_channels, "r") as file: channels = [i.strip() for i in file.readlines()]
            channels_scraped = 0
            create_folders_for_images(channels)
        
            for channel in channels:
                playlistId = get_uploads_playlist_id(channel)
                urls = get_thumbnail_urls_from_playlist(playlistId, channel)
                download_images(channel, urls);time.sleep(2.5)
                channels_downloaded.append(channel);print(f"{len(channels_downloaded)} Out of {len(channels)} channels are scraped.", end="\r")

        else:        
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file("client_secret.json", ["https://www.googleapis.com/auth/youtube"])
            credentials = flow.run_local_server(port=0)
            youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
            playlist_ID = input("Playlist ID => ").strip()
            folder_name = input("Name Of The Folder => ").strip()
            if not folder_name: folder_name = f"folder_{len(os.listdir(root_folder_path))}"
            
            create_folders_for_images([f"@{folder_name}"]);print("Created Folder!")
            urls = get_thumbnail_urls_from_playlist(playlist_Id=playlist_ID, channelname=f"@{folder_name}");print("Got Urls!")
            download_images(channelname=f"@{folder_name}", urls=urls);print("Downloaded Thumbnails!") 
    
    except KeyError as e: print(f"Daily quota exceeded.\nError Message: {e}")
    except HttpError as e: print("Invalid Playlist Id. Please check your id.\nError Message: {e}")
    except FileNotFoundError as e: print(f"File Not Found!\nError Message: {e}")
    except requests.exceptions.Timeout: print("[Requests]: Timeout.")
    except requests.exceptions.ConnectionError: print("[Requests]: Failed to fetch the thumbnail URL. Check your internet connection.")
    except Exception as e: print(f"[Exception]: {e}")

    finally:
        print()
        print(f"Sucessfully downloaded all of the thumbnails from..")
        for c in channels_downloaded: print(c)
        print("Unsucessful channels..")
        for u in channels:
            if u in channels_downloaded: continue
            print(u)




