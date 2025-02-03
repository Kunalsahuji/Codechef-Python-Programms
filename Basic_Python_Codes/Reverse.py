# Reverse the order of the number

"""
n = int(input("Enter number: "))
reversed_num = 0
while n > 0:
    reversed_num = (reversed_num * 10) + (n % 10)
    n //= 10
print("Reversed number:", reversed_num)
"""

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n = n // 10
    return reversed_num

# Testing the function

number = 12345
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)

# This function reverses the order of the number by repeatedly dividing the number by 10 and taking the remainder. The reversed number is then constructed by multiplying the reversed_num by 10 and adding the remainder of the division. The loop continues until the number becomes 0.



