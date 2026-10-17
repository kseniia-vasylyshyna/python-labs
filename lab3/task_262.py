t = int(input("Enter the time: "))
a = 1

for i in range (t):
    if i % 3 == 0:
        a *= 2
        
print(a)
