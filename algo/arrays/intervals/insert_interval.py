from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval :
            return [newInterval]
        if newInterval[0] == 0 and newInterval[1] == 0:
            intervals.insert(0,newInterval)
            return intervals
        intervals.sort(key=lambda x:x[0])
        merged = []
        start = 0
        end = 0
        count = len(intervals)-1
        interval = []
        i = 0
        flag = False

        while i <= count:
            interval = intervals[i]
            #case 1 : check if the current arr lower than range of new arr or already merged
            if interval[1] <newInterval[0] or end!= 0:
                merged.append(interval)
            #found is in range
            else: 
                #case 2: check if lower boundary of current arr > lower boundary of new
                if interval[0] > newInterval[0] :
                    #check if lower boundary of current 
                    if interval[0] > newInterval[1] :
                        merged.append(newInterval)
                        end = newInterval[1]
                        i-=1
                    else :
                        start = newInterval[0]
                        if interval[1] >= newInterval[1]:
                            end = max(interval[1],newInterval[1])
                            merged.append([start,end])
                        else :
                            i += 1
                            if i <=count :
                                interval = intervals[i]
                                flag = True

                if interval[0] <= newInterval[0] or flag == True:
                    if flag == False :
                        start = interval[0]
                    while (i <= count) and  (interval[0] < newInterval[1] and interval[1]<newInterval[1]):
                        i += 1
                        if i<= count:
                            interval = intervals[i]
                    if interval[0]<=newInterval[1]<=interval[1]:
                        end = interval[1]
                        merged.append([start,end])
                    else:
                        end = newInterval[1]
                        merged.append([start,end])
                        i -= 1
            i+=1

        if end == 0 :
            merged.append(newInterval)
        
        
        return merged
        
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        
    insert(intervals = [[1,5]], newInterval = [0,3])
                    

