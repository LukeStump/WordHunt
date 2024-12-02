#write data to leaderboard
#probably won't be it's own python file
output = open("leaderboard.txt","w")

#psuedocode
output.write(game_seed + player_name + score + "\n")

#^^ Move this into a different file maybe

d = {} #dictionary for specific game_seed, 
#key = player_name, value = score

"more psuedocode"
"Create a leaderboard for the respective game_seed from the data of leaderboard.txt"
for line in output: #get each line from leaderboard.txt
    data = line.split() #split the data of each line
    if data[0] == (current_seed): #if the seed in the line matches the seed of the current game
        d += data[1] #initialize key
        data[1] = score #set key value?

    #print all the scores down, 