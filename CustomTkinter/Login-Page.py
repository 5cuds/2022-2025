from customtkinter import *

def login():
    user = enter_username.get()
    passw = enter_password.get()

    if user.lower() == "justnars" and passw.lower() == "password123":

        fined.configure(text="● Login Successful", font=("Arial", 20), text_color="#42f545")

        fined.pack()

        app.after(2000, app.destroy)
    elif user.lower() == "justnars":

        fined.configure(text="● Incorrect Password.", font=("Arial", 20), text_color="#f54242")

    elif passw.lower() == "password123":

        fined.configure(text="● Incorrect Username.", font=("Arial", 20), text_color="#f54242")
    else:

        fined.configure(text="● Incorrect Username\nAnd\nPassword!", font=("Arial", 20), text_color="#f54242")
    fined.pack()

app = CTk()

app.title("Login")
app.geometry("500x560")

label_text = CTkLabel(app, text="Good Do See You Again,\nReady To Get Started?", font=("Arial", 30),
                            text_color="white")
horizontal_line = CTkFrame(app, height=2, fg_color="gray70", corner_radius=0)

label_text.pack(side="top",padx=15, pady=10)
horizontal_line.pack(pady=20, padx=20, fill="y", side="top")

password_label = CTkLabel(app, text="Password", font=("Helvetica", 25))
username_label = CTkLabel(app, text="\nUsername", font=("Helvetica", 25))

enter_username = CTkEntry(app, placeholder_text="Enter Username..", width=260, height=40, font=("Helvetica", 20), corner_radius=20)
enter_password = CTkEntry(app, placeholder_text="Enter Password..", show="●", width=260, height=40, font=("Helvetica", 20), corner_radius=20)

login_button = CTkButton(app, text="Login!", command=login, width=333, font=("Arial", 30))

fined = CTkLabel(app)

username_label.pack(pady=7)
enter_username.pack()

password_label.pack(pady=7)
enter_password.pack()

login_button.pack(pady=35)

app.mainloop()
