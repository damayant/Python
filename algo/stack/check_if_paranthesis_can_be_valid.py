class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Entry point: verifies if the locked string can be turned into valid parentheses
        return self._is_valid_locked_string(s, locked)

    def _is_valid_locked_string(self, s: str, locked: str) -> bool:
        """
        Returns True if s can be transformed into a valid parentheses string.
        Must pass both left-to-right and right-to-left simulations.
        """
        if len(s) % 2 != 0:
            return False
        return self._check_validity(s, locked, is_reversed=False) and self._check_validity(s[::-1], locked[::-1], is_reversed=True)

    def _check_validity(self, s: str, locked: str, is_reversed: bool) -> bool:
        """
        Simulates balance while assuming unlocked characters can be changed.
        In normal direction: ensure open count is valid.
        In reverse: ensure close count is valid.
        """
        balance = 0
        free_slots = 0

        for idx in range(len(s)):
            char = s[idx]
            is_locked = locked[idx] == '1'

            if is_locked:
                if (not is_reversed and char == '(') or (is_reversed and char == ')'):
                    balance += 1
                else:
                    balance -= 1
            else:
                # Unlocked characters are flexible, we assume best-case
                balance += 1

            # If balance goes negative, even with flexible chars, it's invalid
            if balance < 0:
                return False

        return True




# Test cases
# def test():
#     sol = Solution()
#     assert sol.canBeValid("()()", "0000") == True
#     # assert sol.canBeValid("())", "110") == False
#     # assert sol.canBeValid("))", "11") == False
#     # assert sol.canBeValid("(((", "000") == False
#     # assert sol.canBeValid(")))))", "11111") == False
#     # assert sol.canBeValid("()()()", "000000") == True
#     assert sol.canBeValid("(()())", "111111") == True
#     # assert sol.canBeValid(")(", "01") == False

sol = Solution()
print(sol.canBeValid(")()(", "0101"))