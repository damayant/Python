from typing import List


class Solution:
    def searchInsert(nums:List[int],target:int)->int:
        start ,  mid , end = 0 , 0, len(nums)-1
     
        while start<=end:
            mid = (end + start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                end = mid - 1
            else:
                start = mid + 1
        # print(start,mid,end)
        return start
        


    




    print(searchInsert(nums = [1,2,4,6,7], target = 3))