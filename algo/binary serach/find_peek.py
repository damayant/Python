from typing import List


class Solution:
    def findPeekElement(nums:List[int])->int:
        if len(nums) ==  1 :
            return 0
    
        left , right =  0 , len(nums)-1

        while left<=right :
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left

    print(findPeekElement(nums=[3,4,3,2,1]))
        