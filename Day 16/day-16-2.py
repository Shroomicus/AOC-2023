from collections import defaultdict

input = open('input2.txt', 'r')
lines = input.readlines()

shifts = {
    '|': {
        (0, 1) : [(1, 0), (-1, 0)],
        (0, -1) : [(1, 0), (-1, 0)],
    },
    '-': {
        (1, 0) : [(0, 1), (0, -1)],
        (-1, 0) : [(0, 1), (0, -1)],
    },
    '/': {
        (1, 0) : [(0, -1)],
        (-1, 0) : [(0, 1)],
        (0, 1) : [(-1, 0)],
        (0, -1) : [(1, 0)],
    },
    '\\': {
        (1, 0) : [(0, 1)],
        (-1, 0) : [(0, -1)],
        (0, 1) : [(1, 0)],
        (0, -1) : [(-1, 0)],
    }
}

map = []

for line in lines:
    line = line.replace('\n', '')
    map.append(list(line))

for line in map:
    res = ""
    for char in line:
        res += char
    print(res)

def getEnergy(startingBeam):
    energyMap = []
    for line in map:
        energyMap.append([])
        for char in line:
            energyMap[-1].append('.')
    seen = defaultdict(set)
    beams = [startingBeam]
    while(len(beams) > 0):
        beam = beams.pop(0)
        pos = [beam[0][0], beam[0][1]]
        # print()

        while((0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0])) and (map[pos[0]][pos[1]] is '.' or beam[1] not in shifts[map[pos[0]][pos[1]]])):
            if(beam[1] in seen[tuple(pos)]):
                break
            seen[tuple(pos)].add(beam[1])
            energyMap[pos[0]][pos[1]] = '#'
            pos[0] += beam[1][0]
            pos[1] += beam[1][1]

        if(beam[1] in seen[tuple(pos)]):
            continue
        
        if(not (0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0]))):
            continue

        if(beam[1] not in shifts[map[pos[0]][pos[1]]]):
            continue

        energyMap[pos[0]][pos[1]] = '#'
        seen[tuple(pos)].add(beam[1])
        for dir in shifts[map[pos[0]][pos[1]]][beam[1]]:
            beams.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
    total = 0

    # print()
    # for line in range(len(map)):
    #     res = ""
    #     for char in range(len(map[line])):
    #         if(energyMap[line][char] == '#' and map[line][char] == '.'):
    #             res += '#'
    #             continue
    #         res += map[line][char]
    #     print(res)


    for line in energyMap:
        res = ""
        for char in line:
            res += char
            if(char == '#'):
                total += 1
        # print(res)
    return total

max = 0
maxConfig = None
for i in range(len(map)):
    energy = getEnergy(((i, 0), (0, 1)))
    if(max < energy):
        max = energy
        maxConfig = ((i, 0), (0, 1))
    energy = getEnergy(((len(map) - 1 - i, 0), (0, -1)))
    if(max < energy):
        max = energy
        maxConfig = ((len(map) - 1 - i, 0), (0, -1))

for i in range(len(map[0])):
    energy = getEnergy(((0, i), (1, 0)))
    if(max < energy):
        max = energy
        maxConfig = ((0, i), (1, 0))
    energy = getEnergy(((0, len(map[0]) - 1 - i), (-1, 0)))
    if(max < energy):
        max = energy
        maxConfig = ((0, len(map[0]) - 1 - i), (-1, 0))
print(max)
print(maxConfig)