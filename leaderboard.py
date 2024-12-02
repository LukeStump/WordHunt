#write data to leaderboard
#probably won't be it's own python file
output = open("leaderboard.txt","w")

#psuedocode
output.write(game_seed + player_name + score + "\n")

#^^ Move this into a different file maybe
d = {} #dictionary

"more psuedocode"
for line in output: #get each line from leaderboard.txt
    data = line.split() #split the data of each line
    if data[0] == (current_seed) #if the seed in the line matches the seed of the current game