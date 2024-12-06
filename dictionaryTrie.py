import pickle
import trie

readOnInit = True

dictionaryTrie = None
def getDictionaryTrie():
    global dictionaryTrie
    if dictionaryTrie == None:
        try:
            dictionaryTrie = readFromFile()
        except FileNotFoundError:
            dictionaryTrie = createDictionaryTrie()
            writeTrieToFile(dictionaryTrie)

    return dictionaryTrie

fileName = "dictionaryTrie.pickle"
def writeTrieToFile(trie):
    file = open(fileName, "wb")
    pickle.dump(trie,file)

def readFromFile():
    file = open(fileName, "rb")
    out = pickle.load(file)
    return out

def createDictionaryTrie(dicts = ["mitDictionary.txt", "scrabbleDictionary.txt"]):
    # global defaultWordTrie
    wordList = []
    for dict in dicts:
        file = open(dict)
        wordList += file.readlines()
    wordList = [w for w in wordList if len(w.strip())>=3]
    return trie.createTrie(wordList)

def generate(test = True):
    print("Generating...")
    wordTrie = createDictionaryTrie()
    print("Writing...")
    writeTrieToFile(wordTrie)
    if test:
        print("Reading...")
        read = readFromFile()
        print("Checking...")
        for word in wordTrie.getWordList():
            if not read.exists(word):
                print("Error: read trie does not contain:",word)
    print("Done")

if readOnInit:
    getDictionaryTrie()

if __name__ == "__main__":
    generate()