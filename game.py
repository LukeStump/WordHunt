class Game:
    def __init__(self, board):
        self.board = board

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