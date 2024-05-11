import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        
        rows, cols =  len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q :
                row, col = q.popleft()
                for dx, dy in directions:
                    new_row , new_col = row+dx , col+dy
                    if (new_row in range(rows) and
                        new_col in range(cols) and
                        grid[new_row][new_col] == '1' and
                        (new_row,new_col) not in visit):
                        q.append((new_row,new_col))
                        visit.add((new_row,new_col))

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1') and (r,c) not in visit :
                    bfs(r,c)
                    islands += 1
        return islands
