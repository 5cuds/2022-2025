import json
import yt_dlp

def scrape_main_account():
    ydl_opts = {
    'quiet': False,
    'extract_flat': False,
    'dump_single_json': True,
    'cookiefile': 'cookies.txt', 
    'ignoreerrors': True,
    # ADD THESE TWO LINES:
    'extract_flat': 'in_playlist', # Forces deeper extraction of playlist items
    'playlist_items': '1-5000',    # Explicitly asks for the first 5000 items
    }

    print("🛰️ Something account: itsngmyt@gmail.com")
    print("🚀 Starting deep scrape. This will ignore the 1000-video limit!")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Using the direct URL for likes
            result = ydl.extract_info("https://www.youtube.com/playlist?list=LL", download=False)
            
            video_list = []
            if result and 'entries' in result:
                for entry in result['entries']:
                    if entry:
                        video_list.append({
                            "link": f"https://www.youtube.com/watch?v={entry.get('id')}",
                            "title": entry.get('title'),
                            "date": entry.get('upload_date') # Format: YYYYMMDD
                        })

                # Save the final file for your C parser
                with open("itsngmyt_likes3.json", "w", encoding="utf-8") as f:
                    json.dump(video_list, f, indent=4, ensure_ascii=False)
                
                print(f"\n✅ SUCCESS! Found {len(video_list)} videos.")
            else:
                print("❌ No videos found. Is your cookies.txt file in the right folder?")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    scrape_main_account()
