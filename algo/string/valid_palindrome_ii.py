def palidrome(s:str)->bool:
    left_ptr=0
    right_ptr=len(s)-1

    while left_ptr<right_ptr:
        if s[left_ptr]!=s[right_ptr]:
            skipL=s[left_ptr+1:right_ptr+1]
            skipR=s[left_ptr:right_ptr]
            return (skipL==skipL[::-1]) or (skipR==skipR[::-1])
        left_ptr=left_ptr+1
        right_ptr=right_ptr-1
    return True 

