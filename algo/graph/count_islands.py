from collections import deque
from typing import List


class Solution:
    def countIsland(self,grid:List[List[int]],k:int)->int:
        rows,cols=len(grid),len(grid[0])
        island_sum,visit=[],set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        count = 0

        def bfs(r,c):
            q= deque()
            q.append((r,c))
            visit.add((r,c))
            sum=grid[r][c]

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    new_row,new_col=row+dr,col+dc 
                    if ((new_row in range(rows)) and (new_col in range(cols)) and (grid[new_row][new_col]!=0) and (new_row,new_col) not in visit):
                        q.append((new_row,new_col))
                        visit.add((new_row,new_col))
                        sum+=grid[new_row][new_col]
            
            island_sum.append(sum)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!=0 and (r,c) not in visit:
                    bfs(r,c)

        for island in island_sum:
            if island%k == 0 :
                count+=1

        return count 
    
solution=Solution()

print(solution.countIsland([[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5))