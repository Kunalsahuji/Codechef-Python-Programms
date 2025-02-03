# min array in the array:
n = int(input("Enter the element you wish to select: "))
arr = list(map(int, input("Enter values:").split()))
min_val = arr[0]
for i in range(n):
    if arr[i] < min_val:
        min_val = arr[i]
print("Minimum value is:", min_val)

# with min fuction
"""
def min_array(arr):
    return min(arr)

n = int(input("Enter the element you wish to select: "))
arr = list(map(int, input("Enter values:").split()))
print("Minimum value is:", min_array(arr))
"""

# with function:
"""
def min_array(arr):
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val
n = int(input("Enter the element you wish to select: "))
arr = list(map(int, input("Enter values:").split()))
print("Minimum value is:", min_array(arr))
"""