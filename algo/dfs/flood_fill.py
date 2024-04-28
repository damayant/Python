from typing import List


class Solution:
    def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #calculate the size of the matrix
        row , col = len(image), len(image[0])
        #get the current color of the sr,sc block in matrix
        current_color = image[sr][sc]

        #if current color of the sr,sc block is the new color return the matrix
        if current_color == color :
            return image

        
        def dfs(r, c):
            if image[r][c] == current_color :
                image[r][c] = color

                #check adjacent top
                if r >=1:
                    dfs(r-1,c)
            
                if r+1 < row :
                    dfs(r+1,c)

                if c>=1 :
                    dfs(r,c-1)

                if c+1 <col:
                    dfs(r,c+1)
        dfs(sr,sc)
        print(image)
        return image

    floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)        