from tkinter import *

win = Tk()

count = 0
def click():
    global count
    count += 1
    show_count.config(text=count)

photo = PhotoImage(file='C:\\Users\\Windows\\Documents\\cookie-png.png')

button = Button(win, command=click,
                bg="#df9143",
                activebackground='#825120',
                image=photo,
                compound=BOTTOM)

show_count = Label(win, font=("none", 50,'bold'))

win.title("Cookie clicker!")

icon = PhotoImage(file='C:\\Users\\Windows\\Documents\\cookie-png.png')
win.iconphoto(True, icon)


show_count.pack(side=TOP)
button.pack()


win.mainloop()