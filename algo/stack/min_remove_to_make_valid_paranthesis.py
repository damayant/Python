class Solution:
    def minRemoveToMakeValid(self, input_string: str) -> str:
        # Entry point: cleans up invalid parentheses from the input string
        return self._clean_parentheses(input_string)

    def _clean_parentheses(self, input_string: str) -> str:
        """
        Removes invalid parentheses from the string.
        Step 1: Identify the indices of valid parentheses.
        Step 2: Construct a new valid string using only valid indices.
        """
        valid_indices = self._collect_valid_parenthesis_indices(input_string)
        return self._reconstruct_string(input_string, valid_indices)

    def _collect_valid_parenthesis_indices(self, input_string: str) -> set:
        """
        Traverses the string and collects indices of valid '(' and ')'.
        Uses a stack to match each '(' with a valid ')'.
        Returns a set of indices that should be kept.
        """
        unmatched_open_indices = []  # Stack to hold indices of unmatched '('
        valid_indices = set()        # Final set of indices to keep in result

        index = 0
        while index < len(input_string):
            current_char = input_string[index]

            if self._is_opening(current_char):
                unmatched_open_indices.append(index)
            elif self._is_closing(current_char):
                if unmatched_open_indices:
                    matching_open_index = unmatched_open_indices[-1]
                    matching_open_char = input_string[matching_open_index]
                    if self._is_match(matching_open_char, current_char):
                        valid_indices.add(unmatched_open_indices.pop())  # Valid '('
                        valid_indices.add(index)                         # Valid ')'

            index += 1

        return valid_indices

    def _reconstruct_string(self, original_string: str, valid_indices: set) -> str:
        """
        Rebuilds the result string using:
        - All non-parenthesis characters
        - Only those parentheses which are valid (i.e., their indices are in valid_indices)
        """
        final_chars = []
        index = 0

        while index < len(original_string):
            character = original_string[index]
            if not self._is_paren(character) or index in valid_indices:
                final_chars.append(character)
            index += 1

        return ''.join(final_chars)

    def _is_opening(self, character: str) -> bool:
        # Returns True if character is an opening parenthesis
        return character == '('

    def _is_closing(self, character: str) -> bool:
        # Returns True if character is a closing parenthesis
        return character == ')'

    def _is_match(self, opening: str, closing: str) -> bool:
        # Checks if the given pair of characters is a valid matching pair
        return opening == '(' and closing == ')'

    def _is_paren(self, character: str) -> bool:
        # Checks if the character is any kind of parenthesis
        return character in '()'


# Example usage
if __name__ == "__main__":
    expression1 = "a)b(c)d"
    expression2 = "))(("
    
    sol = Solution()
    print(sol.minRemoveToMakeValid(expression1))  # Output: "ab(c)d"
    print(sol.minRemoveToMakeValid(expression2))  # Output: ""
