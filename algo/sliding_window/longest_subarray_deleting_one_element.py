from typing import List

#https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/3719628/beats-100-video-java-c-pyhton/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestSubarray(nums:List[int])->int:
        left = right = 0
        count = max_count = 0
        
        max_count = 0

        for i in range(len(nums)):
            if(nums[i]==1):
                right += 1
            else:
                max_count = max(max_count,right+left)
                left = right
                right = 0
        max_count = max(max_count,right+left)
        
        if(max_count == len(nums)):
            return max_count - 1
        else:
            return max_count
    
    print(longestSubarray(nums=[0,1,1,1,0,1,1,0,1]))
