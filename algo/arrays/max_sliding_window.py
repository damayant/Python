from collections import deque
from typing import List


def maxSlidingWindow(nums:List[int],window_size:int)->List[int]:
    if not nums or len(nums)<window_size:
        return nums 
    q= deque()
    result = [] 
    for index in range(len(nums)):
        window_start_index = index - window_size + 1
        #remove indexes that are no longer inside the window
        if (q and q[0]<window_start_index):
            q.popleft()
        #remove all smaller elements from the back as they can never become the max
        while (q and nums[q[-1]]<nums[index]):
            q.pop()
        q.append(index)
        #record max once the first complete window is formed
        if index >= window_size - 1 :
            result.append(nums[q[0]])
    return result

maxSlidingWindow([1,2,3,4,1,3,5],3)