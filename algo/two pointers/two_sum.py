from typing import List


class Solution:
    def twoSum(nums:List[int],target:int)->List[int]:
        left = 0

        for left in range(0,len(nums)):
            for right in range(1,len(nums)):
                sum = nums[left] + nums[right]
                if(sum == target):
                    return [left,right]
                
        return []
    
    def twoSumImprovedComplexity(nums:List[int],target:int)->List[int]:
        hash_set ={}
        for i in range(len(nums)):
            rem = target - nums[i]
            if(rem in hash_set):
                return [i,hash_set[rem]]
            else:
                hash_set[nums[i]] = i
        return []

    def twoSumWithSortedArray(nums:List[int],target:int)->List[int]:
        left = 0 
        right =  len(nums)-1

        while(left<right):
            sum = nums[left] + nums[right]
            if(sum == target):
                return [left,right]
            elif sum<target:
                left += 1
            else:
                right -=1
        return []

            
        

    
    print(twoSumImprovedComplexity(nums = [3,2,4], target = 6))