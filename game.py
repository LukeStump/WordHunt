from board import Board
from timer import Timer
class Game:
    '''Game class that keeps track of score and timer'''

    def __init__(self, limit):
        ''' input limit is 0 for score-based games, nonzero for timed games '''
        self.score = 0
        self.timer = Timer(limit)
        self.board = Board()
        
    def getPlayerInput(self):
        print(self.board)
        return input("Enter a word: ")