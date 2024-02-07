from typing import List


class Solution :
    def insert(intervals:List[List[int]], newInterval: List[int])->List[List[int]]:
        if not intervals and newInterval :
            return [newInterval]
        intervals.sort(key=lambda x:x[0])
        merged = []
        start = 0
        end = 0
        count = len(intervals)-1
        interval = []
        i = 0

        while i <= count:
            interval = intervals[i]
            if interval[1] <newInterval[0] or end!= 0:
                merged.append(interval)
            else: 
                if interval[0] <= newInterval[0]:
                    start = interval[0]
                    while (i <= count) and  (interval[0] < newInterval[1] or interval[1] < newInterval[1]):
                        i += 1
                        if i<= count:
                            interval = intervals[i]
                    if interval[0]<=newInterval[1]<=interval[1]:
                        end = max(interval[0],interval[1])
                        merged.append([start,end])
                    else:
                        end = newInterval[1]
                        merged.append([start,end])
                        i -= 1
            i+=1

        if start == 0 or end == 0 :
            merged.append(newInterval)
        
        
        return merged
        
        
    insert(intervals = [[1,5]], newInterval = [0,3])
                    

