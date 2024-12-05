#written on a separate file for now
import tkinter as tk
'''GUI.................'''
root = tk.Tk()

root.geometry("600x600") #window size
root.title("Leaderboard")

#Score text
score_dis = tk.Label(root, text = "Leaderboard", font=('Arial',20))
score_dis.pack(padx=20, pady=20)

#create a custom-sized square grid and insert the generated seed into the grid

root.mainloop()
'''GUI end'''


#write game data to leaderboard
#probably won't be it's own python file
output = open("leaderboard.txt","w")

#psuedocode
#output.write(game_seed + player_name + score + "\n")

#^^ Move this into a different file maybe



#key = player_name, value = score

"more psuedocode"
"store scores of specific seed into a dictionary"
def seed_leaderboard(current_seed):
    d = {} #dictionary for specific game_seed, 
    for line in output: #get each line from leaderboard.txt
        data = line.split() #split the data of each line
        if data[0] == (current_seed): #if the seed in the line matches the seed of the current game
            d += data[1] #initialize key (player)
            data[1] = data[2] #set key value (score)
    print(d)
        #print all the scores in the window
seed_leaderboard("test_seed")