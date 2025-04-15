# def fibonacci_recursive(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

# print(fibonacci_recursive(3))


# def fib_iterative(n):
#     if n <= 1:
#         return n
#     first, second = 0, 1
#     for _ in range(2, n + 1):
#         first, second = second, first + second

#     return second

# print(fib_iterative(5))  # Output: 5


def fibonacci_memoization(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

print(fibonacci_memoization(5))  # Output: 5