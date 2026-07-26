import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Scopes required for managing playlists
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPs verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_4.json"

    # Authenticate the user
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, SCOPES)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    source_playlist_id = "PLXpswICW4-AuMAQDus3s_9KTziPZOE7-q"
    target_playlist_id = "PLdbUQU1m9Bv8TkCqX6rJceMD1Q0Ii3smW"

    # 1. Fetch items from the source playlist
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=50,
        playlistId=source_playlist_id
    )
    response = request.execute()

    for item in response.get("items", []):
        print("Hello, World")
        video_id = item["contentDetails"]["videoId"]
        playlist_item_id = item["id"] # Needed to delete from source
        video_title = item["snippet"]["title"]

        print(f"Moving: {video_title}...")

        # 2. Add video to the target playlist
        add_request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": target_playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )
        add_request.execute()

        # 3. Remove video from the source playlist
        delete_request = youtube.playlistItems().delete(
            id=playlist_item_id
        )
        delete_request.execute()
        
    print("✅ Successfully moved videos!")

if __name__ == "__main__":
    main()
