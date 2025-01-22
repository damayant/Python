from typing import List


class Solution:
    def rotate(nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

    rotate(nums = [1,2,3,4,5,6,7], k = 3)

    def rotate_solution_two(nums:List[int],k:int):
        def rev(left:int,right:int):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        rev(0,len(nums)-1) #reverts the entire array
        rev(0,k-1)
        rev(k,len(nums)-1)
        return nums
    rotate_solution_two(nums = [1,2,3,4,5,6,7], k = 3)