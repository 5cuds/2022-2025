import os
import pandas as pd
import requests
import json
from playwright.sync_api import sync_playwright

# --- CONFIG ---
CSV_FILE = "post_votes.csv" 
DOWNLOAD_PATH = "reddit_final_archive"

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

def scrape_reddit_correctly():
    try:
        df = pd.read_csv(CSV_FILE)
        # Ensure we use the full URL
        links = [l if l.startswith('http') else f"https://www.reddit.com{l}" for l in df['permalink'].tolist()]
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    with sync_playwright() as p:
        # 1. Launch with 'headless=False' to bypass basic bot detection
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = context.new_page()

        print(f"🚀 Nihal, starting the deep scan for {len(links)} posts...")

        for idx, link in enumerate(links):
            print(f"📖 [{idx+1}/{len(links)}] Opening: {link}")
            try:
                # 2. Go to the page and wait for it to actually load
                page.goto(link, wait_until="networkidle", timeout=60000)
                page.wait_for_timeout(3000) # Give it a moment to render galleries

                # 3. Targeted extraction: Find the main media
                # This selector targets the high-res images in the new UI
                img_elements = page.query_selector_all('shreddit-aspect-ratio img, .ImageBox-image, [data-testid="post-content"] img')
                
                found_urls = []
                for img in img_elements:
                    src = img.get_attribute('src')
                    if src and ("redd.it" in src or "external-preview" in src):
                        # Get the original high-res URL
                        clean_url = src.split('?')[0].replace("preview.redd.it", "i.redd.it")
                        if clean_url not in found_urls:
                            found_urls.append(clean_url)

                # 4. Download logic
                if not found_urls:
                    print("      ℹ️ No images found. (Might be a video or text-only)")
                    continue

                for i, url in enumerate(found_urls):
                    ext = ".png" if ".png" in url.lower() else ".jpg"
                    file_name = f"post_{idx}_img_{i}{ext}"
                    
                    # Download using requests
                    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                    if res.status_code == 200:
                        with open(os.path.join(DOWNLOAD_PATH, file_name), 'wb') as f:
                            f.write(res.content)
                        print(f"      ✅ Saved: {file_name}")

            except Exception as e:
                print(f"      ⚠️ Skip: Page load error.")

        browser.close()
        print(f"✨ Mission Accomplished, Nihal! Check the '{DOWNLOAD_PATH}' folder. 😎")

if __name__ == "__main__":
    scrape_reddit_correctly()
