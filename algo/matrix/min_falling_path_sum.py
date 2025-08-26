import math
from typing import List


class Solution:
    def minFallingPathSum(self,matrix:List[List[int]])->int:
        rows,cols=len(matrix),len(matrix[0])
        memo={}

        def dfs(row,col):
            #base case 1: if out of bounds
            if col not in range(cols):
                return math.inf
            
            #base case 2: if reached last row
            if row==rows-1:
                return matrix[row][col]
            
            #memoization check
            if (row,col) in memo:
                return memo[(row,col)]
            
            #recursively find out the best path sum for that cell in first row
            best = matrix[row][col] + min(
                dfs(row+1,col-1),   #bottom left diagonal
                dfs(row+1,col),     #bottom cell straight down
                dfs(row+1,col+1)    #bottom right diagonal
            )

            memo[(row,col)]=best 

            return best

        return min(dfs(0,c) for c in range(cols))