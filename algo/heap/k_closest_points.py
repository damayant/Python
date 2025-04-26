from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Step 1: Calculate distance of each point from origin and push into a heap
        min_heap = []
        for x, y in points:
            distance = x * x + y * y  # No need to take sqrt because we only compare distances
            heapq.heappush(min_heap, (distance, x, y))
        
        # Step 2: Extract k closest points
        k_closest_points = []
        for _ in range(k):
            distance, x, y = heapq.heappop(min_heap)
            k_closest_points.append([x, y])
        
        return k_closest_points

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        low, high = 0, max(distances)
        
        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2    
# Test cases
sol = Solution()
print(sol.kClosest2([[1,3],[-2,2],[5,8],[0,1]], 2))
# Expected output: [[-2, 2], [0, 1]]