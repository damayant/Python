#BFS Solution

from typing import Collection, List
from collections import deque


class Solution:
    def numIslands(grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        count,visit=0,set()
        direction=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col=q.popleft() #for dfs simply use pop() instead of popleft()
                
                for dr,dc in direction:
                     r,c=row+dr,col+dc
                     if (r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]=="1"):
                         q.append((r,c))
                         visit.add((r,c))
                     
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and ((r,c) not in visit):
                    bfs(r,c)
                    count+=1

        print(count)
        return count
        

    numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])