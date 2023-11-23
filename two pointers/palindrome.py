class Solution:
    def isPalindrome(s:str)->bool:
        filtered_str = filter(lambda ch: ch.isalnum(),s)
        lowercase_filtered_str = map(lambda ch:ch.lower(),filtered_str)

        filtered_char_list = list(lowercase_filtered_str)
        reversed_filtered_char_list = filtered_char_list[::-1]

        return filtered_char_list == reversed_filtered_char_list
    

    print(isPalindrome(s="A man, a plan, a canal: Panama"))