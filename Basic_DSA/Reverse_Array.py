# Reverse the array in O(n) time and O(1) space.


def reverse_array(n, arr):
    start = 0
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


# Example usage:
n = int(input("Enter the number of elements in the array: "))

arr = list(map(int, input("Enter the elements of the array: ").split()))

print("Original array:", arr)

reversed_arr = reverse_array(n, arr)

print("Reversed array:", reversed_arr)
