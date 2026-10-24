x = 0
y = 0

while True:
    line = input()
    if line == "Treasure!":
        break

    parts = line.split()
    direction = parts[0]
    steps = int(parts[1])

    if direction == "North":
        y += steps
    elif direction == "South":
        y -= steps
    elif direction == "East":
        x += steps

print(x, y)
