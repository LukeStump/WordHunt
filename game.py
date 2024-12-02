import time
class Game:
    '''Game class that keeps track of score and timer'''

    def __init__(self, limit):
        ''' input limit is 0 for score-based games, nonzero for timed games '''
        self.score = 0
        self.time_limit = limit
        self.time_start = 0
    
    def start_time(self):
        ''' marks current time and stores as self.time_start'''
        self.time_start = time.time()
    
    def get_time(self):
        ''' if there is a time limit, returns the amount of time left.
            otherwise, returns amount of time passed since game start '''
        if self.time_limit != 0:
            return self.time_limit - (time.time() - self.timer)
        else:
            return time.time() - self.timer