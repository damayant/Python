class Solution:
    def coinChange(self, coins, amount):
        # Initialize memoization table with None
        self.memo = [None] * (amount + 1)
        return self._coin_change_helper(coins, amount)
    
    def _coin_change_helper(self, coins, remaining):
        # Base Case 1: If remaining amount is negative, no solution possible
        if remaining < 0:
            return -1
        
        # Base Case 2: If remaining amount is 0, no more coins are needed
        if remaining == 0:
            return 0

        # Check if result is already computed (memoization)
        if self.memo[remaining] is not None:
            return self.memo[remaining]

        # Initialize min_coins to infinity to track minimum number of coins needed
        min_coins = float('inf')

        # Try every coin and reduce remaining amount recursively
        for coin in coins:
            result = self._coin_change_helper(coins, remaining - coin)
            if result == -1:
                continue  # Skip if no solution for this path
            min_coins = min(min_coins, result + 1)

        # If min_coins was not updated, it means no solution found
        self.memo[remaining] = -1 if min_coins == float('inf') else min_coins
        return self.memo[remaining]

# Example usage:
solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
# print(solution.coinChange([2], 3))          # Output: -1 (no solution)