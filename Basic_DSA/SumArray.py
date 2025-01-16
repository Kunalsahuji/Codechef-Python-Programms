# sum of element in the array:

# A-1
"""
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Number of elements: ").split()))
sum = 0
for i in range(n):
    sum += arr[i]
print(f"Sum of element in the array: {sum}")
"""

# A-2
"""
n = int(input("Enter the number : "))
arr = list(map(int, input("Enter values: ").split()))
sum = 0
for i in arr:
    sum += i
print(f"Sum of array elements : {sum}")
"""

# A-3
"""
n = int(input("Enter the number : "))
arr = list(map(int, input("Enter values: ").split()))
print(f"sum = {sum(arr)}")
"""

# A-4
"""
def sum_array(arr):
    sums = 0
    for num in arr:
        sums += num
    return sums
# Example usage:
print(sum_array([1, 2, 3, 4, 5]))  # Output: 15

# time complexity: O(n), where n is the number of elements in the array. This is because we iterate through each element in the array once to calculate the sum.
"""
