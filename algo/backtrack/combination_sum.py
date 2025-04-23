from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []

        def backtrack(remaining_sum: int, current_combination: List[int], current_index: int):
            # Base case: valid combination found
            if remaining_sum == 0:
                all_combinations.append(list(current_combination))
                return
            # Base case: invalid path
            if remaining_sum < 0:
                return

            for index in range(current_index, len(candidates)):
                current_candidate = candidates[index]

                # Choose
                current_combination.append(current_candidate)

                # Backtrack
                backtrack(remaining_sum - current_candidate, current_combination, index)

                # Unchoose (backtrack step)
                current_combination.pop()

        backtrack(target, [], 0)
        return all_combinations


# Example usage
if __name__ == "__main__":
    solution = Solution()
    candidates = [3, 4, 5]
    target = 8
    result = solution.combinationSum(candidates, target)
    print(result)  
