class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     dp = []
    #     dp.append(1)
    #     dp.append(2) 

    #     for i in range(2,n+1):
    #         dp.append(dp[i-1] + dp[i-2])
    #     return dp[n-1]
    def climbStairsHelper(self,n,memo):
        if n not in memo:
            memo[n]=self.climbStairsHelper(n-2,memo)+self.climbStairsHelper(n-1,memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo={0:1,1:1}
        return self.climbStairsHelper(n,memo)