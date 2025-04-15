from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , cols = len(board),len(board[0])

        def capture(r,c):
            if(r<0 or c<0 or r== rows or c == cols or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        #DFS - capture unsurrounded regions (O->T)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O") and (r in [0,rows-1] or c in [0,cols-1]) :
                    capture(r,c)
        
        #capture surrounded regions (O->X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = 'X'

        #uncature unsorrounded regions(T->O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        