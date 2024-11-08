# keeps track of the board state
class Board:
    def __init__(self, letters):
        self.letters = letters

    def __str__(self):
        b = [" ".join(list(r)) for r in self.letters]
        sep = "—"*len(b[-1])
        b = [sep] + b + [sep]
        return "\n".join(b)


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
            if self.getLetter(c) != rest[0]:
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

