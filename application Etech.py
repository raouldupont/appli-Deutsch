from tkinter import*
import webbrowser
def open_youtube_channel():
    webbrowser.open_new("https://www.youtube.com/watch?v=bLZOZCxDSNw")

window = Tk()
window.title("ETECH Application")
window.geometry("1080x720")
window.minsize(480,360)
window.iconbitmap("ETECH.ico")
window.config(background = "#41B77F")
frame = Frame(window,bg ="#41B77F", bd=1, relief = SUNKEN)


title = Label(frame, text = "Willkommen zur ETECHs Anwendung", font=("Courrier", 45), bg = "#41B77F", fg = "white")
title.pack()

title2 = Label(frame, text = "Hier anklicken, wenn Sie zum ETECHs youtube kanal gehen möchten", font=("Courrier", 25), bg = "#41B77F", fg = "white")
title2.pack()
frame.pack(expand=YES)

yt_button = Button(frame, text = " Youtube",font=("Courrier", 25), bg = "white", fg = "#41B77F", command =open_youtube_channel)
yt_button.pack(pady = 30, fill = X)



window.mainloop()


