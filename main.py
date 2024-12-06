# The Main file of the Game
import re
# from game import Game
import game
import board

def commandLine():
    # when backend does frontend
    while True:
        options()

def options():
    opts = [("play random", playRandomGame),("compete",compete),("compete [Host]", competeHost),("solve",solve)]
    for i in range(len(opts)):
        print(i+1, opts[i][0])
    opt = int(input(f"[1-{i+1}]:"))
    opt = opts[opt-1][1]
    opt.__call__()

def getGame(boardString = None):
    if boardString == None:
        boardString = input("enter board String:")
    g = None
    if re.match("\w+ \d+x\d+", boardString):
        g = game.makeGameFromBoardString(boardString, scoreLimit=1)
    else:
        g = game.makeGame(4,4, scoreLimit=1)
    return g

def playGame(g):
    try:
        g.gameLoop()    
    except game.GameOver:
        pass

def playRandomGame():
    g = getGame("")
    playGame(g)

def competeHost():
    g = getGame("")
    print(g.getBoardString())
    input("press Enter to start")
    playGame(g)

def compete():
    g = getGame()
    print(g.getBoardString())
    input("press Enter to start")
    playGame(g)

def solve():
    g = getGame()
    g.timer.start_time()
    trie = board.createBoardTrie(g.board)
    g.score = trie.countTotalWordLength()
    try:
        g.gameOver()
    except game.GameOver:
        pass


if __name__ == "__main__":
    commandLine()