from math import ceil

for _ in range(int(input("Enter number: "))):
    n, x = map(int, input("Enter numbers: ").split())
    slices = n * x
    pizza = ceil(slice)/4
    print(pizza)
