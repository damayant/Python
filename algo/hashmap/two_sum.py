from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        result = [0]
    
        for i in range (len(nums)):
            remainder = target - nums[i]
            #insert the current element if not there in hashmap
            if nums[i] not in _map :
                _map[nums[i]] = i
            #check if the rem is there in hashmap
            if remainder in _map:
                #case 1 :  when rem is  not equal to the current  element
                if remainder != nums[i]:
                    result[0]= i
                    result.append(_map[remainder])
                    return result
                #case 2: when the remainder is equal to the current  element ie two same /equal numbers
                else :
                    #in  that case check if the second same number has a diff index than its previous copy
                    if i != _map[nums[i]]:
                        result[0] = _map[nums[i]]
                        result.append(i)
                        return result