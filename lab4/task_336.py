password = input("Please enter your password: ")
result = ''

for el in password:
    number = int(el)
    if number > 5:
        code = number // 2
        if code % 2 == 1:
            result += str(code)

print(f"Your code:{result}")

