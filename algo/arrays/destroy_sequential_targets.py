from typing import List


class Solution:
    def destroyTargets(self,nums:List[int],space:int):
        remainder_map=defaultdict(list)

        #step 1: group numbers by remainder
        for num in nums:
            remainder_map[num%space].append(num)

        #step 2 : find max frequency
        max_freq=0
        for rem in remainder_map:
            max_freq=max(max_freq,len(remainder_map[rem]))

        
        #step 3 : among those groups , chose the samllest numbers
        result=float('inf')
        for rem,group in remainder_map.items():
            if len(group)==max_freq:
                result=min(result,min(group))
        
        return result