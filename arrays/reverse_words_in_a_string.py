class Solution :
    def reverseWords(s:str)-> str :
        str_list = s.split()
        str_list.reverse()

        return ' '.join(str_list)