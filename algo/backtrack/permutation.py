from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # 1. 'res' will store all the completed permutations.
        res = [] 
        
        # 2. 'used' tracks which *indices* of 'nums' are already in
        #    the current 'path'. This is an O(1) lookup.
        #    e.g., used[0] = True means nums[0] is in the path.
        used = [False] * len(nums)
        
        # 3. 'path' is the current permutation we are building.
        #    We pass it down through the recursion.
        def backtrack(path):
            
            # 4. BASE CASE: If the path is a full permutation (same length
            #    as nums), we've found a solution.
            if len(path) == len(nums):
                # We append a COPY of the path. If we just append 'path',
                # it will be empty by the end.
                res.append(path[:]) 
                return # Stop exploring this branch.

            # 5. RECURSIVE STEP: Try every number as the *next*
            #    number in the path.
            for i in range(len(nums)):
                
                # 6. CONSTRAINT: If we've already used the number at this
                #    index, skip it and try the next one.
                if used[i]:
                    continue
                
                # --- The "Choose, Explore, Un-choose" Sandwich ---
                
                # 7. CHOOSE: Mark the number at index 'i' as used
                #    and add it to our current path.
                used[i] = True
                path.append(nums[i])
                
                # 8. EXPLORE: Recursively call backtrack with the *new*
                #    state (the updated path and used array).
                backtrack(path)
                
                # 9. UN-CHOOSE (Backtrack): This is the magic.
                #    After the 'backtrack(path)' call above returns
                #    (meaning it has explored *all* possibilities
                #    starting with this path), we *undo* our choice.
                #    This lets the 'for' loop continue to the next 'i'.
                path.pop()        # Remove the last number added.
                used[i] = False   # Mark its index as available again.
                
                # --- End of Sandwich ---

        # 10. KICK IT OFF: Start the recursive process with an
        #     empty path.
        backtrack([])
        
        # 11. Return the final list of solutions.
        return res