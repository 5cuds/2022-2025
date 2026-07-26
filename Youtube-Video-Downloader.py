from yt_dlp import YoutubeDL
import os


def download(link: str, res: str, name: str, type: str, playlist: bool) -> None:
      """Downloads Video From Youtube"""
      ydl_opts = {
            'format': f'{res}+bestaudio/best',  
            'merge_output_format': type,        
            'outtmpl': os.path.join(r"C:\Users\Windows\Videos\Downloaded Youtube Videos", f'{name}.{type}'),       
            'noplaylist': playlist,        
      }

      try:
            with YoutubeDL(ydl_opts) as ydl:
                  ydl.download([link])
            print(f"Download completed: {name}.{type}")

      except Exception as e:
            print(f"[Error]: {e}")


def main() -> None:
      print("(Python Youtube Video Downloader)\n")
      resolutions = ('144', '240', '360', '480', '720', '1080', '1440', '2160')
      while True:
            try:
                  link = input("Link: ")

                  print("\n(Resolutions)")
                  for num, i in enumerate(resolutions):
                        print(f"{num}){i}")

                  res = int(input("Enter Index: "))
                  title = input("Title (without extension): ").capitalize()
                  type_of_video = input("Type (ex: mp3, mp4): ")
                  play_list = input("Download Playlist? (Yes/No): ").capitalize().strip()

                  os.makedirs(r"C:\Users\Windows\Videos\Downloaded Youtube Videos", exist_ok=True)
                  download(link=link, res=resolutions[res], name=title, type=type_of_video,
                           playlist= True if play_list == "Yes" else False)
                  
                  break

            except Exception as e:
                  print(f"[Error]: {e}")
                  continue

if __name__ == "__main__":
      main()