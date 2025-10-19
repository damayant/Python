class Solution:
    def numDecode(self,s:str)->int:
        length = len(s)
        memo = {}

        def dfs(i):
            #base cases
            if i == length:    #reached end successfully
                return 1    
            if s[i] == 0: #invalid start with 0
                return 0 
            if i in memo: #use cached result
                return memo[i]
            
            #1-digit decode
            ways=dfs(i+1)

            #2-digit decode - if number valie 10-26
            if (i+1)<length and 10<=int(s[i:i+2])<=26:
                ways+=dfs(i+2)
            
            #cache in memo
            memo[i]=ways 
            return ways 
        
        return dfs(0)


            
            
    
sol = Solution()
print(sol.numDecode('226'))