class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        self.result=0
        empty_squares=0
        start_row,start_col=0,0

        #find starting position and calculate the non-obstacle squares
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    start_row,start_col=r,c 
                elif grid[r][c]==0:
                    empty_squares+=1
        
        def dfs(r,c,remaining):
            #check boundaries and obstacles
            if not (0<=r<rows and 0<=c<cols) or grid[r][c]==-1:
                return 
            #if ending square is reached
            if grid[r][c]==2:
                if remaining==-1: #The remaining variable represents the number of non-obstacle squares that need to be visited. This includes all squares with values 0 (empty squares) and 1 (the starting square).
                    self.result+=1
                return
            
            #mark the square as visited
            temp=grid[r][c] 
            grid[r][c]=-1 

            #explore all direction 
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r+dr,c+dc,remaining-1) ##The remaining variable represents the number of non-obstacle squares that need to be visited. This includes all squares with values 0 (empty squares) and 1 (the starting square).

            #backtrack
            grid[r][c]=temp 

        dfs(start_row,start_col,empty_squares)

        return self.result