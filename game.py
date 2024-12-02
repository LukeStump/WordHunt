from board import Board
from timer import Timer
class Game:
    def __init__(self, board, timeLimit = None, minWordLength = 3, scoreLimit = 100):
        ''' input limit is None for score-based games, nonzero for timed games '''
        self.board = board
        self.score = 0
        self.minWordLength = minWordLength
        self.timer = Timer(timeLimit)
        
    def getPlayerInput(self):
        """ displays the timer and board and returns what the player types in
        """
        print(self.timer.get_time())
        print(self.board)
        word = input("Enter a word: ")
        return word.strip().lower()
    
    def scorePlayerInput(self):
        while True:
            word = self.getPlayerInput()
            if len(word) < self.minWordLength:
                print(f"Too short, must be at least {self.minWordLength} letters long.")
                continue
            if not self.board.isOnBoard(word):
                # penalize guessing random words
                print("Not on board")
                return -5
            points = score(word)
            if points == None:
                print("Not in word list")
                continue
    
    def checkGameOver():
        pass

    def gameOver():
        pass

            
        
    

def score(word):
    """ returns the score of a word based off of its length and rarity
        input word: String
        note that this does not check that it is on the game board
    """
    length = len(word)
    mit = occurs(word.lower(),"mitDictionary.txt")
    scrabble = occurs(word.upper(), "scrabbleDictionary.txt")

    if not (mit or scrabble):
        return None
    
    # only mit is 2x, only scrabble is 1x, both is 3x
    multiplier = 2*mit + scrabble

    return length*multiplier

def occurs(word, fileName):
    file = open(fileName, "r")
    for line in file:
        if word == line.strip():
            return True
    return False

# testing
if __name__ == "__main__":
    while(True):
        word = input().strip()
        print(score(word))
