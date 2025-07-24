from typing import List


class SudokuSolver:
    def __init__(self,board:List[List[str]]):
        self.board=board 
        self.grid_size=9

    def solve(self)->None:
        self.solve_sudoku()
    
    def solve_sudoku(self)->bool:
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col]==".":
                    for digit in map(str,range(1,10)):
                        if self.is_valid_placement(row,col,digit):
                            self.board[row][col]=digit
                            if self.solve_sudoku():
                                return True
                            self.board[row][col]="." #backtrack
                        return False #no valid digit found
        return True #puzzle solved
    
    def is_valid_placement(self,row:int,col:int,digit:str)->bool:
        #check row and col
        for i in range(self.grid_size):
            if self.board[row][i]==digit or self.board[i][col]==digit:
                return False 
            
        #check subgrid
        subgrid_row_start=(row//3)
        subgrid_col_start=(col//3)
        for i in range(3):
            for j in range(3):
                if self.board[subgrid_row_start+i][subgrid_col_start+j]==digit:
                    return False
        return True 
    

if __name__ == "__main__":
    sudoku_board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print("Before solving:")
    for row in sudoku_board:
        print(" ".join(row))

    solver = SudokuSolver(sudoku_board)
    solver.solve()

    print("\nAfter solving:")
    for row in sudoku_board:
        print(' '.join(row))
