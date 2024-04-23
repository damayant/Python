class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = 1
            else :
                char_map[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in char_map or char_map[t[i]] == 0 :
                return False
            else:
                char_map[t[i]] -= 1
            
        return len(s) == len(t)


        