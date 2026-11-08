from math import prod
s = input()
line = s.split()
numbers = list(map(int, line))

result = prod(numbers)
print(result)
