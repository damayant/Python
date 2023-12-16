from typing import List


class Solution:
    def groupAnagrams(strs:List[str])->List[List[str]]:
        sets = {}
        ascii_sum = 0
        for st in strs :
            for ch in st:
                ascii_sum += ord(ch)
            if(ascii_sum not in sets):
                sets[ascii_sum]  = [st]
            else:
                if(len(sets[ascii_sum][0]) == len(st)):
                    sets[ascii_sum].append(st)
            ascii_sum = 0

        result = []
        for key,value in sets.items():
            result.append(value)
        
        print(result)

        return result
    
    groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
            
            
                
