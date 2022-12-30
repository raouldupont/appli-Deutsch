from tkinter import *
import tkinter as tk

def newWindow():
    window = tk.Toplevel(app)
    label= tk.Label(window, text="new window")
    button = tk.Button(window, text = "new window button")

    label.pack()
    button.pack()

    app = tk.Tk()
    button = tk.Button(app, text="create new window", command=newWindow)
    
    button.pack()
    app.mainloop()
