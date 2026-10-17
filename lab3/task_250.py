total_sym = 0
total_count = 0
number = int(input("Enter the number: "))

while number != 0:
    total_sym += number
    total_count += 1
    number = int(input("Enter the number: "))

average = total_sym/total_count
print(average)
