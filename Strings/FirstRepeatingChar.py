"""Find the first non-repeating character in a string.”
Example:
Input: "aabbcdeff"
Output: "c"
(→ because c is the first character that appears only once)
"""


def first_non_repeating_char(s: str) -> str:
    char_count = {}

    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return ""  # Return empty string if there is no non-repeating character


# Example usage
if __name__ == "__main__":
    input_str = "aabbcdeff"
    result = first_non_repeating_char(input_str)
    print(f"The first non-repeating character in '{input_str}' is: '{result}'")