from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # We need an array to store the min coins for each amount from 0 to 'amount'.
        # The size is 'amount + 1' to include the 0 index.
        min_coins_for_amount = [float('inf')] * (amount + 1)
        
        # --- The Base Case ---
        # It takes 0 coins to make an amount of 0.
        min_coins_for_amount[0] = 0
        
        # --- Build the Solution from the Bottom Up ---
        # We loop through every single amount from 1 up to the target amount.
        for current_amount in range(1, amount + 1):
            
            # For this 'current_amount', try using each coin we have.
            for coin in coins:
                
                # We can only use a coin if it's not larger than the amount we're trying to make.
                if current_amount - coin >= 0:
                    
                    # This is the core logic:
                    # Is the current best way to make 'current_amount' (which is 'min_coins_for_amount[current_amount]')
                    # WORSE than the '1 + min_coins_for_amount[current_amount - coin]'?
                    #
                    # '1 + min_coins_for_amount[current_amount - coin]' means:
                    # "The cost to make the amount *before* I added this coin, plus one (for this coin)."
                    
                    min_coins_for_amount[current_amount] = min(
                        min_coins_for_amount[current_amount], 
                        1 + min_coins_for_amount[current_amount - coin]
                    )
        
        # --- The Final Answer ---
        # After the loops, min_coins_for_amount[amount] holds the answer for the target amount.
        final_answer = min_coins_for_amount[amount]
        
        # If the value is still 'infinity', it means we were never able to
        # find a combination of coins to make that amount.
        if final_answer == float('inf'):
            return -1
        else:
            return int(final_answer) # Return as an integer
        
        
# Example usage:
solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
# print(solution.coinChange([2], 3))          # Output: -1 (no solution)