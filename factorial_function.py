# In mathematics, the factorial of a non-negative integer n, denoted by n!,
# is the product of all positive integers less than or equal to n.
# The factorial of n also equals the product of n with the next smaller factorial:
# For example, The value of 0! is 1, according to the convention for an empty product.

def factorial_function(n):
    if n < 0:
        return None # if the number is not positive we can not calculate factorial
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 8):
    print(n, factorial_function(n))

# Same function using recursion(function invoking itself):
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
print(n, factorial_function(5))
