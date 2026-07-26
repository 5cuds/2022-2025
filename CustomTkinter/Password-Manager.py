from customtkinter import *
from PIL import Image
import pandas as pd
import json

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        self.appearance = "light"
        set_appearance_mode(self.appearance)

        # set the appearance of the app
        self.resizable(False, False)
        self.title("Nar's Password Manager")
        self.geometry("425x625")

        # this frame is the container for key things settings or password generator 
        a_frame = CTkFrame(self, corner_radius=20, height=100, width=485)
        a_frame.pack(side="botton")


    def get_master_password(self):
        pass
        

        

if __name__ == "__main__":
    MainApp().mainloop()