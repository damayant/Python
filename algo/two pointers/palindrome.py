class Solution:
    def isPalindrome(s:str)->bool:
        filtered_str = filter(lambda ch: ch.isalnum(),s)
        lowercase_filtered_str = map(lambda ch:ch.lower(),filtered_str)

        filtered_char_list = list(lowercase_filtered_str)
        reversed_filtered_char_list = filtered_char_list[::-1]

        return filtered_char_list == reversed_filtered_char_list
    
    def isPalindrome(self, s: str) -> bool:
        filter_s = filter(lambda ch: ch.isalnum(),s)# This line removes all non-alphanumeric characters (such as spaces, punctuation, etc.).
        filtered_lower_s = map(lambda ch :ch.lower(),filter_s) # converts all remaining characters to lowercase using map()
        filter_list = list(filtered_lower_s) #Converts the filtered and lowercased characters into a list for easy indexing.
        i , j = 0, len(filter_list)-1
        # print(filter_list)
        while i<j :
            if filter_list[i] != filter_list[j]:
                return False
            else : 
                i+= 1
                j-= 1
        return True
    

    print(isPalindrome(None,s="A man, a plan, a canal: Panama"))


    '''
Input:
s = "A man, a plan, a canal: Panama"
Execution:
Remove non-alphanumeric characters: "AmanaplanacanalPanama"
Convert to lowercase: "amanaplanacanalpanama"
Convert to list:
['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
Compare first and last characters:
a == a ✅
m == m ✅
a == a ✅
...
All match.
Output: True (It is a palindrome)
'''