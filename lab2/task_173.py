n = int(input())
m = int(input())

percentage = (n / m) * 100

if percentage >= 90:
    print("Your grade is 12.")
elif percentage >= 70:
    print("Your grade is 8.")
elif percentage >= 50:
    print("Your grade is 5.")
else:
    print("Your grade is 2.")
