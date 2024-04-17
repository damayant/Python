from typing import List


class Solution :
    def removeDuplicates(nums: List[int]) -> int:
        hashmap = {}
        count = len(nums)
        i = 0
        while i != count:
            if nums[i] not in hashmap :
                hashmap[nums[i]] = 1
            else :
                hashmap[nums[i]] += 1
                if hashmap[nums[i]] > 2:
                    nums.remove(nums[i])
                    count -= 1
                    i-= 1
            i+= 1
        
        return len(nums)

    def removeDuplicatesWithoutHashmap(nums:List[int])->int:
        # Initialize the counter and the second pointer.
        j, count = 1, 1
        
        # Start from the second element of the array and process
        # elements one by one.
        for i in range(1, len(nums)):
            
            # If the current element is a duplicate, 
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
            
            # For a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array
            if count <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j
    
    print(removeDuplicatesWithoutHashmap(nums = [1,1,2,2,3,3,3]))
                

