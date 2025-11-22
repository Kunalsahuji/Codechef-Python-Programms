# Remove duplicate numbers from a list and return a list of unique numbers
# input like : [1,2,2,3,4,4,5]
# output should be : [1,2,3,4,5]
"""
def unique_numbers(arr):
    unique_set = set()
    for num in arr:
        if num not in unique_set:
            unique_set.add(num)
    return list(unique_set)


# Example usage:
input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = unique_numbers(input_list)
print("List of unique numbers:", result)
"""


def unique_numbers(arr):
    unique_list = []
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


# Example usage:
input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = unique_numbers(input_list)
print("List of unique numbers:", result)
