# Spy Number : A number is said to be a spy number if the sum of its digits is equal to the product of its digit. Example : 22, 1241
n = int(input("Enter a number: "))
sum_digits = 0
product_digits = 1
temp = n
while n > 0:
    digits = n % 10
    sum_digits += digits
    product_digits *= digits
    n //= 10

if sum_digits == product_digits:
    print(f"{temp} is a Spy tempumber")
else:
    print(f"{temp} is not a Spy Number")

# with function:
"""
def is_spy_number(n):
    sum_digits = 0
    product_digits = 1
    while n > 0:
        digit = n % 10
        sum_digits += digit
        product_digits *= digit
        n //= 10
    return sum_digits == product_digits

n = int(input("Enter a number: "))

if is_spy_number(n):
    print(n, "is a spy number")
else:
    print(n, "is not a spy number")
"""
