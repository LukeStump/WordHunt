# The Main file of the Game
import re
# from game import Game
import game
import board
import dictionaryTrie

def commandLine():
    # when backend does frontend
    while True:
        options()

def options():
    opts = [("play random", playRandomGame),("compete",compete),("compete [Host]", competeHost),("solve",solve),("solve [print]",solvePrint),("view board", viewBoard),("check word",checkWord)]
    for i in range(len(opts)):
        print(i+1, opts[i][0])
    opt = int(input(f"[1-{i+1}]:"))
    opt = opts[opt-1][1]
    opt.__call__()

def getGame(boardString = None, scoreLimit = 64):
    if boardString == None:
        boardString = input("enter board String:")
    g = None
    if re.match("\w+ \d+x\d+", boardString):
        g = game.makeGameFromBoardString(boardString, scoreLimit=scoreLimit)
    else:
        g = game.makeGame(4,4, scoreLimit=scoreLimit)
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
    return trie

def solvePrint():
    trie = solve()
    print(trie.getWordList())

def viewBoard():
    g = getGame()
    print(g.board)
    print(g.getBoardString())

def checkWord():
    word = input("enter word:")
    print(dictionaryTrie.getDictionaryTrie().exists(word))


if __name__ == "__main__":
    commandLine()

#BLOEGLNG 4x4
#RNNDOXRO 4x4