# To check Leap year 1992,2024,1543,1974....
n = int(input("Enter year: "))
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print(f"{n} is Leap Year")
else:
    print(f"{n} is not a Leap Year")
