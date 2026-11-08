s = input()
a = s.split()
numbers = list(map(int, a))
count = len(numbers)

if count == 1:
    print(numbers[0])
else:
    result = []
    for i in range(count):
        result.append(numbers[i - 1] + numbers[(i + 1) % count])
    print(*result)

    