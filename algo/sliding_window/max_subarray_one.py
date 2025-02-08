#You are given an integer array nums consisting of n elements, and an integer k.
#Find a contiguous subarray 
# whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.
#Example
#Input: nums = [1,12,-5,-6,50,3], k = 4
#Output: 12.75000
#Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


from typing import List


class Solution:
    def findMaxAverage(nums:List[int],k:int)->float :
        
        if(len(nums)) == 1 :
            return float(nums[0])

        start = 0
        end = k
        avg = 0.0

        #calculate avg of 1st window
        for i in range(k):
            avg += float(nums[i])/k
        
        #initialize max avg
        max_avg =  avg

        #slide the window and update the max avg
        while end<len(nums):
            avg = avg - float(nums[start])/k
            avg = avg + float(nums[end])/k
            max_avg =  max(max_avg,avg)
            start += 1
            end += 1

        print(max_avg)
        return max_avg

    
    findMaxAverage(nums= [1,12,-5,-6,50,3],k=4)