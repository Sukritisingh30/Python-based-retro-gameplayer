
from tkinter import *
from tkinter import font

from pygame import MIDIIN
root = Tk()
text = Text(root)
root.geometry("1000x220")
text.insert(INSERT, "Retro Multigameplayer is a 2022 free-to-play computer strategy multi game player developed by the students of PIET college.\n" )
text.insert(END, "Game is developed for the people who can’t afford expensive gaming consoles to play games.\n")
text.insert(END, "Game comes with the feature of highest score through which one can compete with each other.\n")
text.insert(END, "Game is set in a retro-theme, You can play this with your friends and family to release stress and anxiety.\n")  
#text.insert(END, "This is a phrase.\n")
#text.insert(END, "Bye bye...")
text.pack(expand=1, fill=BOTH)
# adding a tag to a part of text specifying the indices
text.tag_add("start", "1.0", "5.0")
text.tag_config("start", background="grey21", foreground="gold1")
root.mainloop()