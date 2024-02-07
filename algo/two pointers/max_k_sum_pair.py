from typing import List


class Solution:
    def maxOperations(nums:List[int],k:int)->int:
        left = 0
        right = len(nums)-1
        nums.sort()
        ans = 0

        while left<right:
            sum = nums[left]+nums[right]
            if(sum==k):
                ans += 1
                left+=1
                right-=1
            else:
                if(sum>k):
                    right-= 1
                if(sum<k):
                    left+=1

        
        return ans

    print(maxOperations(nums=[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k = 2))
    
