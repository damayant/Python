from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        freq_limit = len(nums)//2
        _map = {}
        for i in range(len(nums)):
            if nums[i] not in _map:
                _map[nums[i]] = 1
            else:
                _map[nums[i]] += 1
                if _map[nums[i]] > freq_limit :
                    return nums[i]
        return 0
    
    def majorityElementWithNoExtraSpace(self, nums: List[int]) -> int:
        count ,current_major_element = 1 ,nums[0]  
        for i in range(1,len(nums)):
            if nums[i] != current_major_element :
                count = count - 1 if count >0 else 0
                if count == 0:
                    current_major_element = nums[i]
                    count = 1
            else:
                count = count +1
        return current_major_element