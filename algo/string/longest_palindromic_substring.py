class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd_pal = expand_around_center(i, i)
            # Even length palindrome
            even_pal = expand_around_center(i, i + 1)
            # Update result if longer palindrome is found
            longer_pal = odd_pal if len(odd_pal) > len(even_pal) else even_pal
            if len(longer_pal) > len(result):
                result = longer_pal
        
        return result