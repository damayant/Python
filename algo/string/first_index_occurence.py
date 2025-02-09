class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)
    
    def twoPointer(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        result=0
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                result=i
                j=0 
                while j<len(needle):
                    if haystack[j+i]==needle[j]:
                        j+=1
                if j==len(needle):
                    return result
        return -1 
    print(twoPointer(None,haystack = "sadbutsad", needle = "sad"))
