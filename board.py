import random
from trie import TrieNode #, getDefaultWordTrie
from dictionaryTrie import getDictionaryTrie
# keeps track of the board state
class Board:
    def __init__(self, letters):
        self.letters = letters
        self.trie = createBoardTrie(self)

    def __str__(self):
        b = [" ".join(list(r)) for r in self.letters]
        sep = "—"*len(b[-1])
        b = [sep] + b + [sep]
        return "\n".join(b)
    
    def getAllCoords(self):
        out = []
        for r in range(len(self.letters)):
            for c in range(len(self.letters[r])):
                out.append((r,c))
        return out

    def getLetter(self, coord):
        return self.letters[coord[0]][coord[1]]
    
    def isOnBoard(self, word):
        """ returns True if and only if the word can be made with adjacent tiles (no repeats)
            input word: String
        """
        word = word.upper()
        for r in range(len(self.letters)):
            for c in range(len(self.letters[r])):
                if self.getLetter((r,c)) != word[0]:
                    continue
                if self.searchForRest(word[1:],[(r,c)]):
                    return True
        return False
    
    def searchForRest(self, rest, tiles):
        """ returns True if and only if rest can be made with adjacent tiles (no repeats) starting from tiles[-1]
                and not using any tiles in tiles
            input rest: String
            input tiles: list of coordinates that have been used already
        """
        if rest == "":
            return True
        start = tiles[-1]
        adj = self.getAdjacent(start)
        for c in adj:
            if c in tiles or self.getLetter(c) != rest[0]:
                continue
            if self.searchForRest(rest[1:],tiles[:]+[c]):
                return True
        return False
        
    def getAdjacent(self, coord):
        """ returns a list of all valid coords directly adjacent to the given coord
            input coord: a tuple (row, column)
        """
        adj = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if x==0 and y==0:
                    continue
                c = (coord[0] + x, coord[1] + y)
                if self.isValidCoord(c):
                    adj.append(c)
        return adj

    def isValidCoord(self, coord):
        """ returns True if and only if coord refers to a valid spot on the grid
            input coord: a tuple (row, column)
        """
        row = coord[0]
        col = coord[1]
        return row >= 0 and row < len(self.letters) and col >= 0 and col < len(self.letters[row])

def makeBoard(letters, rows, columns):
    assert len(letters) == rows*columns
    letters = letters.upper()
    board = [""]*rows
    for i in range(rows):
        board[i] = letters[i*columns:(i+1)*columns]
    return Board(board)

def generateSeed(length = 8):
    random.seed()
    out = ""
    for i in range(length):
        out += getRandomLetter()
    return out

def getRandomLetter():
    # TODO use weights instead
    return "AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ"[random.randint(0, 97)]

def makeRandomBoard(rows, columns, seed: str, maxRepeats = 2):
    assert rows*columns < 26*maxRepeats
    seed = seed.upper()
    random.seed(seed)

    # generate random string of letters
    letters = ""
    while len(letters) < rows*columns:
        letter = getRandomLetter()
        while letters.count(letter) >= maxRepeats:
            letter = getRandomLetter()
        letters += letter
    
    # shuffle string (for reasons)
    l = list(letters)
    random.shuffle(l)
    letters = "".join(l)

    return makeBoard(letters, rows, columns)


def createBoardTrie(b: Board):
    outTrie = TrieNode()

    for coord in b.getAllCoords():
        fillTrie(b,[coord],getDictionaryTrie(),outTrie)

    return outTrie

def fillTrie(b: Board, coords, wordTrie: TrieNode, boardTrie: TrieNode):
    """ fills the trie with all possible words starting from coords[-1]
    """

    for coord in b.getAdjacent(coords[-1]):
        if coord in coords:
            continue
        c = b.getLetter(coord)
        restWordTrie = wordTrie.getChild(c)
        if restWordTrie == None:
            continue
        restBoardTrie = boardTrie.addNewChild(c, end = restWordTrie.end)
        fillTrie(b, coords + [coord], restWordTrie, restBoardTrie)


def unit_test():
    import boardSolver
    board = makeBoard("OATRIHPSHTNRENEI",4,4)
    tests_pos = ["hit", "ptihnn", "stahp", "that", "pne", "sri", "oat", "ohn", "ohtaitprsnireneh"]
    tests_neg = ["hine", "thin", "ptz", "jelly", "aot", "tnt", "oatrsrienphtnenio", "oatao"]
    boardTrie = boardSolver.createBoardTrie(board)
    wordTrie = boardSolver.getDictionaryTrie()
    for test in tests_pos:
        isWord = wordTrie.exists(test)
        assert board.isOnBoard(test)
        assert boardTrie.exists(test) == isWord
    for test in tests_neg:
        assert not board.isOnBoard(test)
        assert not boardTrie.exists(test)

def playTest():
    # import boardSolver
    # board = makeBoard("OATRIHPSHTNRENEI",4,4)
    # seed = input("seed: ")
    seed = generateSeed()
    print("seed:", seed)
    board = makeRandomBoard(8, 8, seed, 3)
    print(board.trie.getWordList())
    while(True):
        print(board)
        word = input()
        print(board.isOnBoard(word))

if __name__ == "__main__":
    getDictionaryTrie()
    # unit_test()
    playTest()
