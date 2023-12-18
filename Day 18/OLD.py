from collections import defaultdict

input = open('input.txt', 'r')
lines = input.readlines()

instList = [x.strip() for x in lines]

moves = {
    "0" : (0, 1),
    "2" : (0, -1),
    "3" : (-1, 0),
    "1" : (1, 0)
}
moveChars = {
    "R" : (0, 1),
    "L" : (0, -1),
    "U" : (-1, 0),
    "D" : (1, 0)
}

processedMoves = []
for inst in instList:
    # data = inst.split()[2]
    # print(moves[data[-2]])
    # print(int(data[2:len(data)-2], 16))
    data = inst.split()
    move = moveChars[data[0]]
    mult = int(data[1])
    processedMoves.append((move, mult, data[0]))

minVals = [0, 0]
maxVals = [0, 0]
pos = [0, 0]
for mov in processedMoves:
    # print(move)
    move = mov[0]
    mult = mov[1]
    pos[0] += mult * move[0]
    pos[1] += mult * move[1]
    # print(pos)
    if(pos[0] < minVals[0]):
        minVals[0] = pos[0]
    if(pos[1] < minVals[1]):
        minVals[1] = pos[1]
    if(pos[0] > maxVals[0]):
        maxVals[0] = pos[0]
    if(pos[1] > maxVals[1]):
        maxVals[1] = pos[1]

map = defaultdict(list)
pos = [0, 0]
total = 0
last = [0, 0]
for mov in processedMoves:
    map[pos[0]].append(pos[1])
    move = mov[0]
    mult = mov[1]
    pos[0] += mult * move[0]
    pos[1] += mult * move[1]

total = 0
currInds = map[minVals[0]]
currInds.sort()
for i in range(len(currInds) // 2):
    total += currInds[i+1] - currInds[i] + 1

lastInds = []
for row in range(minVals[0]+1, maxVals[0]):
    print(total)
    lastInds = currInds.copy()
    for ind in map[row]:
        if ind in currInds:
            currInds.remove(ind)
        else:
            currInds.append(ind)
    currInds.sort()
    print(currInds)
    for i in range(len(currInds) // 2):
        val = (max(currInds[i+1], lastInds[i+1])  - min(currInds[i], lastInds[i]))
        total += val + 1
for i in range(len(currInds) // 2):
    total += currInds[i+1] - currInds[i] + 1

print(total)