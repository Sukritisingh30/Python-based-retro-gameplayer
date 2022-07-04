from tkinter import *
from PIL import ImageTk, Image  
import os
import sys

root = Tk()
root.title("Welcome GUI")
root.configure(bg='grey15')

root.geometry("1400x800")
w = Label(root, text ='  ❃ BONJOUR ❃  ', font = "250", fg='grey21',bg='gold2')

Font_tuple = ("Algerian", 50, "bold")
 
w.configure(font = Font_tuple)

w.pack(side=TOP, padx=15, pady=20)
w.pack()
# Add text
frame = Frame(root)
frame.pack()
topframe = Frame(root)
topframe.pack( side = TOP)

button=Button(root)
root.geometry("1300x800")
def run_bg():
    os.system('python G55//code//bg.py')
# Add Image
start_button = PhotoImage(file =r"G55\image\Play-button-icon-in-yellow-color-on-transparent-background-PNG.png")
#start_button.pack(side=RIGHT, padx=15, pady=20)

# Create button and image
img = Button(root, image = start_button,
             borderwidth = 200,command=run_bg)

             

  
img.pack()

# Execute tkinter
root.mainloop()