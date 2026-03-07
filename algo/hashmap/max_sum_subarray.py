from typing import List


class Solution:
    def subarraySum(self,nums:List[int],k:int)->int:
        count, current_sum = 0, 0
        prefix_sum = {0:1}

        for num in nums:
            current_sum += num
            if (current_sum-k) in prefix_sum:
                count += prefix_sum[current_sum-k]
            
            prefix_sum[current_sum] = prefix_sum.get(current_sum,0)+1
        
        return count 
    
sol = Solution()
print(sol.subarraySum(nums=[1,2,3],k=3))