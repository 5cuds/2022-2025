import os
import re
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def download_playlist_thumbnails():
    user_input = input("🔗 Enter Playlist URL or ID: ").strip()
    # Simple regex to get the ID
    playlist_id = re.search(r"list=([^&]+)", user_input).group(1) if "list=" in user_input else user_input
    
    # Auth setup
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = build("youtube", "v3", credentials=credentials)
    
    folder = "YT_Thumbnails"
    if not os.path.exists(folder): os.makedirs(folder)

    next_page_token = None
    count = 0

    while True:
        res = youtube.playlistItems().list(part="snippet", playlistId=playlist_id, maxResults=50, pageToken=next_page_token).execute()
        
        for item in res['items']:
            count += 1
            title = item['snippet']['title']
            thumbs = item['snippet']['thumbnails']
            
            best = (thumbs.get('maxres') or thumbs.get('standard') or thumbs.get('high') or thumbs.get('default'))
            
            if best:
                url = best['url']
                # --- SMART EXTENSION CHECK ---
                # This checks if the URL says .webp or .jpg
                extension = ".webp" if ".webp" in url.lower() else ".jpg"
                
                clean_title = re.sub(r'[\\/*?:"<>|]', "", title)
                file_path = os.path.join(folder, f"{count:03d}_{clean_title}{extension}")
                
                img_data = requests.get(url).content
                with open(file_path, 'wb') as f:
                    f.write(img_data)
                print(f"✅ Saved: {file_path}")

        next_page_token = res.get('nextPageToken')
        if not next_page_token: break

    print(f"\n🎉 Finished! Check the '{folder}' folder, Nihal!")

if __name__ == "__main__":
    download_playlist_thumbnails()
