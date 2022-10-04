from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("600x300")

mixer.init()
mixer.music.load("1.mp3")


def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()

def volume():
    mixer.music.set_volume(30)


Label(root, text="Welcome to music player", font="lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=260, y=100)
Button(text="Resume", command=resume).place(x=200, y=150)
Button(text="Quit", command=quit).place(x=260, y=150)
Button(text="vol-", command=volume()).place(x=320, y=150)
Button(text="vol+", command=volume()).place(x=320, y=100)

root.mainloop()
