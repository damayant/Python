from collections import deque
from typing import Collection, List



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        q = deque() # Queue to store rotten oranges coordinates
        fresh = 0  # Track fresh oranges
        count = 0  # Time tracker

        # Step 1: Add all rotten oranges to queue & count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Step 2: BFS function
        def bfs():
            nonlocal count, fresh  # Use count and fresh from outer scope
            while q and fresh > 0:
                count += 1  # Increment minutes at the start of each level
                for _ in range(len(q)):  # Process all oranges at the current level
                    row, col = q.popleft()
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == 1:
                            visit.add((new_row, new_col))
                            q.append((new_row, new_col))
                            grid[new_row][new_col] = 2  # Rot the fresh orange
                            fresh -= 1  # Reduce fresh count

        # Step 3: Start BFS
        bfs()

        # Step 4: Return result
        return count if fresh == 0 else -1  # If no fresh oranges left, return minutes; otherwise, return -1

