import json
from google.colab import files, drive
from google import genai
from google.genai import types
from google_auth_oauthlib.flow import Flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import requests
import os
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
from rich.progress import track
import time
import base64

"""### Json"""






"""### Youtube"""







def download_thumbnails(image_data: dict) -> None:
  """Downloads Youtube Thumbnails"""
  folder_path: str = "/content/drive/MyDrive/MyVideoScraperProgram/Images"
  os.makedirs(folder_path, exist_ok=True)

  imagedata = image_data
  # Learning the rich lib
  for url, videoid in track(imagedata.items(), description="Fetching Thumbnails"):
    data = requests.get(url, timeout=15).content
    file_path: str = os.path.join(folder_path, f"{videoid}.jpg")

    with open(file_path, "wb") as file:
      file.write(data)


def filter_videos(data: dict,  tags: list, prompt: str):
  """Filters Videos"""

  search_tags: set = set(tags + [tag.capitalize() for tag in tags])
  client: object = genai.Client(api_key="AIzaSyBvlj8a013fkz3URDY3MKftQFWzjVtNUS0")
  filtered_videos: list = []

  for video in data.get("items"):
    title: str = video.get("snippet", "title"); print(title)
    if "#" not in title:
      print("Using Gemini")
      response: str = client.models.generate_content(
          model='models/gemini-2.5-flash',
          contents=types.Content(
              parts=[types.Part(file_data=types.FileData(file_uri=f'https://www.youtube.com/watch?v={video["snippet"]["resourceId"]["videoId"]}')),
                    types.Part(text=prompt)])).text

      if response == "T":
        filtered_videos.append(video)

    else:
      print("Has Tags")
      tags_in_title = set(title.split("#"))
      if search_tags & tags_in_title: # This is called Set Intersection a senior develoZZper method for fasters checking
        filtered_data.append(video)

  for video in filtered_videos:
    print(video)
    yield video

drive.mount("/content/drive")

if __name__ == "__main__":
  try:

    CLIENT_SECRET: str = "/content/drive/MyDrive/MyVideoScraperProgram/client_secret.json"
    SCOPE: list =     flow: object = Flow.from_client_secrets_file(CLIENT_SECRET, SCOPE, redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    youtube: object = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    
    prompt: str = '''
    check this video and see if its animation, anime, 2d, cartoon, Vtuber, 3D animation, anime edit, related.
    if it is YOUR ONLY AND ONLY RESPONSE YOU SHOULD GIVE IS "T" for True and if it isnt then just send "F" for False
    '''

    tags: list = [
        "animeweeb",
        "animehumor",
        "animejokes",
        "animememe",
        "anime",
        "edit",
        "animeeart",
        "animeedit",
        "edits",
        "manga",
        "animeshorts",
        "animemoments",
    ]
    filtered_data: dict = {}
    data: list = []

    playlist_id: str = input("Playlist ID: ").strip()
    destination: str = input("Destination (Playlist ID): ").strip()

    for response in track(get_video_data(playlist_id), description="Filtering Videos"):
      for video in filter_videos(data=response, tags=tags, prompt=prompt):
        data.append(video)
        j
          if res in video.get("snippet", "thumbnails"):
            filtered_data.update({video.get("snippet", "thumbnails", res, "url"): video})
            break
      time.sleep(0.1)

    # Add To Database
    add_to_database(data)

    # Download Images
    download_thumbnails(filtered_data)


  except InvalidGrantError:
    print("[InvalidGrantError]: The authorization code is incorrect, expired, or has already been used.")
  except FileNotFoundError as e:
    print(f"[FileNotFoundError]: {e}")
  except HttpError:
    print("Invalid Playlist ID Or Video ID. Please Check Your Entered ID.")
  except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
  except Exception as e:
    print(f"Exception: {e}")
    raise

