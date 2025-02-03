# Find out the second highest element in the array:


def second_highest_element(n, arr):
    highest = float("-inf")
    second_highest = float("-inf")
    for i in range(0, n, 1):
        if arr[i] > highest:
            second_highest = highest
            highest = arr[i]
        elif arr[i] > second_highest and arr[i] != highest:
            second_highest = arr[i]
    return second_highest


n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements: ").split()))
print("Second highest element in the array is: ", second_highest_element(n, arr))
