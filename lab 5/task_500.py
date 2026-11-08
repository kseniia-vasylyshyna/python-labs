line = input()
groups = line.split(',')
rows = [list(map(int, group.split())) for group in groups]

print(rows)
print(sorted(rows, key=lambda row: row[1]))
