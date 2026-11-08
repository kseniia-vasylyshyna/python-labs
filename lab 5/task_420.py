s = input()
line = s.split()
numbers = list(map(int, line))

result = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        result.append(numbers[i])
        
print(*result)
