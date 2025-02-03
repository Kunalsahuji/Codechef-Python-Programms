# Find out the second lowest element in the array:
def second_lowest_element(n, arr):
    lowest = float("inf")
    second_lowest = float("inf")
    for i in range(n):
        if arr[i] < lowest:
            second_lowest = lowest
            lowest = arr[i]
        elif arr[i] < second_lowest and arr[i] != lowest:
            second_lowest = arr[i]
    return second_lowest


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the values: ").split()))
second_lowest = second_lowest_element(n, arr)
print("Second lowest element is:", second_lowest)
