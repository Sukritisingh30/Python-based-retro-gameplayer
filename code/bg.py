from lib2to3.pgen2.token import LEFTSHIFT
from operator import length_hint
from tkinter import * 
from tkinter import font as tkFont

import os
import sys
############################################## photo addition



snake_path = 'G55\code\snake.py'    
#append the paths
sys.path.append(snake_path)
root = Tk()
root.geometry("1400x800")
root.configure(bg='grey15')


w = Label(root, text ='PYTHON BASED RETRO GAMEPLAYER', font = "250", fg='gold1',bg='grey21')
Font_tuple = ("Algerian", 50, "bold")

label2=Label(root, text="GAME WILL OCCLUDE AFTER 1 HR ...", font=("Times",15,"bold"), bg='grey21', fg='gold1')
label2.pack(side=TOP, pady=0 ,padx=10)
 
w.configure(font = Font_tuple)

w.pack(side=TOP, padx=15, pady=20)
w.pack()


frame = Frame(root)
frame.pack()


topframe = Frame(root)
topframe.pack( side = TOP)
font = tkFont.Font(family='Algerian', size=20, weight=tkFont.BOLD)

def run_realtime():
    os.system('python G55//code//realtime.py')
b5_button = Button(topframe, text ="REAL TIME", bg='grey21', fg ="gold1",command=run_realtime)
b5_button.config( height = 2, width = 50)
b5_button.pack( side = TOP)
b5_button.pack(side=TOP, padx=15, pady =0)
b5_button['font'] = font

def run_about():
    os.system('python G55//code//text.py')
b6_button = Button(topframe, text ="ABOUT GAME", bg='grey21', fg ="gold1",command=run_about)
b6_button.config( height = 2, width = 50)
b6_button.pack( side = TOP)
b6_button.pack(side=TOP, padx=15, pady=0)
b6_button['font'] = font
def run_highscore():
    os.system('python G55//code//highscr.py')
b7_button = Button(topframe, text ="HIGH SCORE",bg='grey21', fg ="gold1",command=run_highscore)
b7_button.config( height = 2, width = 50 )
b7_button.pack( side = TOP)
b7_button.pack(side=TOP, padx=15, pady=0)
b7_button['font'] = font


def run_snake():
    os.system('python G55//code//snake.py')

b1_button = Button(frame, text ="SNAKE GAME", bg='grey21', fg ="gold1",command=run_snake)
b1_button.pack( side = LEFT)
b1_button.config( height = 2, width = 50 )
b1_button.pack(side=TOP, padx=15, pady=0)
b1_button['font'] = font


def run_pac():
    os.system('python G55//code//pacman.py')

b2_button = Button(frame, text ="PACMAN", fg ="gold1",bg='grey21',command=run_pac)
b2_button.pack( side = LEFT)
b2_button.config( height = 2, width = 50 )
b2_button.pack(side=TOP, padx=15, pady=0)
b2_button['font'] = font

def run_hangman():
    os.system('python G55//code//hangman.py')

b4_button = Button(frame, text ="HANGMAN", fg ="gold1",bg='grey21',command=run_hangman)
b4_button.pack( side = LEFT )
b4_button.config( height = 2, width = 50 )
b4_button.pack(side=TOP, padx=15, pady=0)
b4_button['font'] = font

def run_carrace():
    os.system('python G55//code//carrace.py')
b3_button = Button(frame, text ="CAR RACE", fg ="gold1",bg='grey21',command=run_carrace)
b3_button.pack( side = LEFT )
b3_button.config( height = 2, width = 50 )
b3_button.pack(side=TOP, padx=15, pady=0)
b3_button['font'] = font
## autoclose after 1 hr.
root.after(3600000,lambda:root.destroy())
root.mainloop()