s = input()
a = s.split()
numbers = list(map(int, a))
result = numbers[::2]
print(*result)
