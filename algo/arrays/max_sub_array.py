from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        curr_subarr = nums[0]
        max_subarr = nums[0]

        for i in range(1,len(nums)):
            curr_subarr = max(nums[i],curr_subarr+nums[i])
            max_subarr = max(max_subarr,curr_subarr)
        return max_subarr