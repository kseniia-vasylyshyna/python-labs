a = int(input())
b = int(input())
x = int(input())

y = (a/b)**x+(a**(x+1))/(b**x)

# Виводимо модуль y
print(abs(y))
