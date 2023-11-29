#https://www.youtube.com/watch?v=TjFXEUCMqI8
from typing import List


class Solution:
    def isValidSudoku(board:List[List[str]])->bool:
        N = 9

        #use hash-set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                #check if the position is filled with number
                if val == ".":
                    continue
                    
                #check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                #check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                #check the box
                idx = (r//3)*3 + c//3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
            
        return True

    
    print(isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))