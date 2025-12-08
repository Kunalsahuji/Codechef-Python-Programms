# “Given an array of integers, return true if the array contains any duplicates. Otherwise return false.”
"""
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# Example usage:
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
print(contains_duplicate([1, 2, 3, 4]))  # Output: False
"""

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# Example usage:
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
print(contains_duplicate([1, 2, 3, 4]))  # Output: False
