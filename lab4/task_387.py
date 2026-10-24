line = input("Please enter your line: ")

result = ""
current = line[0]
count = 1

for el in line[1:]:
    if el == current:
        count += 1  
    else:
        result += current + str(count)
        current = el
        count = 1

result += current + str(count)
print(result)
