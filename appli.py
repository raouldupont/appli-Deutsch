
from _tkinter import *
from cgitb import text
from email import message
from email.message import Message
from re import X
from textwrap import fill
from tkinter import GROOVE, LEFT, RAISED, RIGHT, SUNKEN, TOP, Button, Canvas, Checkbutton, DoubleVar, Frame, Label, PhotoImage, Scale, Tk
from tkinter.messagebox import NO, YES
from turtle import bgcolor, right, up
from typing import Literal
import urllib.request
import tkinter as tk


window = Tk()
window.title("RD ANWENDUNG !YES!")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("allemand.ico")
window.config(background="black", cursor="circle")

frame = Frame(window, bg ="#41B77F", bd=0, relief= SUNKEN, pady=10)
frame2 = Frame(window, bg ="blue", bd=0, relief= SUNKEN)
frame3 = Frame(window,bg="black", bd=0, relief= SUNKEN, pady=15,)

framea = Frame(frame2, bg = "yellow", borderwidth=10, relief=GROOVE)
framea.pack(padx=5, pady=5)

frameb = Frame(frame2, bg = "yellow", borderwidth=10, relief=GROOVE)
frameb.pack(padx=5, pady=5)

framec = Frame(frame2, bg = "yellow", borderwidth=10, relief=GROOVE)
framec.pack(padx=5, pady=5)

framed = Frame(frame2, bg = "yellow", borderwidth=10, relief=GROOVE)
framed.pack(padx=5, pady=5)

framee = Frame(frame2, bg = "yellow", borderwidth=10, relief=GROOVE)
framee.pack(padx=5, pady=5)

framef = Frame(frame2, bg = "yellow", borderwidth=10, relief=GROOVE)
framef.pack(padx=5, pady=5)

frames = Frame(frame3, bg = "red", borderwidth=15, relief=GROOVE)
frames.pack()

title = Label(frame, text = "Redemittel für jede Situation", font=("Courrier", 35), bg = "#41B77F", fg = "black")
title.pack()

def firstWindow2():
    window2 = tk.Toplevel(window)
    window2.geometry("720x480")
    window2.minsize(480, 360)
    window2.iconbitmap("allemand.ico")
    window2.config(background="blue", cursor="circle")
#creation d'une nouvelle fenetre a partir d'un boutton 

title2 = Button(framea, text = "Redemittel für das Schreiben eines Kommentars", font=("Courrier", 20), bg = "blue", fg = "red",command=firstWindow2)
title2.pack()

def firstWindow():
    window1 = tk.Toplevel(window)
    window1.geometry("720x480")
    window1.minsize(480, 360)
    window1.iconbitmap("allemand.ico")
    window1.config(background="blue", cursor="circle")
    
    def firstWindowx():
        windowx = tk.Toplevel(window)
        windowx.geometry("720x480")
        windowx.minsize(480, 360)
        windowx.iconbitmap("allemand.ico")
        windowx.config(background="green", cursor="circle")

    def firstWindowy():
        windowy = tk.Toplevel(window)
        windowy.geometry("720x480")
        windowy.minsize(480, 360)
        windowy.iconbitmap("allemand.ico")
        windowy.config(background="red", cursor="circle")

    def firstWindowz():
        windowz = tk.Toplevel(window)
        windowz.geometry("720x480")
        windowz.minsize(480, 360)
        windowz.iconbitmap("allemand.ico")
        windowz.config(background="blue", cursor="circle")

    def firstWindowq():
        windowq = tk.Toplevel(window)
        windowq.geometry("720x480")
        windowq.minsize(480, 360)
        windowq.iconbitmap("allemand.ico")
        windowq.config(background="yellow", cursor="circle")
    
    framecontenu =Frame(window1, bd=0, bg="green")
    frameh = Frame(window1, bd=1, relief=GROOVE, borderwidth=5, bg="green")
    contenu = Label(frameh, text ="Hier finden Sie, was Sie nutzen können, um eine Grafik zu beschreiben.\n Beziehungsweise die Einleitung, die zu verwendenden Konnektoren, \n die Beschreibung \n der wichtigsten Punkte und Schluss", font=("Hack", 28), bg = "yellow")
    variable = Checkbutton(framecontenu, text="Einleitung", width= 20, bg="green", font=("courrier", 20), command= firstWindowx)
    variable1 = Checkbutton(framecontenu, text="Konektoren", width= 15, bg="red", font=("courrier", 20), command= firstWindowy)
    variable2 = Checkbutton(framecontenu, text="wichtige Punkte", width= 15, bg="blue", font=("courrier", 20), command= firstWindowz)
    variable3 = Checkbutton(framecontenu, text="Schluss", width= 15, bg="yellow", font=("courrier", 20), command= firstWindowq)
    frameh.pack()
    contenu.pack(side=TOP, expand= YES)
    variable.pack(side=LEFT, expand= YES)
    framecontenu.pack(side=LEFT, expand=YES)
    variable1.pack( expand=NO)
    variable2.pack( expand=NO)
    variable3.pack( expand=NO)


#creation d'une nouvelle fenetre a partir d'un boutton   

title3 = tk.Button(frameb, text="Redemittel für die Beschreibung einer Grafik", font=("Courrier", 20),bg  = "blue", fg = "red", command=firstWindow)
title3.pack(expand=YES)


def firstWindow3():
    window3 = tk.Toplevel(window)
    window3.geometry("720x480")
    window3.minsize(480, 360)
    window3.iconbitmap("allemand.ico")
    window3.config(background="blue", cursor="circle")
#creation d'une nouvelle fenetre a partir d'un boutton   
title4 = Button(framec, text="Redemittel zum Shreiben eines formellen Briefes", font=("Courrier", 20),bg  = "blue", fg = "red", command=firstWindow3)
title4.pack()

def firstWindow4():
    window4 = tk.Toplevel(window)
    window4.geometry("720x480")
    window4.minsize(480, 360)
    window4.iconbitmap("allemand.ico")
    window4.config(background="blue", cursor="circle")
#creation d'une nouvelle fenetre a partir d'un boutton   
title5 = Button(framed, text="Redemittel zum Schreiben eines informellen Briefes", font=("Courrier", 20),bg  = "blue", fg = "red", command=firstWindow4)
title5.pack()

def firstWindow5():
    window5 = tk.Toplevel(window)
    window5.geometry("720x480")
    window5.minsize(480, 360)
    window5.iconbitmap("allemand.ico")
    window5.config(background="blue", cursor="circle")
#creation d'une nouvelle fenetre a partir d'un boutton   

title6 = Button(framee, text="Redemittel zur Haltung eines Vortrags", font=("Courrier", 20),bg  = "blue", fg = "red", command= firstWindow5)
title6.pack()

def firstWindow6():
    window6 = tk.Toplevel(window)
    window6.geometry("720x480")
    window6.minsize(480, 360)
    window6.iconbitmap("allemand.ico")
    window6.config(background="blue", cursor="circle")
#creation d'une nouvelle fenetre a partir d'un boutton   
title7 = Button(framef, text="Redemittel für Diskussionen", font=("Courrier", 20),bg  = "blue", fg = "red", command= firstWindow6)
title7.pack()
def firstWindow7():
    window7 = tk.Toplevel(window)
    window7.geometry("720x480")
    window7.minsize(480, 360)
    window7.iconbitmap("allemand.ico")
    window7.config(background="black", cursor="plus")
    
    value = DoubleVar
    scale =Scale(window7, variable=value, bg="green")
    scale.pack(side=RIGHT)
#creation d'une nouvelle fenetre a partir d'un boutton   

title8 = Button(frames, text="Außergöhnliche Ausdrücke und ihre Bedeutungen", font=("Courrier", 25),bg  = "black", fg = "yellow", command=firstWindow7)
title8.pack()

wid = 500
hei = 500
image = PhotoImage(file= "allemandico.png").zoom(35).subsample(32)
canvas = Canvas(window, width=wid, height= hei, bg="green",  )
canvas.create_image(wid/2, hei/2, image= image,)
canvas.pack(side = LEFT,  padx=5, pady=0, expand=NO,)



frame.pack(expand=YES)
frame2.pack(expand=YES)
frame3.pack(expand=YES)




window.mainloop()


