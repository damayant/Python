from typing import List


class Solution:
    def searchInsert(nums:List[int],target:int)->int:
        start ,  mid , end = 0 , 0, len(nums)-1
        if target > nums[end]:
            return end + 1
        if target <= nums[start]:
            return start
        while start<end:
            mid = (end + start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                end = mid - 1
            else:
                start = mid + 1
        print(start,mid,end)
        if nums[mid] > target :
            return mid 
        else :
            return mid + 1 
        


    




    print(searchInsert(nums = [1,2,4,6,7], target = 3))