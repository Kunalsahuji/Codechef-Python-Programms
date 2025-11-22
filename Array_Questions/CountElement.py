# input : [1,2,3,1,2,3,4,4,5]
# output: {'1': 2, '2': 2, '3': 2, '4': 2, '5': 1}

"""
def count_elements(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict


# Example usage:
input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = count_elements(input_list)
print("Count of each element:", result)
"""


"""
def count_elements(arr):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict


# Example usage:
input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = count_elements(input_list)
print("Count of each element:", result)
"""

# another approach by hashMap
arr = [1, 2, 3, 1, 2, 3, 4, 4, 5]
hashMap = map(lambda x: (x, arr.count(x)), set(arr))
result = dict(hashMap)
print("Count of each element using hashmap approach:", result)