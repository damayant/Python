from typing import List


class Solution:
    def longestSubarray(nums:List[int])->int:
        left = right = 0
        count = max_count = 0
        k= 1

        for right in range(len(nums)):
            if(nums[right] == 0):
               k -= 1
            if(k<0):
                left += 1 
                count = 1
        
        print(right-left-count)

        return right - left + 1

    longestSubarray(nums=[0,1,1,1,0,1,1,0,1])
