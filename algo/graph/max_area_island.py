class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        island_sum,visit=[],set()
        direction=[(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            i_sum =grid[r][c]

            while q:
                row,col=q.popleft()
                for dr,dc in direction:
                    new_row,new_col=row+dr,col+dc
                    if ( (new_row in range(rows)) and (new_col in range(cols)) and grid[new_row][new_col]!=0 and (new_row,new_col) not in visit):
                        q.append((new_row,new_col))
                        visit.add((new_row,new_col))
                        i_sum+=grid[new_row][new_col]

            island_sum.append(i_sum)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!=0 and (r,c) not in visit:
                    bfs(r,c)

        return max(island_sum) if len(island_sum)>0 else 0
        