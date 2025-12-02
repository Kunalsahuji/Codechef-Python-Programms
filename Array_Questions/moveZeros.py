# Move all zeros in an array to the end, while keeping the order of non-zero elements.


def move_zeros(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr


# Example usage:
arr = [0, 1, 0, 3, 12]
print(move_zeros(arr))  # Output: [1, 3, 12, 0, 0]
