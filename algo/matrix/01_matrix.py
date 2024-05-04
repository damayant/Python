from collections import deque
from typing import List
class Solution:
    def updateMatrix(mat:List[List[int]])->List[List[int]]:

        #check boundaries
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        
        #make local copy of the matrix which will be updated for actual result
        matrix = [row[:] for row in mat]
        m= len(matrix)
        n=len(matrix[0])
        q  = deque()
        seen =  set()

        #1st round to check for zeroes and add those indices to seen set and also to q
        for row in range(m):
            for col  in range(n):
                if matrix[m][n] == 0:
                    q.append(m,n,0)
                    seen.add(m,n)
        
        #define right, left , up , down directions
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            #pop the q elems one by one
            row , col , steps = q.popleft()
            for dx,dy in directions :
                next_row, next_col = row+dx , col+dy
                if(next_row,next_col)not  in seen and valid(next_row,next_col):
                    seen.add(next_row,next_col)
                    q.append(next_row,next_col,steps+1)
                    matrix[next_row][next_col] =  steps+1
        return matrix
                    
