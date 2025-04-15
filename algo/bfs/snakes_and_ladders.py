from collections import deque
from typing import List

# https://www.youtube.com/watch?v=6lH4nO3JfLk 

class Solution:
    def snakesAndLadders(self,board:List[List[int]])->int:
        length=len(board)
        board.reverse()

        def intToPosition(square):
            r=(square-1)//length
            c=(square-1)%length
            if r%2==length%2:
                return [r,length-1-c]
            return [r,c]
        
        q=deque()
        q.append([1,0])
        visited=set()

        while q:
            square,moves=q.popleft()
            for i in range(1,7):
                next_square=square+i
                r,c=intToPosition(next_square)
                if board[r][c]!=-1:
                    next_square=board[r][c]
                if next_square==length*length:
                    return moves+1
                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square,moves+1])
        return -1