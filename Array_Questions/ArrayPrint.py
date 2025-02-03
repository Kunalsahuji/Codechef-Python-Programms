# Array :
# 1. Line by line:
n = int(input("Enter number: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter value for index {i} : ")))
for i in range(n):
    print(f"Value at index {i} : {arr[i]}")

# 2. Using list comprehension:

n = int(input("Enter number: "))
arr = [int(input(f"Enter value for index {i} : ")) for i in range(n)]
for i in range(n):
    print(f"Value at index {i} : {arr[i]}")

# 3. Using built-in function:

n = int(input("Enter number: "))
arr = list(map(int, input("Enter values: ").split()))
for i in range(n):
    print(f"{arr[i]}", end=" ")
