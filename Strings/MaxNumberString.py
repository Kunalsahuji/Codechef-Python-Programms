# Find Max number in the string: 

def max_number(s):
    sum = 0
    maxi = 0
    n = len(s)
    for i in range(n):
        if s[i].isdigit() == True:
            sum = sum * 10 + int(s[i])
        else:
            maxi = max(sum, maxi)
            sum = 0
    x = max(sum, maxi)
    return x


s = input("Enter string: ")
x = max_number(s)
print("Max Number is: ", x)
