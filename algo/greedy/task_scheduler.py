from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], cooldown: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-freq for freq in task_counts.values()]
        heapq.heapify(max_heap)  # Max-heap using negative frequencies

        cooldown_queue = deque()  # Holds [remaining_count, available_time]
        current_time = 0

        while max_heap or cooldown_queue:
            current_time += 1

            # Step 1: Execute the most frequent available task
            if max_heap:
                remaining_count = 1 + heapq.heappop(max_heap)  # Increment because heap stores negative
                if remaining_count != 0:
                    # Task needs more runs; push it to cooldown
                    available_time = current_time + cooldown
                    cooldown_queue.append([remaining_count, available_time])

            # Step 2: Check if any task has completed its cooldown
            if cooldown_queue and cooldown_queue[0][1] == current_time:
                task_ready = cooldown_queue.popleft()
                heapq.heappush(max_heap, task_ready[0])  # Re-add to heap

        return current_time

# Example usage:
tasks = ["A", "A", "A", "B", "B", "B"]
cooldown = 2
solution = Solution()
print(solution.leastInterval(tasks, cooldown))  # Output: 8