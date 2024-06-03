from typing import List


class Solution:
    def sortColors(nums:List[int])-> None:
        i , left_ptr, right_ptr = 0, 0, len(nums)-1

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= right_ptr :
            #move all 0s to left
            if nums[i] == 0 :
                swap(i,left_ptr)
                #move left_ptr to right 
                left_ptr += 1
            #move all 2s to right
            if nums[j] ==  2:
                swap(i,right_ptr)
                #move right_ptr to left
                right_ptr -= 1
                #for right ptr move we are not incrementing i
                i -= 1
            i += 1 