# https://www.youtube.com/watch?v=jzZsG8n2R9A&t=13s
# recommend doing two sum-input sorted array first 
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def twoSum_one(nums:List[int],i:int,res:List[List[int]]):
            lo = i+1
            hi = len(nums)-1

            while(lo<hi):
                sum = nums[i]+nums[lo]+nums[hi]
                if sum < 0 :
                    lo += 1
                elif sum >0 :
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo<hi and nums[lo] == nums[lo-1]:
                        lo += 1
                        
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i == 0 or nums[i-1] !=nums[i]:
                twoSum_one(nums,i,res)
        return res

    

print(threeSum(nums = [-1,0,1,2,-1,-4]))