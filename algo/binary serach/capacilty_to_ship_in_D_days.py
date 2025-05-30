from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function: Calculate how many days needed with given ship capacity
        def calculate_required_days(ship_capacity: int) -> int:
            current_load = 0
            day_count = 1  # Start with day 1

            for weight in weights:
                # If adding this package exceeds capacity, ship it the next day
                if current_load + weight > ship_capacity:
                    day_count += 1
                    current_load = 0
                current_load += weight

            return day_count

        # Define binary search bounds for capacity
        min_capacity = max(weights)  # At least the heaviest package must fit
        max_capacity = sum(weights)  # At most carry everything in 1 day
        optimal_capacity = max_capacity  # Store best so far

        while min_capacity <= max_capacity:
            trial_capacity = (min_capacity + max_capacity) // 2
            required_days = calculate_required_days(trial_capacity)

            if required_days <= days:
                # This capacity works; try a smaller one
                optimal_capacity = trial_capacity
                max_capacity = trial_capacity - 1
            else:
                # Too small capacity; increase it
                min_capacity = trial_capacity + 1

        return optimal_capacity

# Example usage:
weights = [1, 2, 3, 4, 5]
days = 2
solution = Solution()
print(solution.shipWithinDays(weights, days))  # Output: 9