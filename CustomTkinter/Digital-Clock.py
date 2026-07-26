from customtkinter import *
import time
import datetime

def time():
    now = datetime.datetime.now().strftime(f"%H:%M:%S {'%p'}")
    text_label.configure(text=now)
    app.after(1000, time)

app = CTk()

app.title("Nar's Digital Clock")
app.resizable(False, False)

# Fonts
custom_font = CTkFont(family="digital-7", size=45)
date_font = CTkFont(family="digital-7", size=35)

#labels
text_label = CTkLabel(app, text=datetime.datetime.now().strftime("%H:%M:%S"), font=custom_font, bg_color="black", height=60, width=300,
                      text_color="#00ff11")
time()
date_label = CTkLabel(app, text=datetime.date.today(), font=date_font, bg_color="black", height=60, width=300,
                      text_color="#00ff11")

# pack
text_label.pack(side=TOP)
date_label.pack(side=BOTTOM)


app.mainloop()

