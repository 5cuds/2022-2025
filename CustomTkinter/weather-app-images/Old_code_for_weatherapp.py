from customtkinter import *
from PIL import Image
import requests

set_appearance_mode("dark")

def hide():
    title.pack_forget()
    credits_label.pack_forget()
    credits_label2.pack_forget()
    continue_button.pack_forget()
    seg_label.pack_forget()
    seg.pack_forget()

    entry_box.pack(pady = 15)

    big_title.pack(side=TOP)
    des_label.pack(side=TOP, pady=8)
    imager.pack(side=TOP)
    stat_label.pack(side=TOP, pady=8)
    temp_label.pack(side=TOP)
    text_label.pack(side=TOP)

    max_temp.place(x=20, y=360)
    min_temp.place(x=262, y=360)

    frame_display_1.place(x=20, y=415)
    frame_display_2.place(x=190, y=415)


    wind_label2.place(x=25,y=50)
    humity_label2.place(x=35, y=120)

    feel_label.place(x=8, y=20)
    feel_label2.place(x=25,y=50)

def main(event):

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    if entry_box.get() == "":
        text_label.configure(text="Enter Something dummy :)")
    else:
        params = { "q": entry_box.get(), "appid": "17d678349374714a0cb8702690a57526", "units": "metric"}

        response = requests.get(base_url, params=params)
        weather_data = response.json()

        if response.status_code == 200:

            text_label.configure(text="")
            big_title.configure(text=entry_box.get().capitalize())
            des_label.configure(text=f"City/State in {weather_data["sys"]["country"]}")
            stat_label.configure(text=weather_data["weather"][0]["description"].title())
            temp_label.configure(text=f"{weather_data["main"]["temp"]}°C")

            wind_label2.configure(text=f"{weather_data["wind"]["speed"]}km/h")
            humity_label2.configure(text=f"{weather_data["main"]["humidity"]}%")
            feel_label2.configure(text=f"{weather_data["main"]["feels_like"]}°C")

            max_temp.configure(text=f"Max Temp: \n{weather_data["main"]["temp_max"]}°C")
            min_temp.configure(text=f"Min Temp: \n{weather_data["main"]["temp_min"]}°C")

            image1 = None
            match weather_data["weather"][0]["main"]:
                case "Clear":
                    image1 = CTkImage(Image.open("weather-app-images/sun.png"), size=(150, 150))
                case "Clouds":
                    image1 = CTkImage(Image.open("weather-app-images/clouds.png"), size=(150, 150))
                case "Rain" | "Drizzle":
                    image1 = CTkImage(Image.open("weather-app-images/rain.png"), size=(150, 150))
                case "Thunderstorm":
                    image1 = CTkImage(Image.open("weather-app-images/lightning.png"), size=(150, 150))
                case "Snow":
                    image1 = CTkImage(Image.open("weather-app-images/snow.png"), size=(150, 150))
                case _:
                    image1 = CTkImage(Image.open("weather-app-images/mist.png"), size=(150, 150))
            imager.configure(image=image1)
            
        else:
            text_label.configure(text="Error: City Not Found 404")

def theme(value):
    if seg.get() == "Light":
        set_appearance_mode("light")
        frame_display_1.configure(fg_color="#9a9da1")
        frame_display_2.configure(fg_color="#9a9da1")
    else:
        set_appearance_mode("dark")
        frame_display_1.configure(fg_color="#363836")
        frame_display_2.configure(fg_color="#363836")
    

app = CTk()

app.geometry("400x660")
app.title("Nar's Weather App")
app.resizable(False, False)

frame1 = CTkFrame(app, corner_radius=20)
frame1.pack(pady=20, padx=20, fill="both", expand=True)

frame_display_1 = CTkFrame(frame1, height=190, width=150, corner_radius=20, fg_color="#363836")
frame_display_2 = CTkFrame(frame1, height=190, width=150, corner_radius=20, fg_color="#363836")


image1 = CTkImage(Image.open("weather-app-images/icon-cloud.png"), size=(160, 160))
title = CTkLabel(frame1, text="Nar's Weather App", font=("Cascadia Code", 25), image=image1, compound=TOP)

credits_label = CTkLabel(frame1, text="Made By", font=("Cascadia Code", 15))

# image2 = CTkImage(Image.open("youtube.png"), size=(20, 20))
credits_label2 = CTkLabel(frame1, text="JustNars", font=("Cascadia Code", 20), compound=RIGHT)

continue_button = CTkButton(frame1, text="Continue", font=("Cascadia Code", 20), fg_color="#a3aab5", corner_radius=10, hover_color="Gray", width=60, height=40, command=hide)

title.pack(side=TOP, pady=20)
credits_label.pack(side=TOP)
credits_label2.pack(side=TOP)
continue_button.pack(side=TOP, pady=60)

entry_box = CTkEntry(frame1, placeholder_text="Search a City", font=("Cascadia Code", 15), corner_radius=10, width=300, height=40)
entry_box.bind("<Return>", main)

ima = CTkImage(Image.open("weather-app-images/sun.png"), size=(150, 150))
imager = CTkLabel(frame1, text="", image=ima)

big_title = CTkLabel(frame1, text="", font=("Cascadia Code", 35))
des_label = CTkLabel(frame1, text="", font=("Cascadia Code", 15))
stat_label = CTkLabel(frame1, text="", font=("Cascadia Code", 20))
temp_label = CTkLabel(frame1, text="", font=("Arial", 35))
text_label = CTkLabel(frame1, text="", font=("Cascadia Code", 17))

wind_label2 = CTkLabel(frame_display_1, text="", font=("Cascadia Code", 20))
humity_label2 = CTkLabel(frame_display_1, text="", font=("Cascadia Code", 34))

feel_image = CTkImage(Image.open("weather-app-images/user.png"), size=(20, 20))
feel_label = CTkLabel(frame_display_2, text=" Feels:", font=("Cascadia Code", 20), image=feel_image, compound=LEFT)
feel_label2 = CTkLabel(frame_display_2, text="", font=("Cascadia Code", 20))

seg_label = CTkLabel(frame1, text="Choose A Theme", font=("Cascadia Code", 25))
seg_label.pack(side=BOTTOM)

max_temp = CTkLabel(frame1, text="", font=("Cascadia Code", 15))
min_temp = CTkLabel(frame1, text="", font=("Cascadia Code", 15))

# --------(Buttons)--------

modes = ["Dark", "Light"]
seg = CTkSegmentedButton(frame1, values=modes, font=("Cascadia Code", 20), fg_color="Gray", corner_radius=10, selected_color="#8b929e", selected_hover_color="#8b929e", command=theme)
seg.pack(side=BOTTOM, pady=20)
seg.set("Dark")

app.mainloop()