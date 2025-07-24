from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = defaultdict(set)

        empty_cells = []

        # Step 1: Initialize sets and gather empty cell positions
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3, c // 3)].add(val)

        # Step 2: Backtracking function
        def backtrack(idx: int) -> bool:
            if idx == len(empty_cells):
                return True  # Solved

            r, c = empty_cells[idx]
            for digit in map(str, range(1, 10)):
                if digit in rows[r] or digit in cols[c] or digit in boxes[(r // 3, c // 3)]:
                    continue

                # Try placing digit
                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[(r // 3, c // 3)].add(digit)

                if backtrack(idx + 1):
                    return True

                # Backtrack
                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[(r // 3, c // 3)].remove(digit)

            return False

        backtrack(0)
