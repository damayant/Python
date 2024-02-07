class Solution:
    def intToRoman(num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0: break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)
    
    print(intToRoman(num=58))


    '''
    In Python, the `divmod()` function takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder when divided. 
    The syntax is `divmod(x, y)`, where `x` is the numerator and `y` is the denominator.

Here's an example:

```python
quotient, remainder = divmod(10, 3)
print("Quotient:", quotient)  # Output: 3
print("Remainder:", remainder)  # Output: 1
```

This is equivalent to the following:

```python
quotient = 10 // 3
remainder = 10 % 3
print("Quotient:", quotient)  # Output: 3
print("Remainder:", remainder)  # Output: 1
```

So, `divmod(x, y)` is a concise way to get both the quotient and remainder of the division operation in a single call. It returns a tuple where the first element is the quotient (`x // y`) and the second element is the remainder (`x % y`).

The main difference between `divmod()` and the `%` (modulo) operator is that `divmod()` returns both the quotient and remainder as a tuple, while `%` only returns the remainder. The `//` (floor division) operator, on the other hand, gives only the quotient.

Using `divmod()` can be more efficient than separate calls to `//` and `%` because it involves a single division operation, whereas using `//` and `%` separately would require two division operations.
'''