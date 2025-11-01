class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s)==1:
            return len(s) 
        if len(s) == 2:
            if s[0] != s[1]:
                return len(s) 
        
        visit = set()  
        start , end = 0, 1
        max_len = -math.inf
    

        while end <len(s) and start < end :
            start_char = s[start]
            visit.add(start_char)
            while end < len(s) and (s[end]) not in visit:
                visit.add(s[end])
                end+=1  
            max_len = max(max_len,len(s[start:end]))
            for i in range(start,end):
                visit.remove(s[i])
            start +=1
            end = start+1

        return max_len