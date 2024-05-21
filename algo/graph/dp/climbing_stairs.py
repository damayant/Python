class Solution:
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        dp = []
        dp.append(1)
        dp.append(2) 

        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]
#https://www.youtube.com/watch?v=UUaMrNOvSqg