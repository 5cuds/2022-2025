import json
import os
from collections import Counter
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# --- 1. OAUTH2 AUTHENTICATION ---
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)

# --- 2. TAG SCRAPER & COUNTER ---
def scrape_playlist_tags(playlist_id):
    youtube = get_authenticated_service()
    all_tags = []
    next_page_token = None

    print(f"📡 Authorized access started for Playlist: {playlist_id}...")

    while True:
        pl_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()
        video_ids = [item['contentDetails']['videoId'] for item in pl_response['items']]

        v_request = youtube.videos().list(
            part="snippet",
            id=",".join(video_ids)
        )
        v_response = v_request.execute()

        for video in v_response['items']:
            # PULLING BIGGER KEYWORDS (Anime, Edits, Manga)
            tags = video['snippet'].get('tags', [])
            all_tags.extend([t.lower() for t in tags])

        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break

    # Count and Save to JSON
    tag_counts = dict(Counter(all_tags))
    sorted_stats = dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True))

    output = {
        "status": "Success",
        "total_videos_scanned": len(video_ids),
        "tags": sorted_stats
    }

    with open("nihal_tags_v2.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"🏁 Done! {len(tag_counts)} unique tags saved to JSON.")

if __name__ == "__main__":
    # Replace with your playlist ID
    scrape_playlist_tags("LL")
