class Solution:
    def findLongestPalindromicSubstring(s:str)->int:
        hash_set = set() #hash set will capture only the chars occuring in odd number
        for c in s :
            if c not in hash_set:
                hash_set.add(c)
            else:
                hash_set.remove(c)
        
        # if len(hash_set)>0:
        #     return len(s) - len(hash_set)+1
        # else:
        #     return len(s)
        return len(s)-len(hash_set)+1 if len(hash_set)>0 else len(s)
    
    print(findLongestPalindromicSubstring(s = "abccccdd"))


'''
A quick explanation:
Let's take a look at what our hash looks like in our test case.
"abccccdd"
{'a', 'b'}

You'll notice that it's only the characters that appear an odd amount of times in our string that get saved
This is because for all even occurrences of a letter we are guaranteed to be able to make a palindrome.

i.e.
ccddcc
dccccd
cdccdc

As you can see a length of 6 from the c's and d's can be acquired

So where does this plus 1 come into play?
len(s) - len(hash) + 1
In a purely even palindrome we can add back at most one odd occurrence of a letter

ex:
ccdadcc
ccdbdcc

if len(hash) == 0
This means all the characters occur an even amount of times in the string and the length of the string itself should be returned
ex.
"ccccdd" -> "ccddcc" length 6

Furthermore let's say that the that a and b were 3 characters long
"aaabbbccccdd"
in that case the hash would look exactly the same
since for every time we put an element in the set we remove it if we see it again only the odd occurring elements appear again.
{'a', 'b'}

as such our resulting palindrome would look something like this
"abccd" + "a" + "dccba" with either a or b as a possible middle character.
'''
