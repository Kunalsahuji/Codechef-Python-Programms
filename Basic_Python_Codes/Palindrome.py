# Check wheater number is palindrome or not
n = int(input("Enter the number: "))
sum = 0
temp = n
while n > 0:
    sum = (sum * 10) + (n % 10)
    n //= 10
if sum == temp:
    print(f"{temp} is a palindrome number.")
else:
    print(f"{temp} is not a palindrome number.")
