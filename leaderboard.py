#write game data to leaderboard
#probably won't be it's own python file
"Variables"
infile = open("leaderboard.txt","r", encoding='utf-8')
d = {} #dictionary for specific game_seed : #key = player_name, value = score
current_seed = "test_seed" #seed of the current game


"store scores of specific seed into a dictionary"
for line in infile: #get each line from leaderboard.txt
    data = line.split() #split the data of each line

    #if the seed in the line matches the seed of the current game
    if data[0] == (current_seed):
        d[data[1]] = data[2] #add player and score to dictionary

def get_scores():
    return d 
"Testing to see if the code works"
for i in d:
    print(i, d[i]) #print all the scores in the window

