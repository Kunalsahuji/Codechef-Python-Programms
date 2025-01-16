""" Array : Array is the collection of similar data type stored in continuous memory location.
 Array start from the 0 and end with n-1.
          0  1   2   3   4   5    6  7  8   9    :   Indexing
 arr = [ 10  20  30  40  50  60  70  80 90 100 ]
        100 104 108 112 116 120 124 128 132 136   : Base Address
   
arr       elem       base
index     ents       address    
 arr[0]  =  10        100
 arr[1]  =  20        104
 arr[2]  =  30        108
 arr[3]  =  40        112
 arr[4]  =  50        116
 arr[5]  =  60        120
 arr[6]  =  70        124
 arr[7]  =  80        128
 arr[8]  =  90        132
 arr[9]  =  100       136
 
 Advantages: 
 1. Accessing/Updation: WE can access/update any element of an array in constant time with O(1) time complexity by using formula :
 Required Address = Base Address + Index * Size
 Address of arr : arr[2] = 100 + 2 * 4
                  arr[2] = 108 => 30
                  
2. Array are simple and easy to implement.

Disadvantages:
1. Static Memory Location : Array has static memory location it means it size cannot be increased/decreased at runtime.
2.Insertion/Deletion : Insertion/Deletion are costly and time consuming operations in array because to insert any element in the array 
we need to move all the elements to make space for the new element. This is a costly operation. same to delete the element from the array 
we also need to move all the elements to fill the gap. This is a costly operation.
2. Fixed Memory Size : Array has fixed memory size. If we want to increase/decrease the size of an array, we need to create a new array and copy the elements from the old array to the new array.
3. Memory Fragmentation : Array elements may not be stored consecutively in memory leading to memory fragmentation.
4. Difficulty in Sharing: Arrays are not designed to be shared between multiple processes or threads.

Time Complexity:
1. Accessing/Updating: O(1)
2. Insertion/Deletion: O(n) because all the elements need to be shifted to make space for the new element.
3. Sorting: O(n log n) because sorting algorithm like Quick Sort, Merge Sort, or Heap Sort requires comparisons and swaps.

Space Complexity:
1. Constant Space : Array uses constant amount of memory regardless of the size of the array. It does not depend on the number of elements.
2. Dynamic Space : Array uses dynamic amount of memory depending on the number of elements. It can grow or shrink as per the requirement.

Limitations:
1. Fixed Size : Arrays have fixed size, which means we cannot add or remove elements dynamically. To add or remove elements, we need to create a new array and copy the elements from the old array to the new array. This is a costly operation.
2. Inefficient Insertion/Deletion : Insertion/Deletion of elements in the middle of an array requires shifting all the elements to make space for the new element. This can be costly operation.
3. Inefficient Sharing : Arrays are not designed to be shared between multiple processes or threads. If we want to share an array between multiple processes or threads, we need to use appropriate synchronization mechanisms. This can be costly operation.
4. Inefficient Sorting : Sorting an array requires comparing and swapping elements. This can be costly operation for large arrays.
5. Inefficient Access: Accessing an element in an array requires accessing the element at the specified index, hence it has a time complexity of O(1). However, accessing an element at a random index in an array can be costly operation.

In summary:
1. Memory Efficiency : Arrays have constant time complexity for accessing/updating elements, insertion/deletion, and sorting. This makes them efficient for storing and manipulating large amounts of data.
2. Flexibility : Arrays have flexibility to store any type of data and can be easily resized. This makes them suitable for various use cases.
3. Efficient Sharing : Arrays are designed to be shared between multiple processes or threads efficiently. This makes them suitable for scenarios where data needs to be accessed by multiple processes or threads simultaneously.
4. Slow Insertion/Deletion : Insertion/Deletion of elements in the middle of an array requires shifting all the elements to make space for the new element. This can be costly operation. In Python, list provides efficient methods for inserting/deleting elements in the middle of a list.
5. Slow Access : Accessing an element in an array requires accessing the element at the specified index, hence it has a time complexity of O(1). However, accessing an element at a random index in an array can be costly operation. In Python, list provides efficient methods for accessing elements at random indexes.


Note: In Python, array is implemented as dynamic array. Python list is a built-in data structure that allows dynamic size and can hold any type of data. It is implemented as a dynamic array under the hood.
Example:
 """
# different types of arrays methods for accessing/deletion/insert/remove/sort/reverse/update/
arr = [10, 20, 30, 40, 50]
print(arr)  # Output: [10, 20, 30, 40, 50]

arr[2] = 45
print(arr)  # Output: [10, 20, 45, 40, 50]

arr.append(60)
print(arr)  # Output: [10, 20, 45, 40, 50, 60]

arr.remove(45)
print(arr)  # Output: [10, 20, 40, 50, 60]

arr.pop(3)
print(arr)  # Output: [10, 20, 40, 60]

arr.insert(3, 45)
print(arr)  # Output: [10, 20, 40, 45, 60]

arr.sort()
print(arr)  # Output: [10, 20, 40, 45, 60]

arr.reverse()
print(arr)  # Output: [60, 45, 40, 20, 10]

print(arr[1:4])  # Output: [45, 40, 20]

print(arr[:4])  # Output: [60, 45, 40, 20]

print(arr[4:])  # Output: [10]

print(len(arr))  # Output: 5

print(arr.index(45))  # Output: 1

print(45 in arr)  # Output: True

arr.clear()

print(arr)  # Output: []

print(len(arr))  # Output: 0

arr = [10, 20, 30, 40, 50]

arr.copy()

print(arr)  # Output: [10, 20, 30, 40, 50]

arr[2:4] = [45, 55]

print(arr)  # Output: [10, 20, 45, 55, 50]

arr[2:4] = []

print(arr)  # Output: [10, 20, 50]
