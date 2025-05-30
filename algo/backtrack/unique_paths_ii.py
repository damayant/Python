from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols=len(obstacleGrid),len(obstacleGrid[0])
        self.result=0
        target_row,target_col=rows-1,cols-1
        # If start or end is an obstacle, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[target_row][target_col] == 1:
            return 0

        def dfs(row,col):
            if row == target_row and col == target_col:
                self.result+=1
                return
            
            if not (0<=row<rows and 0<=col<cols) :
                return 
            if obstacleGrid[row][col]==1:
                return
            
            temp=obstacleGrid[row][col]
            obstacleGrid[row][col]=1

            for dr,dc in [(1,0),(0,1)]:
                dfs(row+dr,col+dc)

            obstacleGrid[row][col]=temp  
            
        dfs(0,0)
        return self.result
            
    #the above solution is not optimal. The time complexity is O(2^(m+n)) where m is the number of rows and n is the number of columns.
    #The space complexity is O(m*n) for the recursion stack.
    #The above solution can be optimized using memoization or dynamic programming.
    #The optimized solution is as follows:

    def uniquePathsWithObstaclesOptimizedSolution(self, obstacleGrid: List[List[int]]) -> int:   
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        target_row,target_col=rows-1,cols-1
        memo={}
        # If start or end is an obstacle, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0
        
        def dfs(row,col):
            # Base case: if we reach the target cell
            if row == target_row and col == target_col:
                return 1
            
            # Check if out of bounds or if the cell is an obstacle
            if not (0<=row<rows and 0<=col<cols) :
                return 0 
            if obstacleGrid[row][col]==1:
                return 0
            
            # Check if the result is already computed
            if (row,col) in memo:
                return memo[(row,col)]
            
            # explore the two possible directions: down and right
            # and store the result in the memoization dictionary
            memo[(row,col)]= dfs(row+1,col)+dfs(row,col+1)
            return memo[(row,col)]
        return dfs(0,0)
        