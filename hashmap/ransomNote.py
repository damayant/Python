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



    print(canConstruct(ransomNote = "aa", magazine = "aab"))
