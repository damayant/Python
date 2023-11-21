from typing import List


class Solution:
    def longestOnes(nums:List[int],k:int)->int:
        start = 0
        end = start+1
        count = 0
        max_count = count
        counter = k

        while end<len(nums):
            while(counter!=0):
                if(nums[start]==1):
                    count += 1
                elif(nums[start]==0):
                    count+=1
                    counter -= 1
                start += 1
                end += 1
            max_count = max(max_count,count)
            count = 0
            counter = k
        print(max_count)
        return max_count
    
    longestOnes(nums=[1,1,1,0,0,0,1,1,1,1,0],k=2)
