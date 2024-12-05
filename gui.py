#written on a separate file for now
import tkinter as tk
from tkinter import *
root = tk.Tk() #main

root.geometry("900x600") #window size
root.title("Word Hunt")

frame = tk.Frame(root, bg="lightblue")
frame.place(relwidth=1, relheight=1)

#Score text
score_dis = tk.Label(root, 
text = "Score: XXXX", 
font=('Arial',20),
anchor=tk.NW)
score_dis.place(x=100,y=500)

#Scrollbar for found words
# scrollbar1 = tk.Scrollbar(root)
# scrollbar1.place(x=700,y=300)

# mylist = Listbox(root,  
#                  yscrollcommand = scrollbar1.set ) 
   
# for line in range(1, 26): 
#     mylist.insert(END, "Geeks " + str(line)) 

# scrollbar1.config( command=mylist.yview)

#Textbox for user input
input = Text(root, height = 1, width = 16,font=('Arial',30))
input.insert(tk.END, "WORRRDDDDD")
input.place(x=480,y=385)

#Button to submit word
submit = Button(root, height=2,width=21,text="Submit", font=('Arial',20))
submit.place(x=486,y=450)
""" create a custom-sized square grid 
and insert the generated seed into the grid """
grid_size = 4 #this can be changed
root.columnconfigure(0, weight=0)
for i in range(grid_size):
    for j in range(grid_size):
        frame = tk.Frame(root, bg='black', width=100, height=100)
        frame.grid(row=i, column=j+1,padx=5,pady=5)
root.columnconfigure(grid_size+1, weight=1)

root.mainloop()