from typing import List


class Solution:
    def productExceptSelf(nums:List[int])->List[int]:
        #initiat empty result arr of size of nums arr with all 1 
        #as that will take care of the edge cells
        result = [1]*(len(nums))

        #initiate prefix with 1
        prefix = 1
        #loop through nums array from left to right 
        #multiplying the cells before except for edge cell on left
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        #initiate the postfix
        postfix =  1
        #now loop through in reverse direction from right to left
        #and multiply the previous cells with prfix except for the
        #edge cell on right
        for i in range((len(nums)-1),-1,-1):
            result[i] = result[i]*postfix
            postfix*=nums[i]
        return result
    print(productExceptSelf(nums=[1,2,3,4]))