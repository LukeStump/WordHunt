#write data to leaderboard
#probably won't be it's own python file
output = open("leaderboard.txt","w")

#psuedocode
output.write(game_seed + player_name + score + "\n")

"more psuedocode"
for line in output: #get each line from leaderboard.txt
    data = line.split() #split the data of each line
    if data[0] == (current_seed) #if the seed in the line matches the seed of the current game
        #add it to a dictionary which will then be sorted