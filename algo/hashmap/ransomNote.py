import collections


class Solution:
    def canConstruct(ransomNote:str,magazine:str)->bool:
        source_map = {}
        for  ch in magazine:
            if(ch not in source_map):
                source_map[ch] = 1
            else:
                source_map[ch] += 1

        for ch in ransomNote:
            if(ch in source_map):
                if(source_map[ch]>0):
                    source_map[ch]-=  1
                else:
                    return False
            else:
                return False
        return True
    
    def withCounter(ransomNote:str,magazine:str)->bool:
        #check for obvious fail case
        if len(ransomNote)>len(magazine):return False
        #in python we can use the counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
        letters=collections.Counter(magazine)
        # For each character, c, in the ransom note:
        for c in ransomNote:
        # If there are none of c left, return False.
            if letters[c]<=0:
                return False
        #remove one of c from counter
            letters[c]-=1
        return True
    
        #time complexity : O(m+n)
        #space complexity : O(n)






    print(canConstruct(ransomNote = "aa", magazine = "aab"))
