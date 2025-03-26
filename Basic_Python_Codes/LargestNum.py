# Find the largest element in 3 numbers:
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if a >= b and a >= c:
    print(f"{a} is the largest number")
elif b >= a and b >= c:
    print(f" {b} is the largest number")
elif a == b == c:
    print(f" {a} is the smallest number")
else:
    print(f" {c} is the largest number")
