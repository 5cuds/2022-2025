import google_auth_oauthlib.flow
import googleapiclient.discovery

# 1. Fill these in!
CLIENT_SECRETS_FILE = "client_secret_4.json" # Your downloaded OAuth file
SOURCE_PLAYLIST_IDS = ["PLxzM8KCqXhzcdWxtuQy7eZZilsUcIaFV-", "PLxzM8KCqXhzc0r_RER0b5B3YNOq0L0rNR", "PLxzM8KCqXhze36AVdboxGpr2hQslDTOMv",
                       "PLxzM8KCqXhzdpOCCgFVbZtsVmk9Sni0jV", "PLXpswICW4-AuEUaqkNNzJtkTmuMobzFYU"]

MASTER_PLAYLIST_ID = "PLdbUQU1m9Bv_Wo2Et_YaeI09o-3JYv8Yw"

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def get_video_data(youtube, playlist_id):
    videos = {} # Using a dict to map ID -> Title
    next_page_token = None
    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response['items']:
            v_id = item['contentDetails']['videoId']
            v_title = item['snippet']['title']
            videos[v_id] = v_title
        next_page_token = response.get('nextPageToken')
        if not next_page_token: break
    return videos

def main():
    youtube = get_service()
    
    print("🔍 Fetching Master Playlist...")
    master_videos = get_video_data(youtube, MASTER_PLAYLIST_ID)
    
    all_missing = []
    
    for src_id in SOURCE_PLAYLIST_IDS:
        print(f"📂 Checking Source: {src_id}...")
        source_videos = get_video_data(youtube, src_id)
        
        for v_id, v_title in source_videos.items():
            if v_id not in master_videos:
                all_missing.append(f"{v_title} (https://youtu.be/{v_id})")

    print("\n--- 📝 MISSING VIDEOS ---")
    if not all_missing:
        print("✅ Everything is synced! Your master list is perfect. 😎")
    else:
        for vid in all_missing:
            print(f"❌ {vid}")
        print(f"\nTotal missing: {len(all_missing)}")

if __name__ == "__main__":
    main()
