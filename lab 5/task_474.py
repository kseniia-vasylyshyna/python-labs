n = int(input())

matrix = [['.' for _ in range(n)] for _ in range(n)]

mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid or i == j or i + j == n -1:
            matrix[i][j] = '*'

for row in matrix:
    print(''.join(row))