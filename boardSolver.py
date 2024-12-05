class trieNode:
    def __init__(self, children=None, end = False):
        if children == None:
            children = [None]*26
        assert len(children) == 26
        self.children = children
        self.end = end