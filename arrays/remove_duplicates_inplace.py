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
        fptr , sptr = 0 , 0
        count = len(nums)
        if count == 1 or count == 2 or count == 0:
            return count
        repeat = 0
        
        while(sptr<count):
            if nums[fptr] == nums[sptr]:
                while sptr < count and nums[fptr] == nums[sptr] :
                    repeat+= 1
                    sptr += 1
                if repeat>2:
                    for i in range(fptr+1,sptr-1):
                        nums.pop(i)
                        sptr-=1
            fptr = sptr
            sptr+= 1
            count = len(nums)
        
        return len(nums)
    
    print(removeDuplicatesWithoutHashmap(nums = [1,1,1,2,2,3]))
                

