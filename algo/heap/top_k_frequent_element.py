import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies of all elements
        frequency_map = Counter(nums)

        # Step 2: Build a min-heap of size k with (frequency, element) pairs
        top_k_heap = []
        for num, frequency in frequency_map.items():
            heapq.heappush(top_k_heap, (frequency, num))
            if len(top_k_heap) > k:
                heapq.heappop(top_k_heap)  # Keep only k most frequent

        # Step 3: Extract the k most frequent elements from the heap
        top_k_elements=[]
        for frequency, element in top_k_heap:
            top_k_elements.append(element)
        return top_k_elements
    
    #Time complexity: O(N log k), where N is the number of elements in nums: O(N) for counting frequencies and O(log k) for each insertion into the heap.
        # Space complexity: O(k) for the heap and O(N) for the frequency map.

    # Alternative approach using bucket sort
    # This approach is more efficient when k is small compared to the number of unique elements in nums.
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies of all elements
        frequency_map = Counter(nums)
        #Step 2: Create a list of buckets where index i contains all elements with frequency i 0(N)
        bucket=[]
        for _ in range(len(nums)+1):
            bucket.append([])
        for num, frequency in frequency_map.items():
            bucket[frequency].append(num)
        # Step 3: Collect the top k frequent elements starting from highest freq
        result = []

        # Go through the bucket in reverse (from high freq to low)
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                # Once we have collected k elements, return the result
                if len(result) == k:
                    return result
    
# Test cases

sol = Solution()
sol.topKFrequent2([1,1,1,2,2,2,3], 2) 
# Expected output: [1, 2]

    
