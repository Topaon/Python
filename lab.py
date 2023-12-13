from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

app = Tk()
app.title("Pieds en mètres")

#on crée la fenêtre principale pour le logiciel
mainframe = ttk.Frame(app, padding="3 3 12 12")
mainframe.grid(column = 0 , row = 0, sticky = (N, W, E, S))
app.columnconfigure(0, weight = 1)
app.rowconfigure(0, weight = 1)

#on crée le champs à compléter, qu'on associe à => feet
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet)
feet_entry.grid(column = 2, row = 1, sticky=(W, E))

#on crée un label pour la réponse, qu'on associe à => meters
meters = StringVar()
ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Calculer", command = calculate).grid(column = 3, row = 3, sticky = W)

ttk.Label(mainframe, text = "pieds").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "équivaut à").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "mètres").grid(column = 7, row = 2, sticky = W)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

feet_entry.focus()
app.bind("<Return>", calculate)

app.mainloop()
