class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 
        candidates.sort()  # Add this line to sort the array

        def backtrack(remaining:int, current_combination:List[int], current_index:int):
            if remaining == 0:
                result.append(current_combination[:])
                return

            if remaining < 0:
                return 

            for index in range(current_index, len(candidates)):
                # Skip duplicates at the same level
                if index > current_index and candidates[index] == candidates[index-1]:
                    continue
                    
                current_candidate = candidates[index]
                current_combination.append(current_candidate)
                backtrack(remaining - current_candidate, current_combination, index + 1)
                current_combination.pop()

        backtrack(target, [], 0)
        return result