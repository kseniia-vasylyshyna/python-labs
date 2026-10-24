A = input()
B = input()

result = True

for letter in set(B):
    if B.count(letter) > A.count(letter):
        result = False
        break

if result:
    print("Yes")
else:
    print("No")
    
