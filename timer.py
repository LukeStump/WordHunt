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
    
    def get_time(self):
        ''' if there is a time limit, returns the amount of time left.
            otherwise, returns amount of time passed since game start '''
        if self.is_limited():
            return self.format_time(self.time_limit - (time.time() - self.time_start))
        else:
            return self.format_time(time.time() - self.time_start)
    
    def format_time(self, the_time):
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