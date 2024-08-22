
class Solution:
    def reverse(self, x: int) -> int:
        # Define the minimum and maximum values for a 32-bit signed integer.
        # The range is from -2,147,483,648 to 2,147,483,647.
        MIN = -2147483648  # Minimum value for a signed 32-bit integer
        MAX = 2147483647   # Maximum value for a signed 32-bit integer

        res = 0  # This will store the reversed number

        while x:  # Continue until x becomes 0
            # Extract the last digit of x using modulus operation.
            # math.fmod is used because Python handles negative numbers differently.
            digit = int(math.fmod(x, 10))  # Example: -123 % 10 = -3 in Python

            # Update x by removing the last digit.
            # Integer division by 10 shifts the digits to the right.
            x = int(x / 10)  # Example: -123 // 10 = -12 in Python

            # **Overflow Check (Positive Side)**
            # Check if adding the new digit will cause the result to exceed the maximum value.
            # res > MAX // 10: If res is already larger than MAX // 10, adding any digit will cause an overflow.
            # res == MAX // 10 and digit >= MAX % 10: If res is exactly at MAX // 10, ensure the new digit doesn't push it beyond the maximum limit.
            if (res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10)):
                return 0  # Return 0 to indicate overflow, as the reverse integer cannot be represented in 32-bit.

            # **Overflow Check (Negative Side)**
            # Check if adding the new digit will cause the result to go below the minimum value.
            # res < MIN // 10: If res is already smaller than MIN // 10, adding any digit will cause an underflow.
            # res == MIN // 10 and digit <= MIN % 10: If res is exactly at MIN // 10, ensure the new digit doesn't push it beyond the minimum limit.
            if (res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10)):
                return 0  # Return 0 to indicate underflow, as the reverse integer cannot be represented in 32-bit.

            # Add the digit to the reversed number by shifting the current digits left and adding the new one.
            res = (res * 10) + digit

        return res  # Return the reversed integer
