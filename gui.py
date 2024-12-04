#written on a separate file for now
import tkinter as tk

root = tk.Tk()

root.geometry("600x600") #window size
root.title("Word Hunt")

#Score text
score_dis = tk.Label(root, text = "Score: XXXX", font=('Arial',20))
score_dis.pack(padx=20, pady=20)

#create a custom-sized square grid and insert the generated seed into the grid

root.mainloop()