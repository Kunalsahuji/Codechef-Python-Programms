# max element in the array:
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter values: ").split()))
max_element = arr[0]
for i in range(1, n):
    if arr[i] > max_element:
        max_element = arr[i]
print(f"Maximum element:{max_element}")

# with function:
def find_max(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element


arr = list(map(int, input("Enter values: ").split()))
max_element = find_max(arr)
print(f"Maximum element: {max_element}")

# with max function
def find_max(arr):
    return max(arr)


arr = list(map(int, input("Enter values: ").split()))
max_element = find_max(arr)
print(f"Maximum element: {max_element}")

# with built-in function
arr = list(map(int, input("Enter values: ").split()))
max_element = max(arr)
print(f"Maximum element: {max_element}")
