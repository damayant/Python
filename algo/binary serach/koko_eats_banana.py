from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate total time required to finish all piles at a given speed
        def calculate_total_hours(eating_speed: int) -> int:
            total_hours = 0
            for bananas in piles:
                # Avoid using math.ceil by simulating it
                total_hours += (bananas + eating_speed - 1) // eating_speed
            return total_hours

        # Define binary search boundaries
        min_speed = 1
        max_speed = max(piles)
        optimal_speed = max_speed  # Start with the worst-case max

        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            required_hours = calculate_total_hours(mid_speed)

            if required_hours <= h:
                # Try to lower the speed
                optimal_speed = mid_speed
                max_speed = mid_speed - 1
            else:
                # Need to increase the speed
                min_speed = mid_speed + 1

        return optimal_speed


# Example usage:
piles = [3, 6, 7, 11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))  # Output: 4