# Selection Sort:
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
def selection_sort(n, arr):
    for i in range(0, n, 1):
        for j in range(i + 1, n, 1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


n = int(input("Enter the number: "))
arr = list(map(int, input("Enter the elements: ").split()))
print(selection_sort(n, arr))
 # Example usage:
 # Enter the number: 5
 # Enter the elements: 5 2 8 1 3
 # [1, 2, 3, 5, 8]
 # The sorted array is: [1, 2, 3, 5, 8]
 # Time complexity: O(n^2)
 # Space complexity: O(1)
 # Stability: Yes
 # Adaptive: Yes
 # In-place: Yes
 # Not stable: Yes
 




