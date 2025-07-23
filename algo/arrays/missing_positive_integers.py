from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums_present=set(arr)
        nums_absent=[]
        num=1

        while len(nums_absent)<=k:
            if num not in nums_present:
                nums_absent.append(num)
            num+=1
        
        return nums_absent[k-1]
        