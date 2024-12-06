#written on a separate file for now
import board 
import game
import tkinter as tk
from tkinter import *
root = tk.Tk() #main

w = 900
h = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y)) #window size
root.title("Word Hunt")

left_frame = tk.Frame(master=root, bg="#9fbded")
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
right_frame = tk.Frame(master=root, bg="#9fbded")
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

#init
gameBoard = board.makeRandomBoard(4,4, board.generateSeed())
g = game.Game(gameBoard)

#Timer label
time_dis = tk.Label(right_frame, 
text = "Time: 0:00", 
font=('Arial',20),bg='#9fbded',
anchor=tk.NW)
time_dis.pack(side=tk.TOP, pady=10, padx=10, anchor=tk.E)
#time_dis.place(x=750,y=30)

#Scrollbar for found words
word_list = Listbox(right_frame, width=10,font=("Arial",16), justify="center")
word_list.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=10, pady=5)
# word_list.place(x=600,y=80)

scrollbar1 = tk.Scrollbar(right_frame,orient=VERTICAL)

my_list = []
mylist = Listbox(right_frame, yscrollcommand = scrollbar1.set ) 
scrollbar1.config( command=mylist.yview)   
for i in (my_list):
    word_list.insert(END, i)

#Validation message
submit = Label(right_frame, height=1,text="", font=('Arial',14),fg="#4f0b12",bg="#9fbded")
submit.pack(side=tk.TOP, pady=10)

#Textbox for user input
input = Text(right_frame, height = 1, width = 16,font=('Arial',30))
input.insert(tk.END, "")
input.pack(side=tk.TOP)

#Button to submit word
submit = Button(right_frame, height=2,width=21,text="Submit", font=('Arial',20))
submit.pack(side=tk.TOP, pady=10)
#submit.place(x=486,y=450)



""" create a custom-sized square grid 
and insert the generated seed into the grid """
grid_size = 4 #this can be changed but additional code needs to be done to
#compensate the window
left_size = grid_size+2
for i in range(left_size):
    left_frame.columnconfigure(i, weight=1)
    left_frame.rowconfigure(i, weight=1)
frame_size = 420//grid_size
pad_size = 20//grid_size
letter_size = 200//grid_size
for i in range(grid_size):
    for j in range(grid_size):
        frame = tk.Frame(left_frame, bg='#d6e6ff', width=frame_size, height=frame_size)
        frame.grid(row=i, column=j+1,padx=pad_size,pady=pad_size)
        letter = gameBoard.getLetter((i,j))
        label = tk.Label(frame, text=letter, font=('Arial',letter_size))
        label.place(relwidth=1, relheight=1)

#Score text
score_dis = tk.Label(left_frame, text = "Score: 0", font=('Arial',30),bg='#9fbded',anchor=tk.NW)
score_dis.grid(row=left_size-1, columnspan=left_size, pady=10)
#score_dis.place(x=100,y=470)
root.mainloop()
