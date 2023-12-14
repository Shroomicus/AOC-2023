input = open('input.txt', 'r')
lines = input.readlines()

map = []

for row in range(len(lines)):
    map.append([])
    for col in range(len(lines[0].strip())):
        map[row].append(lines[row][col])

for row in map:
    print(row)

# row dir, col dir
dir = (-1, 0)
def tilt(dir, map):
    if(dir[0] == -1):
        curr = [0] * len(map[0])
        for row in range(len(map)):
            for col in range(len(map[0])):
                if(map[row][col] == '#'):
                    curr[col] = row + 1
                if(map[row][col] == 'O'):
                    map[row][col] = '.'
                    map[curr[col]][col] = 'O'
                    curr[col] += 1

tilt(dir, map)

print()
for row in map:
    res = ""
    for col in row:
        res += col
    print(res)

total = 0
for row in range(len(map)):
    for col in range(len(map[0])):
        if(map[row][col] == 'O'):
            total += 10 - row
print(total)