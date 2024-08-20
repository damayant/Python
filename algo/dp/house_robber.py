from typing import List


class Solution:
    def rob_with_memoziation(nums:List[int])->int:
        length=len(nums)
        #base cases
        if length == 0 : return 0
        if length == 1 : return nums[0]
        if length == 2 : return max(nums[0],nums[1])

        dp = [] 
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))

        for  i in range(2,length):
            dp.append(max(dp[i-2]+nums[i],dp[i-1])) 

        return dp[length-1]
    
    #optimization of the above memoziation with respect to time complexity
    def rob_with_two_ptr(nums:List[int])->int:
        result,m1,m2=0,0,0
        for i in range(len(nums)):
            result = max(nums[i]+m2,m1)
            m2=m1
            m1=result
        return result
    