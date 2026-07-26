import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json, requests, os, time


def create_database() -> None:
    """Creates A Json Database (File)"""
    # Check if "videos.json" exists. If not create it.
    if not os.path.exists("videos.json"):
        with open("videos.json", "w") as file:
            json.dump([], file)
        print(f'Created "videos.json"!')


def add_to_database(video_data: list) -> None:
    """Adds Video Data To Database""" 
    # Open videos.json
    with open("videos.json", "r") as file:
        data: list = json.load(file)
    
    # Add
    videodata = video_data
    print("Adding to the database..")
    for vid in videodata:
        data.append(vid)
    
    # Close
    with open("videos.json", "w") as file:
        json.dump(data, file, indent=4)


def get_video_data(playlist_id: str):
    """Get Video Data"""
    pagetoken: str = None
    
    # get all of the urls by 50 "Max"
    while True:
        response: dict = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=pagetoken).execute()

        # I need to learn more about generators lol
        yield response

        if not response.get("nextPageToken"): 
            break
        else: 
            pagetoken: str = response.get("nextPageToken")


def add_items_to_playlist(playlist_id: str, list_of_video_ids: list):
    print("Adding Videos To New Playlist") 
    
    # request and add videos
    for video_id in list_of_video_ids:
        response = youtube.playlistItems().insert(
                part="snippet",
                body={"snippet": {"playlistId": playlist_id,"resourceId": {"kind": "youtube#video", "videoId": video_id}}}
        ).execute()

    print("Done!")

    return 0


def download_thumbnails(response: dict) -> None:
    
    # Make Folder if not exists
    os.makedirs("Images", exist_ok=True)

    # Download image content 
    for item in response.get("items"):
        # Get the highest res
        for res in ("maxres", "standard", "high"):

            print(json.dumps(item["snippet", "thumbnails"], indent=4))

            if res in item["snippet", "thumbnails"]:
                print(res)

                url = item["snippet", "thumbnails", res, "url"]
                videoid = item["snippet", "resourseId", "videoId"]

                data = requests.get(url, timeout=15).content
                file_path: str = os.path.join("Images", f"{videoid}.jpg")
                print(data)
                # Create Image
                with open(file_path, "wb") as file:
                    file.write(data)




if __name__ == "__main__":
    
    try:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                "client_secret.json",
                ["https://www.googleapis.com/auth/youtube.force-ssl"]
                )
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

        for i in get_video_data("LL"):
            download_thumbnails(i)
            break
    except Exception as e:
        print(f"Error: {e}")
