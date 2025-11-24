# Given an integer array nums, return the length of the longest subarray 
# where the difference between the maximum and minimum elements is at most 1.
def longest_subarray(nums):
    max_length = 0
    n = len(nums)

    for i in range(n):
        current_min = nums[i]
        current_max = nums[i]
        for j in range(i, n):
            current_min = min(current_min, nums[j])
            current_max = max(current_max, nums[j])
            if current_max - current_min <= 1:
                max_length = max(max_length, j - i + 1)
            else:
                break

    return max_length

# Example usage:
input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = longest_subarray(input_list)
print("Length of the longest subarray:", result)