# Strong Number: A number is said to be a Strong Number if the sum of factorial of its digits is uequal to the number itself.
# Ex. 145,40585,1

from math import factorial

n = int(input("Enter a number: "))
sum = 0
temp = n
while n > 0:
    rem = n % 10
    sum += factorial(rem)
    n //= 10
if temp == sum:
    print(f"{temp} is a Strong Number")
else:
    print(f"{temp} is not a Strong Number")

"""
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def is_strong_number(n):
    sum_of_digits = 0
    temp = n
    while n > 0:
        digit = n % 10
        sum_of_digits += factorial(digit)
        n //= 10
    return sum_of_digits == temp


n = int(input("Enter a number: "))

if is_strong_number(n):
    print(f"{n} is a Strong Number")
else:
    print(f"{n} is not a Strong Number")
"""
