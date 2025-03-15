class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num=str(num)
        if len(str_num)==0 or len(str_num)==1:
            return num
        nums=[]
        for char in str_num:
            nums.append(int(char))
        length=len(nums)
        max_digit, max_i=0,-1
        swap_i,swap_j=-1,-1
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i]>max_digit:
                max_digit=nums[i]
                max_i=i 
            if nums[i]<max_digit:
                swap_i,swap_j=i,max_i
        nums[swap_i],nums[swap_j]=nums[swap_j],nums[swap_i]
                

        return int(''.join(map(str,nums)))


            

                    

            

                    
