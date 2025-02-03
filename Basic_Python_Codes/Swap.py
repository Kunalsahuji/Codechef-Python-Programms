# Swap 2 numbers using 3rd variable: (A-1)
"""
a = int(input("Enter number: "))
b = int(input("Enter number: "))
temp = a
a = b
b = temp
print(f"a = {a} b = {b}")
"""

# swap 2 numbers without using 3rd variable: (A-2)
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
a = a + b
b = a - b
a = a - b
print(f"a = {a} b = {b}")
"""

# swap 2 numbers without using 3rd variable and arithmatic operatore: (A-3)
"""
a = int(input("Enter 1st number:"))
b = int(int(input("Enter 2nd number: ")))
a = a ^ b
b = a ^ b
a = a ^ b
print(f"a = {a} b = {b}")
"""

# swap 2 numbers without using 3rd variable and arithmatic operatore: (A-4)
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
a, b = b, a
print(f"a = {a} b = {b}")
"""

# swap 3 numbers without using any extra variables: (A-5)
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
a = a + b + c
b = a - b - c
c = a - b - c
a = a - b - c
print(f"a = {a} b = {b} c = {c}")
"""

# swap 3 numbers without using extra variable and arithmatic operatore: (A-6)
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
# a, b, c = map(int, input("Enter numbers: ").split())
a = a ^ b ^ c
b = a ^ b ^ c
c = a ^ b ^ c
a = a ^ b ^ c
print(f"a = {a} b = {b} c = {c}")
"""
