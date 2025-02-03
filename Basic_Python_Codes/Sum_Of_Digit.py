# Problem-3 Sum of digits of a number
n = int(input("Enter number: "))
sum = 0
temp = n
while n != 0:
    rem = n % 10
    sum += rem
    n //= 10
print(f"sum of {temp} = {sum}")
