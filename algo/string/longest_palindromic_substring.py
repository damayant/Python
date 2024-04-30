class Solution:
    def findLongestPalindromicSubstring(s:str)->int:
        hash_set = set()
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
