while f_ptr<len(nums_arr):
            if nums_arr[f_ptr]<nums_arr[s_ptr]:
                while s_ptr<len(nums_arr) :
                    if nums_arr[high_index]<nums_arr[s_ptr]:
                        high_index=s_ptr
                        swap=True
                    s_ptr+=1
                if swap==True:
                    temp=nums_arr[f_ptr]
                    nums_arr[f_ptr]=nums_arr[high_index]
                    nums_arr[high_index]=temp
                    return int("".join(map(str, nums_arr)))
            else:
                f_ptr+=1
                s_ptr=f_ptr+1
        return num
            