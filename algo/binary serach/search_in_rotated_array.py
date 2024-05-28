from typing import List


class Solution:
    def search(nums:List[int],target:int)->int:
        left , right = 0 , len(nums)-1
        
        while left <=right :
            mid = (left+right)//2
            if nums[mid]== target:
                return mid
            if nums[left]<=nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left =  mid + 1
                else:
                    right =  mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid -1
                else :
                    left = mid + 1
        return -1
    
    print(search(nums=[4,5,6,7,0,1,2], target=0))
