import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = -math.inf
        low = math.inf
        result = 0
        for i in range(len(prices)-1):
            #check two  adjacent elements
            #if current price is higher than next day price then check if next day price is lower than the low 
            if prices[i] > prices[i+1]:
                #checking if next day price is lower than the low
                if prices[i+1] < low :
                    #if next day price is lower than next day price then low = next day price
                    low = prices[i+1] 
                    #after the new low price , the current high price also needs to be changed as cannot be previous day high price
                    high = prices[i+2] if (i+2) < len(prices) else high
                #increase the index
                i= i+1
            else :
                #if current price is lesser than next day price check if current low price is lower than current low
                low = prices[i] if prices[i] <low else low
                high = prices[i+1] if prices[i+1] > high else high
                result = max((high - low), result)
        return result


        