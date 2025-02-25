from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows , cols = len(image), len(image[0])
        current_color = image[sr][sc]
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        q=deque()

        if current_color == color :
            return image
        else:
            image[sr][sc]=color
        
        q.append((sr,sc))

        while q:
            r,c=q.popleft()
            for dx,dy in directions:
                new_row,new_col=r+dx,c+dy 
                if new_row in range(rows) and new_col in range(cols) and image[new_row][new_col]==current_color:
                    image[new_row][new_col]=color
                    q.append((new_row,new_col))
        
        return image


    floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)        