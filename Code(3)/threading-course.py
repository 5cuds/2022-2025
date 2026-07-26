import requests
from tkinter import *

win = Tk()

# win.config(background="Sky Blue")

def enter():
    global png, img_label

    key = "17d678349374714a0cb8702690a57526"
    city = entry.get()

    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

    r = requests.get(link)

    if r.status_code == 200:
        data = r.json()

        weather_main = data["weather"][0]["main"]
        
        match weather_main:
            case "Clouds":
                icon = "images/cloud.png"
            case "Rain":
                icon = "images/rain.png"
            case "Snow":
                icon = "images/snowflake.png"
            case "Thunderstorm":
                icon = "images/thunderstorm.png"
            case "Clear":
                icon = "images/clear.png"
            case "Drizzle":
                icon = "images/drizzle.png"

        png = PhotoImage(file=icon)
        img_label.config(image=png)
        img_label.image = png  # Keep a reference to avoid garbage collection

        text.config(text=f"Temp: {data['main']['temp']}°C\n"
                         f"Feels like: {data['main']['feels_like']}°C\n"
                         f"Pressure: {data['main']['pressure']} hPa\n"
                         f"Humidity: {data['main']['humidity']}%\n"
                         f"Temp (MIN): {data['main']['temp_min']}°C\n"
                         f"Temp (MAX): {data['main']['temp_max']}°C")
    else:
        text.config(text="404 Error Not Found!")

    entry.delete(0, END)

def delete():
    entry.delete(0, END)

def clear():
    text.config(text="Enter a City name.")
    img_label.config(image='')  # Clear the image

entry = Entry(win, font=("Comic Sans MS", 40))

enter_button = Button(
    win,
    text="Enter",
    command=enter,
    font=("Basic", 15),
    bg="#5ddf43"
)

delete_button = Button(
    win,
    text="Delete",
    command=delete,
    font=("Basic", 15),
    bg="#e74023"
)

exit_button = Button(
    win,
    text="Clear\nstatus",
    command=clear,
    font=("Basic", 10),
    bg="#e74023"
)

text = Label(
    win,
    text="Enter a City name.",
    font=("Basic", 15),
    fg="Black",
    bg="Sky blue"
)

img_label = Label(win, bg="Sky blue")  # Create a label for the image

entry.pack(anchor="nw", ipadx=30)
text.pack()
img_label.pack()

delete_button.place(x=160, y=615, width=100, height=50)
exit_button.place(x=30, y=615, width=100, height=50)
enter_button.place(x=30, y=550, width=230, height=50)

win.attributes('-fullscreen', False)
win.mainloop()
