input = open('input2.txt', 'r')
lines = input.readlines()

map = []

for row in range(len(lines)):
    map.append([])
    for col in range(len(lines[0].strip())):
        map[row].append(lines[row][col])

for row in map:
    print(row)


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
    if(dir[0] == 1):
        curr = [len(map)-1] * len(map[0])
        for row in range(len(map)-1, -1, -1):
            for col in range(len(map[0])):
                if(map[row][col] == '#'):
                    curr[col] = row-1
                if(map[row][col] == 'O'):
                    map[row][col] = '.'
                    map[curr[col]][col] = 'O'
                    curr[col] -= 1
    if(dir[1] == -1):
        curr = [0] * len(map)
        for col in range(len(map[0])):
            for row in range(len(map)):
                if(map[row][col] == '#'):
                    curr[row] = col + 1
                if(map[row][col] == 'O'):
                    map[row][col] = '.'
                    map[row][curr[row]] = 'O'
                    curr[row] += 1
    if(dir[1] == 1):
        curr = [len(map[0])-1] * len(map)
        for col in range(len(map[0])-1, -1, -1):
            for row in range(len(map)):
                if(map[row][col] == '#'):
                    curr[row] = col-1
                if(map[row][col] == 'O'):
                    map[row][col] = '.'
                    map[row][curr[row]] = 'O'
                    curr[row] -= 1

def spin():
    tilt((-1, 0), map)
    tilt((0, -1), map)
    tilt((1, 0), map)
    tilt((0, 1), map)


seen = {}

count = 0
keepGoing = False
loopCount = 0
while(True):
    spin()
    count+=1
    if(not keepGoing and "".join(["".join(x) for x in map]) in seen):
        print(count)
        val = seen["".join(["".join(x) for x in map])]
        print(val)
        keepGoing = True
        print()
        count = (1000000000 // (count - val)) * (count - val) + val - (val // (count - val) + 1) * (count - val)
        print(count)


    seen["".join(["".join(x) for x in map])] = count
    # print(count)
    if(count == 1000000000):
        break

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
            total += len(map) - row
print(total)