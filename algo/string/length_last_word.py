class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        #trim trailing spaces as starting from end ie right of string
        end= len(s)-1
        while end>=0 and s[end]==' ':
            end-=1
        
        #start counting the length of last word
        while end>=0 and s[end]!=' ':
            end-=1
            count+=1
        
        return count
    
    print(lengthOfLastWord(None,s = "Hello World"))
    print(lengthOfLastWord(None,s = "   fly me   to   the moon  "))
    print(lengthOfLastWord(None,s = "luffy is still joyboy))"))