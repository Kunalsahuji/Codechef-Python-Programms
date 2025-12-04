# Given an array, find the majority element — the element that appears more than n/2 times.”

"""Example:
Input:
[2, 2, 1, 1, 1, 2, 2]
Output:
2
(because 2 appears 4 times, which is more than 7/2 = 3.5)
"""


def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# Example usage:
if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    print("Majority element is:", majority_element(arr))  # Output: 2
# Boyer-Moore Voting Algorithm Implementation