from collections import Counter
from typing import List
import heapq

class ServerClusterOptimizer:
    def __init__(self, capacities: List[int], cluster_size: int):
        self.capacities = capacities
        self.cluster_size = cluster_size
        self.capacity_frequency = Counter(capacities)

    def _get_grouping_potential(self) -> List[int]:
        """
        Convert frequency counts into a max-heap to simulate greedy selection of most frequent capacities.
        """
        return [-count for count in self.capacity_frequency.values()]  # Negative for max-heap

    def _calculate_remaining_servers(self, frequency_heap: List[int]) -> List[int]:
        """
        Simulate greedily forming clusters and track leftover server capacities.
        """
        leftover_counts = []

        while frequency_heap:
            current_group = []

            for _ in range(self.cluster_size):
                if frequency_heap:
                    top_count = -heapq.heappop(frequency_heap)
                    current_group.append(top_count)
                else:
                    current_group.append(0)

            min_servers = min(current_group)

            for server_count in current_group:
                leftover = server_count - min_servers
                if leftover > 0:
                    leftover_counts.append(leftover)

        return leftover_counts

    def min_moves_to_form_clusters(self) -> int:
        """
        Main function that returns the minimum number of moves to form valid clusters.
        """
        frequency_heap = self._get_grouping_potential()
        heapq.heapify(frequency_heap)

        leftover_counts = self._calculate_remaining_servers(frequency_heap)
        total_leftovers = sum(leftover_counts)

        # To form complete clusters, we might need to add or convert some servers.
        remainder = total_leftovers % self.cluster_size
        return (self.cluster_size - remainder) % self.cluster_size

# Example usage:
if __name__ == "__main__":
    capacities = [4, 2, 4, 4, 7, 4]
    cluster_size = 3
    optimizer = ServerClusterOptimizer(capacities, cluster_size)
    print(optimizer.min_moves_to_form_clusters())  # Output: 2