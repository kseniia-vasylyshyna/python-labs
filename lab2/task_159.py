number = int(input())

one_number = number // 10
two_number = number % 10

if one_number > two_number:
    print("1")
elif one_number < two_number:
    print("2")
else:
    print("=")
