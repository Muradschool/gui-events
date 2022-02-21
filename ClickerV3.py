from distutils import command
from distutils.command.config import config
from tabnanny import check
import tkinter
import tkinter as tk
from tkinter import font

global up
clicks = 0
checks = " "
# alle tkinter code komt hier tussen
gui = tk.Tk()

gui.title("Clicker V3")
gui.geometry("500x500")
gui.config(bg= "gray")
clicks = 0 

def Colors(aantal)->str:
    kleur = "gray"
    if aantal < 0:
        kleur = "red"
    elif aantal > 0:
        kleur = "green" 
    return kleur

def up():
    global clicks, checks
    clicks += 1
    Button.config(text=clicks)
    checks ="up"
    gui.configure(bg=Colors(clicks))
    print(clicks)

def down():
    global clicks, checks
    clicks -= 1
    Button.config(text=clicks)
    checks ="down"
    gui.configure(bg=Colors(clicks))
    print(clicks)

def Enter(event):
    gui.configure(bg="yellow")

def Leave(event):
    global clicks
    gui.configure(bg=Colors(clicks))

def doubleclicks(event):
    global checks, clicks
    if checks == "up":
        clicks *= 3
    elif checks == "down":
        clicks /= 3 
    Button.config(text= clicks)

#box 1
ButtonUp = tk.Button(
text="Up",
font=("arial",25,"bold"),
bg="white",
fg="black",
command=up
)
ButtonUp.pack()

def UpButton():
    print(clicks)
ButtonUp.bind("<Button-1>")


#box 2
ButtonDown = tk.Button(
text="Down",
font=("arial",25,"bold"),
bg="white",
fg="black",
command=down
)
ButtonDown.place(relx=.5, rely=.5, anchor="s")


#box 3
Button = tk.Label(
text=clicks,
font=("arial",25,"bold"),
bg="white",
fg="black",
)
Button.place(relx=.5, rely=.3, anchor="center")

ButtonUp.bind("<Enter>", Enter)
ButtonUp.bind("<Leave>", Leave)
ButtonDown.bind("<Enter>", Enter)
ButtonDown.bind("<Leave>", Leave)
Button.bind("<Double-Button>", doubleclicks)
# alle tkinter code komt hier tussen
gui.mainloop()