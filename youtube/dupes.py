import json

with open("my_actual_likes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract just the video IDs
ids = [video['id'] for video in data]
total_count = len(ids)
unique_count = len(set(ids))

if total_count == unique_count:
    print(f"✅ Clean Data! All {total_count} videos are unique.")
else:
    print(f"⚠️ Found {total_count - unique_count} duplicates!")
    # Create a new list without dupes
    seen = set()
    unique_data = []
    for video in data:
        if video['id'] not in seen:
            unique_data.append(video)
            seen.add(video['id'])
    
    with open("my_clean_likes.json", "w", encoding="utf-8") as f:
        json.dump(unique_data, f, indent=4)
    print(f"🧹 Saved {len(unique_data)} unique videos to 'my_clean_likes.json'")
