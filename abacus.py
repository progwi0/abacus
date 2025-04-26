import os
import tk as tk
from tkinter import messagebox as dialogus
from ttkbootstrap import *
from ttkbootstrap.constants import *

app = Window(themename="litera")
app.title("Abacus")

homus = os.path.expanduser("~")
patus = os.path.join(homus, ".progwi0")
themepath = os.path.join(patus, "theme.txt")

simplus = "~/.progwi0/theme.txt"

def result():
    resulti = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, str(resulti))

def info():
    dialogus.showinfo("🧮", "Abacus 1.0\nCreated in 2025 by progwi0.")

def light():
    app.style.theme_use("litera")
    with open(themepath, "w") as file:
        file.write("litera")

def dark():
    app.style.theme_use("darkly")
    with open(themepath, "w") as file:
        file.write("darkly")

top = Frame(app)
top.pack(fill="x", pady="2", padx="2")

a = Frame(app)
a.pack(fill="both", pady="2", padx="2", expand=True)

b = Frame(app)
b.pack(fill="both", pady="2", padx="2", expand=True)

c = Frame(app)
c.pack(fill="both", pady="2", padx="2", expand=True)

d = Frame(app)
d.pack(fill="both", pady="2", padx="2", expand=True)

abacus = Button(top, text = "🧮", command = lambda:menu.post(app.winfo_pointerx(), app.winfo_pointery()), bootstyle = SECONDARY)
abacus.pack(side="left", padx="2", fill="x", expand=True)

entry = Entry(top)
entry.pack(side="left", padx="2", fill="x", expand=True)

one = Button(a, text = "1", command = lambda:entry.insert(END, "1"), bootstyle = SECONDARY)
one.pack(side="left", padx="2", fill="both", expand=True)

two = Button(a, text = "2", command = lambda:entry.insert(END, "2"), bootstyle = SECONDARY)
two.pack(side="left", padx="2", fill="both", expand=True)

three = Button(a, text = "3", command = lambda:entry.insert(END, "3"), bootstyle = SECONDARY)
three.pack(side="left", padx="2", fill="both", expand=True)

four = Button(b, text = "4", command = lambda:entry.insert(END, "4"), bootstyle = SECONDARY)
four.pack(side="left", padx="2", fill="both", expand=True)

five = Button(b, text = "5", command = lambda:entry.insert(END, "5"), bootstyle = SECONDARY)
five.pack(side="left", padx="2", fill="both", expand=True)

six = Button(b, text = "6", command = lambda:entry.insert(END, "6"), bootstyle = SECONDARY)
six.pack(side="left", padx="2", fill="both", expand=True)

seven = Button(c, text = "7", command = lambda:entry.insert(END, "7"), bootstyle = SECONDARY)
seven.pack(side="left", padx="2", fill="both", expand=True)

eight = Button(c, text = "8", command = lambda:entry.insert(END, "8"), bootstyle = SECONDARY)
eight.pack(side="left", padx="2", fill="both", expand=True)

nine = Button(c, text = "9", command = lambda:entry.insert(END, "9"), bootstyle = SECONDARY)
nine.pack(side="left", padx="2", fill="both", expand=True)

zero = Button(d, text = "0", command = lambda:entry.insert(END, "0"), bootstyle = SECONDARY)
zero.pack(side="left", padx="2", fill="both", expand=True)

plus = Button(a, text = "+", command = lambda:entry.insert(END, "+"), bootstyle = SECONDARY)
plus.pack(side="left", padx="2", fill="both", expand=True)

minus = Button(b, text = "-", command = lambda:entry.insert(END, "-"), bootstyle = SECONDARY)
minus.pack(side="left", padx="2", fill="both", expand=True)

division = Button(c, text = "/", command = lambda:entry.insert(END, "/"), bootstyle = SECONDARY)
division.pack(side="left", padx="2", fill="both", expand=True)

resultus = Button(d, text = "=", command = result,bootstyle = SECONDARY)
resultus.pack(side="left", padx="2", fill="both", expand=True)

multiplier = Button(d, text = "*", command = lambda:entry.insert(END, "*"), bootstyle = SECONDARY)
multiplier.pack(side="left", padx="2", fill="both", expand=True)

c = Button(a, text = "C", command = lambda:entry.delete(0, END), bootstyle = SECONDARY)
c.pack(side="left", padx="2", fill="both", expand=True)

menu = Menu(app, tearoff = 0)
menu.add_separator()
menu.add_command(label="Light theme", command = light)
menu.add_command(label="Dark theme", command = dark)
menu.add_separator()
menu.add_command(label="Update (Only for pix version)", command = lambda:os.system("pix reinstall abacus"))
menu.add_separator()
menu.add_command(label="My site", command = lambda:webbrowser.open("https://progwi0.github.io/"))
menu.add_command(label="About", command = info)
menu.add_separator()

with open(themepath, "r") as file:
        themus = file.read().strip()
        app.style.theme_use(themus)

app.mainloop()
