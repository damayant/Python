from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self,strs:List[str])->List[List[str]]:
        char_map=defaultdict(list)

        for string in strs:
            #count character in each word
            count=[0]*26
            for char in string:
                count[ord(ch)-ord('a')]+=1
            
            #use tuple of counts as keys
            key=tuple(count)
            char_map[key].append(string)

        return list(char_map.values())