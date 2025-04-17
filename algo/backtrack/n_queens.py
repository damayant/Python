from typing import List


class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     cols=set() 
    #     positiveDiagonal=set() #(r+c)
    #     negativeDiagonal=set() #(r-c)

    #     result=[]
    #     board=[['.']*n for i in range(n)]

    #     def backtrack(r):
    #         if r==n:
    #             copy=[''.join(row)for row in board]
    #             result.append(copy)
    #             return
    #         for c in range(n):
    #             if c in cols or (r+c) in positiveDiagonal or (r-c) in negativeDiagonal:
    #                 continue
            
    #             cols.add(c)
    #             positiveDiagonal.add(r+c) 
    #             negativeDiagonal.add(r-c)
    #             board[r][c]='Q'

    #             backtrack(r+1)

    #             cols.remove(c)
    #             positiveDiagonal.remove(r+c) 
    #             negativeDiagonal.remove(r-c)
    #             board[r][c]='.'

    #     backtrack(0)   
    #     return result

    from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(row: int, col: int) -> bool:
            """Check if placing a queen at (row, col) is safe."""
            return (
                col not in columns and
                (row + col) not in diagonals_pos and
                (row - col) not in diagonals_neg
            )

        def placeQueen(row: int, col: int):
            """Place a queen and update tracking sets."""
            board[row][col] = 'Q'
            columns.add(col)
            diagonals_pos.add(row + col)
            diagonals_neg.add(row - col)

        def removeQueen(row: int, col: int):
            """Remove a queen and revert tracking sets."""
            board[row][col] = '.'
            columns.remove(col)
            diagonals_pos.remove(row + col)
            diagonals_neg.remove(row - col)

        def buildBoard() -> List[str]:
            """Convert board to a list of strings for the final result."""
            return [''.join(row) for row in board]

        def backtrack(row: int):
            """Try placing queens row by row using backtracking."""
            if row == n:
                solutions.append(buildBoard())
                return

            for col in range(n):
                if isSafe(row, col):
                    placeQueen(row, col)
                    backtrack(row + 1)
                    removeQueen(row, col)

        # Sets to track threats
        columns = set()
        diagonals_pos = set()  # row + col
        diagonals_neg = set()  # row - col

        # Board and result
        board = [['.'] * n for _ in range(n)]
        solutions = []

        backtrack(0)
        return solutions

# Example usage
if __name__ == "__main__":
    n = 4
    solution = Solution()
    result = solution.solveNQueens(n)
    for board in result:
        for row in board:
            print(row)
        print()
# Output:
# [
# 	[".Q..",  # Solution 1
# 	 "..Q.",
# 	 ".Q..",
# 	 "...Q"],
# 	["..Q.",  # Solution 2
# 	 ".Q..",
# 	 "...Q",
# 	 "..Q."]
# ]
