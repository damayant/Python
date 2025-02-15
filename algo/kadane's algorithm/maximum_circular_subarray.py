# https://www.youtube.com/watch?v=fxT9KjakYPM
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max ,global_min = nums[0], nums[0]
        cur_max, cur_min = 0,0
        total = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)

            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)

            total += num

        return max(global_max, total - global_min) if global_max > 0 else global_max
    # print(maxSubarraySumCircular(None, [-3,-2,-3]))
    maxSubarraySumCircular(None, [5,-3,5])