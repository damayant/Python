import math
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Phase 1: Maximum profit up to each day
        n = len(prices)
        max_profit_1 = [0] * n
        min_price = math.inf
        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit_1[i] = max(max_profit_1[i - 1] if i > 0 else 0, prices[i] - min_price)
        
        # Phase 2: Maximum profit from each day to the end
        max_profit_2 = [0] * n
        max_price = -math.inf
        for i in range(n - 1, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit_2[i] = max(max_profit_2[i + 1] if i < n - 1 else 0, max_price - prices[i])
        
        # Combine results for two transactions
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_profit_1[i] + max_profit_2[i])
        
        return max_profit
