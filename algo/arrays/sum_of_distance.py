from collections import defaultdict
from typing import List


class Solution:
    def sum_of_distance(self,nums:List[int])->List[int]:
        index_map=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    index_map[i]+=abs(i-j)
                    index_map[j]+=abs(i-j)
        return index_map
    
    def sum_of_distance_optimized(self, nums: List[int]) -> List[int]:
        index_map = [0] * len(nums)
        positions = defaultdict(list)

        # Step 1: Group indices by value
        for i, num in enumerate(nums):
            positions[num].append(i)

        # Step 2: For each group of positions, calculate distances using prefix sums
        for indices in positions.values():
            prefix = [0] * len(indices)
            prefix[0] = indices[0]
            for i in range(1, len(indices)):
                prefix[i] = prefix[i - 1] + indices[i]

            total = prefix[-1]
            n = len(indices)
            for i in range(n):
                left = i * indices[i] - (prefix[i - 1] if i > 0 else 0)
                right = (prefix[-1] - prefix[i]) - (n - i - 1) * indices[i]
                index_map[indices[i]] = left + right

        return index_map
            
# Example usage:
sol = Solution()
print(sol.sum_of_distance_optimized([1,3,1,1,2]))
                
