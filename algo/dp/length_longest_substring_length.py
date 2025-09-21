from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        """
        We want the length of the longest subsequence whose sum = target.
        If no such subsequence exists, return -1.
        """

        # Step 1: Create a DP array where
        # dp[s] = the maximum length of a subsequence that sums to 's'
        # Initialize everything as -1 (meaning: "unreachable sum")
        dp = [-1] * (target + 1)

        # Step 2: Base case → sum=0 can always be made with empty subsequence of length 0
        dp[0] = 0

        # Step 3: Process each number one by one
        for num in nums:
            # We iterate backwards so that each number is only used once
            # (classic trick from 0/1 knapsack)
            for s in range(target, num - 1, -1):
                # Can we reach sum = s-num?
                if dp[s - num] != -1:
                    # Yes → we can extend that subsequence by adding 'num'
                    new_length = dp[s - num] + 1
                    dp[s] = max(dp[s], new_length)  # keep the best (longest) length

        # Step 4: Our answer is dp[target], if it's still -1 then no subsequence exists
        return dp[target]
