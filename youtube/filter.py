import json, os, csv
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import google.generativeai as genai

# --- 1. THE NIHAL-CLEANSED KEYWORDS (Extracted from nihal_tags_v2.json) ---
ANIME_MANGA = ["anime", "manga", "manhwa", "manhua", "webtoon", "jjk", "jujutsu kaisen", "gojo", "blue lock", "bluelock", "isagi", "recap", "anime recap"]
GACHA_VTUBER = ["genshin", "hoyoverse", "mihoyo", "wuwa", "wuthering waves", "hsr", "star rail", "zzz", "zenless", "vtuber", "miku", "hololive"]
EDITS_VIBES = ["edit", "animeedit", "amv", "sakuga", "animation meme", "phonk", "lofi", "aesthetic", "velocity"]

WHITELIST = ANIME_MANGA + GACHA_VTUBER + EDITS_VIBES

# --- 2. AI CONFIGURATION (5-KEY ROTATION) ---
GEMINI_KEYS = ["AIzaSyAPieJtXP4MD_MJlUACZeJ-W1VtKwmecdw", "AIzaSyBdcFBIfRqQRpGI0oEmkiQq4h4uyVhoRLk", "AIzaSyBcifsosKZeSiRZFaktWKQGPyW5x9zO_yc", "AIzaSyALi8DZlh91CEnKAhQ4q-lmWzDmDg6_TMs", "AIzaSyCuo2-ssKw9sFQF1AaSF6BOljCZyilisIU", "AIzaSyAuvEAFKTatuDirW7TLhvCzyvLktJYyVgs"]
current_ai_key = 0

SYSTEM_PROMPT = """
Strict Auditor Mode: Is this title related to Anime, Manga, Gacha Games (Genshin/Star Rail/Wuwa), Vtubers, or Fan Edits?
IGNORE: Programming (Python/C++), Sports (Messi/Football), Generic Gaming (Minecraft/Roblox), and Memes.
OUTPUT: Only 'Yes' or 'No'.
"""

def ask_ai_strict(help):
    global current_ai_key
    genai.configure(api_key=GEMINI_KEYS[current_ai_key])
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        response = model.generate_content(f"{SYSTEM_PROMPT}\nTitle: {title}").text.strip()
        return "Yes" in response
    except:
        current_ai_key = (current_ai_key + 1) % len(GEMINI_KEYS)
        return False

# --- 3. AUTHENTICATION HELPER ---
def get_yt_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/youtube.readonly'])
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', ['https://www.googleapis.com/auth/youtube.readonly'])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

# --- 4. MAIN SCRAPER ENGINE ---
def run_final_audit(playlist_id):
    youtube = get_yt_service()
    
    with open("godhelpus.csv", "w", newline="", encoding="utf-8") as pass_f, \
         open("lifeismeaningless.csv", "w", newline="", encoding="utf-8") as fail_f:
        
        passed = csv.writer(pass_f)
        failed = csv.writer(fail_f)
        
        header = ["Title", "URL", "Method"]
        passed.writerow(header)
        failed.writerow(header)

        print(f"📡 Scanning 1,194+ items in Playlist: {playlist_id}...")

        request = youtube.playlistItems().list(part="snippet,contentDetails", playlistId=playlist_id, maxResults=50)
        while request:
            response = request.execute()
            for item in response['items']:
                title = item['snippet']['title']
                url = f"https://www.youtube.com/watch?v={item['contentDetails']['videoId']}"
                t_low = title.lower()

                # STEP 1: KEYWORD FAST-PASS (Only for specific Nihal-approved tags)
                if any(k in t_low for k in WHITELIST):
                    passed.writerow([title, url, "Keyword Approved"])
                    continue
                
                # STEP 2: AI AUDIT (For titles that are vague or complex)
                if ask_ai_strict(title):
                    passed.writerow([title, url, "AI Verified"])
                else:
                    failed.writerow([title, url, "Rejected"])

            request = youtube.playlistItems().list_next(request, response)

    print("🏁 Processing complete! Check godhelpus.csv for the filtered results. 🦄🚀")

if __name__ == "__main__":
    run_final_audit("LL")
