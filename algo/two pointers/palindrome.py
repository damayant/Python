class Solution:
    def isPalindrome(s:str)->bool:
        filtered_str = filter(lambda ch: ch.isalnum(),s)
        lowercase_filtered_str = map(lambda ch:ch.lower(),filtered_str)

        filtered_char_list = list(lowercase_filtered_str)
        reversed_filtered_char_list = filtered_char_list[::-1]

        return filtered_char_list == reversed_filtered_char_list
    
    def twoPointer(s:str)->bool:
        i = 0 
        j = len(s)-1

        while i<j :
            print(s[i])
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            
            if s[i].lower()!= s[j].lower():
                return False
        return True
    

    print(twoPointer(s="A man, a plan, a canal: Panama"))