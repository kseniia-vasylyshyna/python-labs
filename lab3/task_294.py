a = int(input("Enter the four-digit number: "))
b = int(input("Enter the four-digit number: "))

for number in range (a, b + 1):
    thousands = number // 1000
    hundreds = number // 100 % 10
    tens = number // 10 % 10
    units = number % 10
    if thousands == units and hundreds == tens:
        print(number)
