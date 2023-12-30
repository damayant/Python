from typing import List


class Solution :
    def merge(intervals : List[List[int]])->List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals :
            #if the list of merged intervals is empty or 
            #if the current interval does not overlap with previous , simply append it
            if  not merged or merged[-1][1] <interval[0] : 
                merged.append(interval)
            else:
                #otherwise, there is an overlap, so merge the current and previous interval
                merged[-1][1] = max(merged[-1][1],interval[1])
        
        return merged

    merge(intervals = [[1,3],[2,6],[8,10],[15,18]])


#Time complexity : 
