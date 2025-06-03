import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        char_freq = self._get_char_frequency(s)
        
        # Step 2: Check if reorganization is possible
        if not self._can_reorganize(char_freq, len(s)):
            return ""
        
        # Step 3: Build a max heap from frequency map
        max_heap = self._build_max_heap(char_freq)
        
        # Step 4: Build the reorganized string using greedy strategy
        return self._build_reorganized_string(max_heap)

    def _get_char_frequency(self, s: str) -> dict:
        """
        Returns a dictionary of character frequencies.
        """
        return Counter(s)

    def _can_reorganize(self, freq_map: dict, string_length: int) -> bool:
        """
        Check if it's possible to reorganize the string.
        """
        max_allowed = (string_length + 1) // 2
        return max(freq_map.values()) <= max_allowed

    def _build_max_heap(self, freq_map: dict) -> list:
        """
        Builds a max heap (simulated using negative frequencies).
        """
        return [(-freq, char) for char, freq in freq_map.items()]
    
    def _build_reorganized_string(self, max_heap: list) -> str:
        """
        Constructs the reorganized string from the heap ensuring
        no two adjacent characters are the same.
        """
        heapq.heapify(max_heap)
        result = []

        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            # Re-add the previous character if it still has remaining count
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            # Update prev to current (decrease freq because it's used once)
            prev_freq, prev_char = freq + 1, char

        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.reorganizeString("aabbcc"))  # Output: "abcabc" or similar valid arrangement