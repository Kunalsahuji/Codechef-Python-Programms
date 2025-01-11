# Armstrong Number: An Armstrong Number is eqaul to the sum of its digits, each raised to the power of the number of digits in the number. Ex: 153, 370, 371, 407, 1634
n = int(input("Enter the number: "))
count = 0
temp = n
while n > 0:
    count += 1
    n //= 10

n = temp
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit**count
    n //= 10

if sum_of_digits == temp:
    print(f"{temp} is an Armstrong Number")
else:
    print(f"{temp} is not an Armstrong Number")

# with function:


"""
def is_armstrong_number(n):
    count = 0
    temp = n
    while n > 0:
        count += 1
        n //= 10
    n = temp
    sum_of_digits = 0
    while n > 0:
        digit = n % 10
        sum_of_digits += digit**count
        n //= 10
    return sum_of_digits == temp


# Test the function

number = int(input("Enter a number: "))
result = is_armstrong_number(number)
if result:
    print(f"{number} is an Armstrong Number")
else:
    print(f"{number} is not an Armstrong Number")
"""
