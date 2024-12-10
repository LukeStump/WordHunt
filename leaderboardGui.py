#gui popup for when a game ends

#have player enter name first, then display the leaderboard
#written on a separate file for now
import board 
import game
import leaderboard
import tkinter as tk
from tkinter import *

#class Window(Frame):
    #Opens the leaderboard on command
def openNewWindow(self):
    leaderboardgui = Toplevel() #main
    leaderboardgui.geometry = ("400x600")
    leaderboardgui.title("Leaderboard")

    "Get data from game"
    seed = "test_seed"
    dict = leaderboard.sorted_dict

    "GUI"
    #Title
    title = tk.Label(leaderboardgui, height = 1, width = 14,text="Leaderboard",font=('Arial',30))
    title.pack(side=tk.TOP, pady=10)
    seed = tk.Label(leaderboardgui, height = 1, width = 14,text=f"Seed: {seed}",font=('Arial',18))
    seed.pack(side=tk.TOP, pady=5)

    #List
    score_list = tk.Listbox(leaderboardgui, height = 20, width = 30,font=('Arial',15),justify="center")
    score_list.pack(side=tk.TOP, pady=10)

    #Add scores to list
    for i in dict:
        score_list.insert(END,i + " " + str(dict[i]))



