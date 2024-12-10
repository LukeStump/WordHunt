import time
class Timer:
    def __init__(self, limit):
        ''' input limit is None for score-based games, nonzero for timed games '''
        self.time_limit = limit
        self.time_start = None

    def is_limited(self):
        return self.time_limit != None
    
    def start_time(self):
        ''' marks current time and stores as self.time_start'''
        self.time_start = time.time()
    
    def get_time(self, raw=False):
        ''' if there is a time limit, returns the amount of time left.
            otherwise, returns amount of time passed since game start '''
        if self.is_limited():
            return self.get_time_remaining(raw=raw)
        else:
            return self.get_time_elapsed(raw=raw)
    
    def get_time_elapsed(self, raw=False):
        t = time.time() - self.time_start
        if not raw:
            t = format_time(t)
        return t

    def get_time_remaining(self, raw=False):
        t = self.time_limit - (time.time() - self.time_start)
        if not raw:
            t = format_time(t)
        return t
    
def format_time(the_time):
    ''' returns input the_time converted into a minutes:seconds format '''
    seconds = int(the_time)
    if seconds >= 60:
        minutes = seconds // 60
        seconds %= 60
    else:
        minutes = 0
    if seconds < 10:
        return str(minutes) + ":0" + str(seconds)
    else:
        return str(minutes) + ":" + str(seconds)