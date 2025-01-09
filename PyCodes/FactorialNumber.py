# Find the Factorial Number:
n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i

print(f"The factorial of {n} is {fact}")

# with function:
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
"""
