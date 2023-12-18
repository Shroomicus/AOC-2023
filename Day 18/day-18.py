from tabnanny import check


input = open('input.txt', 'r')
lines = input.readlines()

instList = [x.strip() for x in lines]

moves = {
    "R" : (0, 1),
    "L" : (0, -1),
    "U" : (-1, 0),
    "D" : (1, 0)
}

map = [['#', '.']]
mapStart = [0, 0]

pos = [0, 0]

size = [1, 2]

for inst in instList:
    data = inst.split()
    move = moves[data[0]]
    for ind in range(int(data[1])):
        pos[0] += move[0]
        pos[1] += move[1]
        if(pos[0] < mapStart[0]):
            size[0] += 1
            mapStart[0] = pos[0]
            print(mapStart)
            map.insert(0, ['.'] * size[1])
        if(pos[0] - mapStart[0] >= size[0]):
            size[0] += 1
            map.append(['.'] * size[1])
        if(pos[1] < mapStart[1]):
            size[1] += 1
            mapStart[1] = pos[1]
            print(mapStart)
            for ind in range(size[0]):
                map[ind].insert(0, '.')
        if(pos[1] - mapStart[1] >= size[1]):
            size[1] += 1
            for ind in range(size[0]):
                map[ind].append('.')
        map[pos[0] - mapStart[0]][pos[1] - mapStart[1]] = '#'

print(pos)

checkRow = map[len(map)//2]
seenFirst = False
innerPos = [len(map)//2]
for i in range(len(map[0])):
    print(i)
    if(checkRow[i] == '#'):
        if(not seenFirst):
            seenFirst = True
            continue
    if(checkRow[i] == '.'):
        if(seenFirst):
            innerPos.append(i)
            break
print(innerPos)

queue = [innerPos]
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
while(len(queue) > 0):
    pos = queue.pop(0)
    if(not (0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[1]))):
        continue
    if(map[pos[0]][pos[1]] == '#'):
        continue
    map[pos[0]][pos[1]] = '#'
    for dir in dirs:
        queue.append((pos[0] + dir[0], pos[1] + dir[1]))

total = 0
for line in map:
    res = ""
    tempTotal = 0
    for char in line:
        if(char == '#'):
            tempTotal += 1
        res += char
    total += tempTotal
    print(res)
print(total)