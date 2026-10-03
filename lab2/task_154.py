a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c + 1 <= a and d + 1 <= b:  
    print("Yes")
elif d + 1 <= a and c + 1 <= b:
    print("Yes")
else:
    print("No")
