#from snake import highestscore
#from pacman import state
from tkinter import * 
from tkinter import font as tkFont

import os
import sys
root = Tk()
root.configure(bg='grey21')

with open("G55\score text\snake_score.txt","r") as f:
    snake_sc=f.read()
    print(snake_sc)

w = Label(root, text ='HIGHSCOREs', font = "250", fg='gold1', bg ='grey21')
Font_tuple = ("Algerian", 50, "bold")
w.configure(font = Font_tuple)
w.pack(side=TOP, padx=15, pady=20)
w.pack()

w1 = Label(root, text ='Snake Game Highest score-' + snake_sc, font = "100", fg='gold1',bg='grey21')
Font_tuple = ("Algerian", 20, "bold")
w1.configure(font = Font_tuple)
w1.pack(side=TOP, padx=0, pady=0)
w1.pack()

with open("G55\score text\carrace_score.txt","r") as f:
    carrace_sc=f.read()
    print(carrace_sc)
w2 = Label(root, text ='Car Race Highest score-' + carrace_sc, font = "100", fg='gold1',bg='grey21')
Font_tuple = ("Algerian", 20, "bold")
w2.configure(font = Font_tuple)
w2.pack(side=TOP, padx=0, pady=0)
w2.pack()

with open("G55\score text\pacman_score.txt","r") as f:
    pacman_sc=f.read()
    print(pacman_sc)
w2 = Label(root, text ='Pacman Highest score-' + pacman_sc, font = "100", fg='gold1',bg='grey21')
Font_tuple = ("Algerian", 20, "bold")
w2.configure(font = Font_tuple)
w2.pack(side=TOP, padx=0, pady=0)
w2.pack()


root.mainloop()