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
        """
        n = self.getChildNum(character)
        if self.children[n] == None:
            self.children[n] = TrieNode(end=end)
        elif end == True:
            self.children[n].end = True


    def getChildNum(self, character):
        """ returns the branch number represented by the character
        """
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
