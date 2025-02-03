# Rotate an array by k times:


def k_rotate_array(n, arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the number of times to rotate the array: "))
if k > n:
    k = k % n
arr = k_rotate_array(n, arr, 0, n - 1)
arr = k_rotate_array(n, arr, 0, k - 1)
arr = k_rotate_array(n, arr, k, n - 1)
print(f'Array after rotating {k} times:', arr)