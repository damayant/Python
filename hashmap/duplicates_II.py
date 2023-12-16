from typing import List


class Solution:
    def duplicates(nums:List[int],k:int)->bool:
        hashmap = {}

        for i in range(0,len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]= i
            else:
                diff = abs(i-hashmap[nums[i]])
                if diff <= k :
                    return True
                else:
                    hashmap[nums[i]] = i
        return False


    print(duplicates(nums = [1,0,1,1], k = 1))
