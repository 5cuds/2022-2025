import json

def verify_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        print(f"📊 --- SUMMARY ---")
        print(f"✅ Total unique videos: {len(data)}")
        
        if len(data) > 0:
            print(f"🆕 NEWEST: {data[0]['title']} ({data[0]['date']})")
            print(f"📜 OLDEST: {data[-1]['title']} ({data[-1]['date']})")
            
    except Exception as e:
        print(f"❌ Error reading file: {e}")

verify_data("asterlin_clean_likes7.json")
