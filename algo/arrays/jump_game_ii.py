# https://www.youtube.com/watch?v=dJ7sWiOoK7g
class Solution:
    def jump(self,nums:List[int])->int:
        if len(nums)==1:
            return 0
        jumps=0
        left,right=0,0

        while right<len(nums)-1:
            farthest=0
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
            left=right+1
            jumps+=1

        return jumps