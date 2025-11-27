# Subarrya: (Subsequence)
#  Number picking problem

nums = [1, 2, 2, 3, 1, 2]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
maxLen = 0
for key in nums:
    number = int(key)
    option = freq[number] + freq.get(number + 1, 0)
    maxLen = max(maxLen, option)
print(maxLen)
