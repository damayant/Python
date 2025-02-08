# https://www.youtube.com/watch?v=5WZl3MMT0Eg
# https://www.youtube.com/watch?v=AHZpyENo7k4

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)
        return max_sum 
    print(maxSubArray(None, [-2,1,-3,4,-1,2,1,-5,4]))