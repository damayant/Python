from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Where we write the result
        f_ptr = 0  # Where we start reading a group
        count = len(chars)

        while f_ptr < count:
            char = chars[f_ptr]
            s_ptr = f_ptr
            
            # Find the end of the group of identical characters
            while s_ptr < count and chars[s_ptr] == char:
                s_ptr += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if it's greater than 1
            length = s_ptr - f_ptr
            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1
            
            # Move f_ptr to the next group
            f_ptr = s_ptr

        return write