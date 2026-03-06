class RecentCounter:
    def __init__(self):
        self.requests = []
        self.result = []
    
    def ping(self,t:int):
        self.requests.append(t)
        lower_limit, upper_limit = 0,0
        count = 0 
        for request in self.requests:
            if lower_limit<=request<=upper_limit:
                count+=1
        self.result.append(count)
        return self.result[-1]