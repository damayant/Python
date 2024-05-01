import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        ransom_note_set = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] in ransom_note_set:
                ransom_note_set[ransomNote[i]] += 1
            else:
                ransom_note_set[ransomNote[i]] = 1
        for i in range(len(magazine)):
            if magazine[i] in ransom_note_set :
                ransom_note_set[magazine[i]] -= 1
        # Iterate over values
        for value in ransom_note_set.values():
            if value > 0:
                return False
        
        return True

        
        
    def fasterSolution(self, ransomNote: str, magazine: str) -> bool :
    
    # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
        letters = collections.Counter(magazine)
    
    # For each character, c, in the ransom note:
        for c in ransomNote:
        # If there are none of c left, return False.
            if letters[c] <= 0:
                return False
        # Remove one of c from the Counter.
            letters[c] -= 1
    # If we got this far, we can successfully build the note.
        return True