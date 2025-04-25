class  Solution:
    def minSwaps(self,s:str)->int:
        balance = 0
        max_balance = 0

        for char in s:
            if char == '[':
                balance+=1
            else:
                balance-=1
            
            if  balance < 0:
                max_balance = max(max_balance, abs(balance))

        # The number of swaps needed is half the maximum balance
        # because each swap can fix two unmatched brackets
        return  (max_balance + 1) // 2