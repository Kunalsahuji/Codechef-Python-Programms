# Bubble Sorting:


def bubble_sort(n, arr):
    for i in range(n):
        flag = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            break
    return arr


n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
print("Sorted array is: ", bubble_sort(n, arr))

"""
Example usage:
Enter the number of elements: 5
12 11 13 5 6
Sorted array is:  [5, 6, 11, 12, 13]

Time complexity: O(n^2)
Space complexity: O(1)
Stability: Yes
Adaptive: Yes
In-place: Yes
Not stable: Yes

Bubble Sort is not suitable for large data sets. It has a time complexity of O(n^2) and is not suitable for large datasets. It is more efficient for smaller data sets or for already sorted data. However, it has a worst-case scenario time complexity of O(n^2).

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
"""
