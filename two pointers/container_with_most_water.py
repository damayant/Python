from typing import List


class Solution:
    def maxArea(height:List[int])->int:
        maxarea = 0 
        left = 0 
        right = len(height)-1

        while left<right :
            width = right - left
            maxarea = max(maxarea,min(height[left],height[right])*width)
            #if left pillar is small then keep moving towrds right so increase left pointer
            if height[left]<= height[right]:
                left+=1
            #if right pillar is smaller then keep moving towards left hence decrease right pointer
            else:
                right -=1
        return maxarea

    print(maxArea(height = [1,8,6,2,5,4,8,3,7]))