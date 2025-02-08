from typing import List


class Solution:
    def longestOnes(nums:List[int],k:int)->int:
        left = right = 0
        for right in range(len(nums)):
            # print(right)
            #if we encounter 0 then decrement k
            if(nums[right]==0):
                k -= 1
            #else no impact to k
            #if k <0 then we need to move left part of window forward to try and remove extra 0s
            if k<0:
                #if the left one was zero then we adjust k
                if(nums[left]==0):
                    k+=1
                #regardless of whether we had a 1 or 0 we can move left side by 1
                #if we keep seeing 1s the window still keeps moving as is
                left += 1
        return right - left + 1

        
    
    longestOnes(nums=[1,1,1,0,0,0,1,1,1,1,0],k=2)
