import board

class TrieNode:
    def __init__(self, children=None, end = False):
        if children == None:
            children = [None]*26
        assert len(children) == 26
        self.children = children
        self.end = end


    def addNewChild(self, character, end = False):
        """ adds a new child on the branch represented by the character if one is not present
                garuntees getChild(character) != None
            and if end is True
                garuntees getChild(character).end == True
            returns the new child
        """
        n = self.getChildNum(character)
        if n >= 26 or n < 0:
            print("err:",character,n)
        if self.children[n] == None:
            self.children[n] = TrieNode(end=end)
        elif end == True:
            self.children[n].end = True
        return self.children[n]
    
    def addWord(self, word, end = True):
        """ adds a word to the trie
        """
        trie = self
        for c in word[:-1]:
            trie = trie.addNewChild(c)
        c = word[-1]
        trie.addNewChild(c, end=True)


    def getChildNum(self, character):
        """ returns the branch number represented by the character
        """
        assert character != "\n"
        return ord(character.lower()) - ord('a')

    def getChild(self, character):
        """ returns the child at the branch represented by the character
        """
        return self.children[self.getChildNum(character)]
    

    def traverse(self, word):
        """ travrses the trie down the given word, and returns the trie from that point,
            or None if the word is not present
        """
        trie = self
        while len(word) > 0 and trie != None:
            trie = trie.getChild(word[0])
            word = word[1:]
        return trie
    
    def exists(self, word, ensureEnd=True):
        """ returns weather the given word is represented in the trie
        """
        trie = self.traverse(word)
        if trie == None:
            return False
        return trie.end or not ensureEnd

def createTrie(wordList):
    """ returns a Trie that includes exactly the words in wordList
    """
    trie = TrieNode()
    for word in wordList:
        trie.addWord(word.strip())
    return trie


defaultWordTrie = None
def getDefaultWordTrie():
    if defaultWordTrie == None:
        createDefaultWordTrie()
    assert defaultWordTrie != None
    return defaultWordTrie

def createDefaultWordTrie(dicts = ["mitDictionary.txt", "scrabbleDictionary.txt"]):
    global defaultWordTrie
    wordList = []
    for dict in dicts:
        file = open(dict)
        wordList += file.readlines()
    defaultWordTrie = createTrie(wordList)
    

def createBoardTrie(b: board.Board):
    outTrie = TrieNode()

    for coord in b.getAllCoords():
        fillTrie(b,[coord],getDefaultWordTrie(),outTrie)

    return outTrie

def fillTrie(b: board.Board, coords, wordTrie: TrieNode, boardTrie: TrieNode):
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




if __name__ == "__main__":
    wordList = ["efhowe", "esofjheoifh", "efjehi", "efj", "fsheiufef", "euigwhfujskn", "e", "fshe"]
    notWords = ["irthw", "esofjheoif", "ef"]
    trie = createTrie(wordList)
    for w in wordList:
        assert trie.exists(w)
    for w in notWords:
        assert not trie.exists(w)

    # b = board.makeBoard("OATRIHPSHTNRENEI",4,4)
