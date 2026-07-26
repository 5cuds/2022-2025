from customtkinter import *

class App(CTk):
      def __init__(self) -> None:
            choices = ["Have Fun", "Die Trying", "Live Happy"]
            widget = CTkOptionMenu(self, values=choices)
            widget.pack()


if __name__ == "__main__":
      App().mainloop()