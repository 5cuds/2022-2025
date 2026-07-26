import tkinter as tk
from tkinter import messagebox
import json
import webbrowser
import google_auth_oauthlib.flow
import googleapiclient.discovery

class NihalYoutubeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nihal's Systems-Level Liked Crawler")
        self.root.geometry("500x450")
        
        # --- UI ELEMENTS ---
        tk.Label(root, text="Spider-Man Video ID:", font=('Arial', 10, 'bold')).pack(pady=5)
        self.id_entry = tk.Entry(root, width=30); self.id_entry.pack()
        self.id_entry.insert(0, "Pn0zg4sDm9I") # Default Spider-Man ID

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)
        
        tk.Button(self.btn_frame, text="1. Authenticate & Fetch", command=self.start_crawl).grid(row=0, column=0, padx=5)
        self.watch_btn = tk.Button(self.btn_frame, text="2. Watch Current 📺", state="disabled", command=self.open_link)
        self.watch_btn.grid(row=0, column=1, padx=5)

        # Video Data Display
        self.info_text = tk.Text(root, height=10, width=55, font=('Consolas', 9))
        self.info_text.pack(pady=10)

        # Filter Buttons
        self.filter_frame = tk.Frame(root)
        self.filter_frame.pack(pady=10)
        tk.Button(self.filter_frame, text="Move to JSON A", bg="green", fg="white", command=lambda: self.save_to_json("filter_A.json")).grid(row=0, column=0, padx=10)
        tk.Button(self.filter_frame, text="Move to JSON B", bg="blue", fg="white", command=lambda: self.save_to_json("filter_B.json")).grid(row=0, column=1, padx=10)

        self.current_video_data = None

    def get_service(self):
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", ["https://www.googleapis.com/auth/youtube.readonly"])
        return googleapiclient.discovery.build("youtube", "v3", credentials=flow.run_local_server(port=0))

    def start_crawl(self):
        try:
            self.youtube = self.get_service()
            # Fetch most recent liked video as a demo (you can loop this to go "up")
            request = self.youtube.playlistItems().list(part="snippet,contentDetails", playlistId="LL", maxResults=1)
            response = request.execute()
            item = response['items'][0]
            vid_id = item['contentDetails']['videoId']
            
            # Get specific stats (Views)
            v_req = self.youtube.videos().list(part="snippet,statistics", id=vid_id).execute()
            v_data = v_req['items'][0]

            self.current_video_data = {
                "title": v_data['snippet']['title'],
                "id": vid_id,
                "uploaded_at": v_data['snippet']['publishedAt'],
                "views": v_data['statistics'].get('viewCount', '0'),
                "thumb": v_data['snippet']['thumbnails']['high']['url'],
                "link": f"https://www.youtube.com/watch?v={vid_id}"
            }
            
            self.update_ui()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_ui(self):
        self.info_text.delete('1.0', tk.END)
        data = self.current_video_data
        display_str = (f"TITLE: {data['title']}\n"
                       f"DATE:  {data['uploaded_at']}\n"
                       f"VIEWS: {data['views']}\n"
                       f"THUMB: {data['thumb']}\n"
                       f"LINK:  {data['link']}")
        self.info_text.insert(tk.END, display_str)
        self.watch_btn.config(state="normal")

    def open_link(self):
        if self.current_video_data:
            webbrowser.open(self.current_video_data['link'])

    def save_to_json(self, filename):
        if not self.current_video_data: return
        # STREAMING WRITE: We append as a new line. No list needed!
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(self.current_video_data) + "\n")
        messagebox.showinfo("Success", f"Video streamed to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    NihalYoutubeGUI(root)
    root.mainloop()
