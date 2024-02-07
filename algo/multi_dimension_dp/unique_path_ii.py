from typing import List


class Solution :
    def uniquePathsWithObstacles_solutionOne (grid:List[List[int]])->int :
        #time : O(m*n) , spce : O(n*m)
        m , n = len(grid) , len(grid[0])

        dp = {(m-1,n-1):1}

        def dfs(r,c):
            if r == m or c == n or grid[r][c] :
                return 0 
            if(r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] =  dfs(r+1,c) +dfs(r,c+1)

            return dp(r,c)
        return dfs(0,0)


    

    uniquePathsWithObstacles_solutionOne(grid = [[0,0,0],[0,1,0],[0,0,0]])