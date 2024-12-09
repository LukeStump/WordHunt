import board as brd
from timer import Timer
import sys
class Game:
    def __init__(self, board, seed=None, timeLimit = None, minWordLength = 3, maxWordLength = None, scoreLimit = 100):
        ''' input limit is None for score-based games, nonzero for timed games '''
        self.board = board
        self.score = 0
        self.minWordLength = minWordLength
        self.maxWordLength = maxWordLength
        self.scoreLimit = scoreLimit
        self.timer = Timer(timeLimit)
        self.enteredWords = []
        self.correctWords = []
        self.seed = seed
    
    def reset(self):
        self.score = 0
        self.enteredWords = []
        self.correctWords = []
        self.timer = Timer(self.timer.timeLimit)
        
    def getPlayerInput(self):
        """ displays the timer and board and returns what the player types in
        """
        print("time:",self.timer.get_time())
        print("score:",self.score)
        print(self.board)
        word = input("Enter a word: ")
        return word.strip().lower()
    
    def scorePlayerInput(self):
        # outdated
        while True:
            self.checkGameOver()
            word = self.getPlayerInput()
            if word in self.enteredWords:
                print("Already entered")
                continue
            self.enteredWords += [word]
            if len(word) < self.minWordLength:
                print(f"Too short, must be at least {self.minWordLength} letters long.")
                continue
            if self.maxWordLength != None:
                if len(word) > self.maxWordLength:
                    print(f"Too long, must be at most {self.minWordLength} letters long.")
                continue
            if not self.board.isOnBoard(word):
                # penalize guessing random words
                print("Not on board")
                return -5
            points = score(word)
            if points == None:
                print("Not in word list")
                continue
            return points
    
    def enterWord(self, word):
        """ returns a tuple of (points, message) where points is how many points were earned
            and message is a string to display to the user
        """
        word = word.strip().lower()
        if word in self.enteredWords:
            return (0, "Already Entered")
        self.enteredWords.append(word)

        if self.minWordLength != None and len(word) < self.minWordLength:
            return (0, f"Too short, must be ≥{self.minWordLength} letters long.")
        if self.maxWordLength != None and len(word) > self.maxWordLength:
            return (0, f"Too long, must be ≤{self.minWordLength} letters long.")

        if self.board.trie.exists(word):
            self.correctWords.append(word)
            pts = score(word, True)
            self.score += pts
            return (pts, "")
        
        if self.board.isOnBoard(word):
            return (0, "Not in word list")
        
        # self.score = max(self.score - 5, 0)
        self.score -= 5
        return (-5, "Not on Board")


    def solve(self):
        """ finds every possible word and tallies the points
            returns (points, time) where points is the total points and time is how long it took
        """
        self.timer.start_time()
        # redundant but good to include in timing
        trie = brd.createBoardTrie(self.board)
        words = trie.getWordList()
        points = [score(w, True) for w in words]
        pts = sum(points)

        self.enteredWords = words
        self.correctWords = words
        self.score = pts

        return (pts, self.timer.get_time_elapsed())


    
    def gameLoop(self):
        self.timer.start_time()
        while(True):
            pts = self.scorePlayerInput()
            self.score += pts
    
    def isGameOver(self):
        """ checks if the requirements for the game to end have been fulfilled
        """
        if self.timer.is_limited():
            if self.timer.get_time() <= 0:
                return True
        else:
            if self.score >= self.scoreLimit:
                return True
        return False
    
    def checkGameOver(self):
        """ checks if the requirements for the game to end have been fulfilled
            calls gameOver if they have
        """
        if self.isGameOver():
            self.gameOver()

    def gameOver(self):
        """ ends the game
        """
        print("---- Game Over ----")
        print(f"score: {self.score}")
        print(f"time: {self.timer.get_time()}")
        print(self.getBoardString())
        print("-------------------")
        raise GameOver()
        # sys.exit()
    

    def getBoardString(self):
        seedString = "<custom>" if self.seed == None else self.seed
        return f"{seedString} {self.board.rows}x{self.board.columns}"

class GameOver(Exception):
    pass
            
        
    

def score(word, garunteed = False):
    # TODO make faster (only check MIT? just by length?)
    """ returns the score of a word based off of its length and rarity
        input word: String
        note that this does not check that it is on the game board
    """
        
    length = len(word)
    mit = occurs(word.lower(),"mitDictionary.txt")

    if not garunteed:
        scrabble = occurs(word.upper(), "scrabbleDictionary.txt")

        if not (mit or scrabble):
            return None
    
    # only scrabble is 1x, mit is 2x
    multiplier = 2 if mit else 1

    return length*multiplier

def occurs(word, fileName):
    file = open(fileName, "r")
    for line in file:
        if word == line.strip():
            return True
    return False



def makeGame(rows, columns, timeLimit=None, scoreLimit=100, minWordLength=3, maxWordLength = None, seed=None):
    if seed == None:
        seed = brd.generateSeed()
    b = brd.makeRandomBoard(rows, columns, seed)
    game = Game(b, seed=seed, timeLimit=timeLimit, minWordLength=minWordLength, scoreLimit=scoreLimit, maxWordLength=maxWordLength)
    return game

def makeGameFromBoardString(boardString: str, timeLimit=None, scoreLimit=100, minWordLength=3):
    s = boardString.split(" ")
    seed = s[0]
    s = s[1]
    s = s.split("x")
    rows = int(s[0])
    columns = int(s[1])
    return makeGame(rows, columns, timeLimit, scoreLimit, minWordLength, seed)



# testing
if __name__ == "__main__":
    gameBoard = brd.makeBoard("OATRIHPSHTNRENEI",4,4)
    seed = brd.generateSeed()
    print("seed:", seed)
    gameBoard = brd.makeRandomBoard(4,4,seed)
    g = Game(gameBoard)
    g.gameLoop()