from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # MINIMAL LOGIC CHANGE: Use counts instead of 'x'/'t' markers for efficiency.
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        
        # `required` is the number of unique characters in t that we need to match.
        required = len(t_count)
        # `formed` tracks how many of those unique characters have been matched in the current window.
        formed = 0
        # `window_count` tracks the count of characters in the current window.
        window_count = defaultdict(int)
        
        result = ""
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            # If the current character's count in the window matches its count in t,
            # we have satisfied the requirement for this character.
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Try to contract the window from the left as much as possible.
            while formed == required and left <= right:
                # Update the result if this window is smaller.
                if result == "" or (right - left + 1) < len(result):
                    result = s[left:right+1]

                # Remove the leftmost character from the window.
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1

        return result