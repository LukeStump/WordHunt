import time
class Timer:
    def __init__(self, limit):
        ''' input limit is None for score-based games, nonzero for timed games '''
        self.time_limit = limit
        self.time_start = 0
    
    def start_time(self):
        ''' marks current time and stores as self.time_start'''
        self.time_start = time.time()
    
    def get_time(self):
        ''' if there is a time limit, returns the amount of time left.
            otherwise, returns amount of time passed since game start '''
        if self.time_limit != None:
            return self.time_limit - (time.time() - self.time_start)
        else:
            return time.time() - self.time_start