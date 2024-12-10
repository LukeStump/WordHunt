#written on a separate file for now
import board 
import game
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from threading import *
root = tk.Tk() #main

w = 1300
h = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y)) #window size
root.title("Word Hunt")
root.resizable(False, False)

settings_frame = tk.Frame(master=root, bg="#9fbded")
settings_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

board_frame = tk.Frame(master=root, bg="#9fbded")
board_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

word_frame = tk.Frame(master=root, bg="#9fbded")
word_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

#init
gameBoard = None
g = None
timerActive = False

def enterWord(word):
    """ called when the player enters a word
    """
    if checkEndGame(): # ends the game if the requirements are fulfilled
        return
    result = g.enterWord(word)
    pts = result[0]
    display = result[1]

    if pts > 0:
        display += f"+{pts}"
    elif pts < 0:
        display += f"\t{pts}"
    
    vali.config(text=display)
    # TODO put display in gui (vali)
    input.delete("1.0","end")
    update()

    pass

def update():
    """ called to update timer and word lists
    """
    if g != None:
        # update score
        score = g.score
        score_dis.config(text=f"Score: {score}")

        # update timer
        time = g.timer.get_time()
        time_dis.config(text=time)

        # update word_list
        word_list.delete(0,END)
        word_list.insert(END,*g.correctWords)
    checkEndGame()
    pass

def generateSeed():
    """ called when player clicks "generate seed"
        generates a new seed and puts it in the seed box
        (creates new game with that seed?)
    """
    newSeed = board.generateSeed()
    # TODO put new seed in gui
    seedText.delete("1.0","end")
    seedText.insert(tk.END, newSeed)
    pass

def createGame():
    """ called when player clicks "create game"
        sets the board to a new board with the supplied proprties
    """
    global gameBoard, g
    seed = seedText.get("1.0", "end-1c")
    if seed == "":
        generateSeed()
        seed = seedText.get("1.0", "end-1c")
    seedText.delete("1.0","end")
    seedText.insert(tk.END, seed)
    size = int(gridSizeText.get("1.0", "end-1c"))
    minLength = int(minLengthText.get("1.0", "end-1c"))
    maxLength = maxLengthText.get("1.0", "end-1c")
    if maxLength == "":
        maxLength = None
    else:
        maxLength = int(maxLength)
    # TODO add more vars
    # TODO get vars from gui
    g = game.makeGame(size,size,minWordLength=minLength, maxWordLength=maxLength, seed = seed)
    gameBoard = g.board
    updateBoard()
    g.timer.start_time()
    input.config(state="normal")
    update()
    pass

def solveBoard():
    if g != None:
        g.solve()
        update()
    pass

def updateBoard():
    """ updates the display game board grid to be the current gameBoard
    """
    global score_dis
    # clear frame
    for widget in board_frame.winfo_children():
        widget.destroy()

    width = gameBoard.columns
    height = gameBoard.rows

    left_size = width+2
    for i in range(left_size):
        board_frame.columnconfigure(i, weight=1)
        board_frame.rowconfigure(i, weight=1)
    frame_size = 500//width
    pad_size = 15//width
    letter_size = 250//width

    for c in range(width):
        for r in range(height):
            frame = tk.Frame(board_frame, bg='#d6e6ff', width=frame_size, height=frame_size)
            frame.grid(row=r+1, column=c+1,padx=pad_size,pady=pad_size)
            letter = gameBoard.getLetter((r,c))
            label = tk.Label(frame, text=letter, font=('Arial',letter_size))
            label.place(relwidth=1, relheight=1)

    # TODO move into word_frame and out of this function
    #Score text
    score_dis.config(text = "Score: 0")
    pass

def setup_board():
    global gameBoard
    gameBoard = board.makeBoard("X"*16,4,4)
    updateBoard()

def resetSettings():
    seedText.delete("1.0","end")
    gridSizeText.delete("1.0","end")
    gridSizeText.insert(tk.END, "4")
    minLengthText.delete("1.0","end")
    minLengthText.insert(tk.END, "3")
    maxLengthText.delete("1.0","end")

def startButton(event=None):
    global timerActive
    createGame()
    timerActive = True
    t1=Thread(target=timeThread)
    t1.start()

def timeThread():
    while(timerActive):
        update()
        time.sleep(1)

def checkEndGame():
    """ checks if the game has ended, if it has, end the game and return True
        if it has not, return False
    """
    if not g.isGameOver():
        return False
    pass
    return True

#word header for score and time
word_header_frame = tk.Frame(master=word_frame, bg="#9fbded")
word_header_frame.pack(side=tk.TOP, fill=tk.BOTH)

word_header_frame.columnconfigure(0, weight=2)

#score label
score_dis = tk.Label(word_header_frame, text = "Score: 0", font=('Arial',28),bg='#9fbded', justify="left")
score_dis.grid(row=0,column=0, pady=10, padx=10, sticky=tk.W)

#Timer label
time_dis = tk.Label(word_header_frame, text = "0:00", font=('Arial',28),bg='#9fbded', justify="right")
time_dis.grid(row = 0, column=1, pady=10, padx=10, sticky=tk.EW)
#time_dis.place(x=750,y=30)

#Scrollbar for found words
word_list = Listbox(word_frame, width=10,font=("Arial",16), justify="center")
word_list.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=10, pady=5)
# word_list.place(x=600,y=80)

scrollbar1 = tk.Scrollbar(word_frame,orient=VERTICAL)

my_list = []
mylist = Listbox(word_frame, yscrollcommand = scrollbar1.set ) 
scrollbar1.config( command=mylist.yview)   
for i in (my_list):
    word_list.insert(END, i)

#Validation message
vali = tk.Label(word_frame, height=1,text="Waiting for input", font=('Arial',14),fg="#4f0b12",bg="#7792d4")
vali.pack(side=tk.TOP, pady=10)

#Textbox for user input
input = Text(word_frame, height = 1, width = 14,font=('Arial',30))
input.insert(tk.END, "")
input.pack(side=tk.TOP, pady=10)
input.config(state="disabled")

""" create a custom-sized square grid 
and insert the generated seed into the grid """


setup_board()


settings_frame.columnconfigure(0, weight=1)
settings_frame.columnconfigure(1, weight=3)
settings_frame.columnconfigure(2, weight=3)
settings_frame.columnconfigure(3, weight=1)
settings_frame.rowconfigure(0, weight=1)

#start game
startGame = Button(settings_frame, text="START GAME", font=('Arial',28), command=startButton) #Generates a random seed
startGame.grid(row=1, columnspan=4, pady=10)

solve = Button(settings_frame, text="Solve board", font=('Arial',20), command=solveBoard) #Generates a random seed
solve.grid(row=2, columnspan=4, pady=20)

settingsLabel = tk.Label(settings_frame, text = "----- Settings -----", font=('Arial',24), bg='#9fbded')
settingsLabel.grid(row=3, column=1, columnspan=2, pady=10)

def changeGameMode(event=None):
    global gmvariable
    gameLimitText.config(state="normal")
    gameLimitText.delete("1.0","end")
    if gmvariable.get() == "Score Limit":
        gameLimitLabel.config(text = "Score Limit:")
        gameLimitText.insert(tk.END, "100")
    elif gmvariable.get() == "Time Limit":
        gameLimitLabel.config(text = "Time Limit:")
        gameLimitText.insert(tk.END, "3:00")
    elif gmvariable.get() == "Limitless":
        gameLimitLabel.config(text = "")
        gameLimitText.insert(tk.END, "N/A")
        gameLimitText.config(state="disabled")
    pass

gmvariable = StringVar()
gmvariable.set("Limitless")
gameModeLabel = tk.Label(settings_frame, text = "Gamemode:", font=('Arial',20), bg='#9fbded')
gameModeMenu = OptionMenu(settings_frame, gmvariable, *["Limitless", "Score Limit", "Time Limit"], command=changeGameMode)
gameModeLabel.grid(row=4, column=1, pady=10)
gameModeMenu.config(height=1, width=10)
gameModeMenu.grid(row=4, column=2, pady=10)

gameLimitLabel = tk.Label(settings_frame, text = "", font=('Arial',20), bg='#9fbded')
gameLimitText = Text(settings_frame,height = 1, width = 5,font=('Arial',20))
gameLimitText.insert(tk.END, "N/A")
gameLimitText.config(state="disabled")
gameLimitLabel.grid(row=5, column=1, pady=10)
gameLimitText.grid(row=5, column=2, pady=10)

seedLabel = tk.Label(settings_frame, text = "Seed:", font=('Arial',20), bg='#9fbded')
seedText = Text(settings_frame,height = 1, width = 10,font=('Arial',20))
seedText.insert(tk.END, "")
seedLabel.grid(row=6, column=1, pady=10)
seedText.grid(row=6, column=2, pady=10)

#Generate seed
randomSeed = Button(settings_frame, text="Generate random seed", font=('Arial',18), command=generateSeed) #Generates a random seed
randomSeed.grid(row=7, column = 1, columnspan=2)

#Grid size edit
gridSizeLabel = tk.Label(settings_frame, text = "Grid size:", font=('Arial',20), bg='#9fbded')
gridSizeText = Text(settings_frame, height = 1, width = 3,font=('Arial',20))
gridSizeText.insert(tk.END, "4")
gridSizeLabel.grid(row=8, column=1, pady=10)
gridSizeText.grid(row=8, column=2, pady=10)

#min word size
minLengthLabel = tk.Label(settings_frame, text = "Min word length:", font=('Arial',20), bg='#9fbded')
minLengthText = Text(settings_frame, height = 1, width = 3,font=('Arial',20))
minLengthText.insert(tk.END, "3")
minLengthLabel.grid(row=9, column=1, pady=10)
minLengthText.grid(row=9, column=2, pady=10)

#max word size
maxLengthLabel = tk.Label(settings_frame, text = "Max word length:", font=('Arial',20), bg='#9fbded')
maxLengthText = Text(settings_frame, height = 1, width = 3,font=('Arial',20))
maxLengthText.insert(tk.END, "")
maxLengthLabel.grid(row=10, column=1, pady=10)
maxLengthText.grid(row=10, column=2, pady=10)

reset = Button(settings_frame, text="Set to default", font=('Arial',20), command=resetSettings) #Generates a random seed
reset.grid(row=11, columnspan=4, pady=10)

settings_frame.rowconfigure(12, weight=2)

# def wordcheck(word):
#     global word_list, score_dis_score
#     word = word.strip().lower()

#     input.delete("1.0", "end")
#     vali.config(text = "")
#     the_time = "Time: " + str(g.timer.get_time())
#     time_dis.config(text = the_time)

#     displayText = "Waiting for input"

#     if word in g.enteredWords:
#         displayText = "Already entered"
#         # vali.config(text = )
#     else:
#         g.enteredWords += [word]
#         if len(word) < g.minWordLength:
#             displayText = f"Too short, must be at least {g.minWordLength} letters long."
#             # vali.config(text = )
#         elif g.maxWordLength != None and len(word) > g.maxWordLength:
#             displayText = f"Too long, must be at most {g.maxWordLength} letters long."
#             # vali.config(text = 
#         elif not g.board.isOnBoard(word):
#             # penalize guessing random words
#             displayText = "Not on board"
#             # vali.config(text = )
#             score_dis_score -= 5
#             g.score -= 5
#         else:
#             score = game.score(word)
#             if score == None:
#                 displayText = "Not in word list"
#                 # vali.config(text = )
#             else:
#                 displayText = "You found a word"
#                 word_list.insert(END, word)
#                 score_dis_score += score
#                 g.score += score
#     the_score = "Score: " + str(score_dis_score)
#     score_dis.config(text = the_score)
#     vali.config(text = displayText)

def submitButton(event=None):
    enterWord(input.get("1.0", "end-1c"))

input.bind("<Return>", submitButton) 

#Button to submit word
# submit = Button(word_frame, height=2,width=15,text="Submit", font=('Arial',20),command=submitButton)
# submit.pack(side=tk.TOP, pady=10)
#submit.place(x=486,y=450)

root.mainloop()