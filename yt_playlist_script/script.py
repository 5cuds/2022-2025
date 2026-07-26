from google import genai
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import json, time
from google.genai import types


def filter_video(videoid: dict, tags: tuple) -> list:
    
    filtered_urls = {}
    client = genai.Client(api_key="AIzaSyAceqOmyvATlMDc47yG9FKD12WU_TQKqU")
    
    print("Gemini Filtering Video Ids..")
    video_ids = videoids
    for vid_id, kind in video_ids.items():
        url = f"https://www.youtube.com/watch?v={vid_id}"
        response = client.models.generate_content(model='models/gemini-2.5-flash',contents=types.Content(parts=[
            types.Part(file_data=types.FileData(file_uri=url)),
            types.Part(text=GEMINI_PROMPT)]))
        if "T" == response.text: filtered_urls.update({vid_id: kind})

    return filtered_urls

ZZ
def add_videos_to_playlist(playlistId: str, list_of_ids: dict) -> None:
    print("Adding Filtered Videos To New Playlist..")
    ids = list_of_ids
    for vid_id, kind in ids.items():
        response = youtube.playlistItems().insert(
            part="snippet",
            body={"snippet": {"playlistId": playlistId, "resourceId": {"videoId": vid_id, "kind": kind}}}
        ).execute()


if __name__ == "__main__":
    try:
        GEMINI_PROMPT = """ 
        """
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file("client_secret.json", ["https://www.googleapis.com/auth/youtube"])
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)



    except HttpError as e: print(f"Http Error: {e}") 
    except FileNotFoundError as e: print(f"File Not Found!\nError Message: {e}")
    except KeyError as e: print(f"Daily quota exceeded.\nError Message: {e}")
    except Exception as e: print(f"[Exception]: {e}")

