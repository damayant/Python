from collections import Counter 

class Solution:
    def shortestSubStrings(self,arr:list[str])->list[str]:
        # global_counts: maps each substring to the number of original strings it appears in.
        # unique_subs_per_word: stores the set of unique substrings for each word to avoid re-calculation.
        global_counts = Counter()
        unique_subs_per_word = []

        #phase 1: precalculate the counts and store substrings
        for word in arr:
            word_length = len(word)
            current_word_subs= set()

            #generate all possible substrings from the current word
            for start in range(word_length):
                for end in range(start+1,end+1):
                    current_word_subs.add(word[start:end])
            
            unique_subs_per_word.append(current_word_subs)

            #update global frequency map
            for sub in current_word_subs:
                global_counts[sub]+=1
        

        results = [] 

        #phase 2: identify shortest uniq substring for each word
        for i in range(len(arr)):
            # Retrieve the substrings we already generated for this specific word
            candidates = unique_subs_per_word[i]
            # Sort candidates: Primary key = Length (ascending), Secondary key = Alphabetical
            candidates.sort(key=lambda x:(len(x),x))
        
            found_match = False 

            for sub in candidates:
                # If the count is exactly 1, it means this substring 
                # appears ONLY in the current word.
                if global_counts[sub] == 1:
                    results.append(sub)
                    found_match = True
                    break 
                if not found_match:
                    results.append("")
        
        return results
