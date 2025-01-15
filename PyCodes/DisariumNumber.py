#  Disarium Number: A Disarium Number is a number where the sum of its digits raised to the power of their position is equal to the number itself.
# The number counted from left to right starting from 1.
"""  
Example:
 135: 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
 518: 5^1 + 1^2 + 8^3 = 5 + 1 + 512 = 518
 1306: 1^1 + 3^2 + 0^3 + 6^4 = 1 + 9 + 0 + 1296 = 1306
 89, 135, 518 etc. are represented as disarium numbers.
 """
n = int(input("Enter the number: "))
temp = n
count = 0
while n > 0:
    n //= 10
    count += 1
sum = 0
n = temp
while n > 0:
    digit = n % 10
    sum += digit**count
    n //= 10
    count -= 1

if sum == temp:
    print(f"{temp} is a Disarium Number.")
else:
    print(f"{temp} is not a Disarium Number.")

    # with function


def is_disarium_number(n):
    temp = n
    count = 0
    while n > 0:
        n //= 10
        count += 1
    sum = 0
    n = temp
    while n > 0:
        digit = n % 10
        sum += digit**count
        n //= 10
        count -= 1
    return sum == temp


number = int(input("Enter the number: "))
result = is_disarium_number(number)
if result:
    print(f"{number} is a Disarium Number.")
else:
    print(f"{number} is not a Disarium Number.")
