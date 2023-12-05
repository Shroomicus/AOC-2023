input = open('input2.txt', 'r')
lines = input.readlines()
seedRanges = [int(x) for x in lines[0][7:].split()]
seeds = []
for i in range(len(seedRanges)//2):
    seeds.append((seedRanges[i*2], seedRanges[i*2] + seedRanges[i*2+1]))

lines = lines[2:]

maps = [[], [], [], [], [], [], []]

currMap = -1
for line in lines:
    line = line.replace('\n', '')
    if(line.endswith(":")):
        currMap +=1
        continue
    
    if(line == ""):
        continue

    maps[currMap].append([int(x) for x in line.split()])


def getIntersection(s1, e1, s2, e2):
    sec = (max(s1, s2), min(e1, e2))
    if(sec[1] - sec[0] >= 0):
        return sec
    return None

def getOther(startFull, endFull, spans):
    other = [(startFull, endFull)]
    for span in spans:
        newSpans = []
        for i in range(len(other)):
            oth = other.pop()
            int = getIntersection(span[0], span[1], oth[0], oth[1])
            if(int):
                if(oth[0] != int[0]):
                    newSpans.append((oth[0], int[0]-1))
                if(oth[1] != int[1]):
                   newSpans.append((int[1]+1, oth[1]))
        for i in newSpans:
            other.append(i)
    return other

print(seeds)

for map in maps:
    newSeeds = []
    for seed in seeds:
        ranges = []
        originalRanges = []
        for moves in map:
            int = getIntersection(seed[0], seed[1], moves[1], moves[1]+moves[2])
            if(int):
                ranges.append((int[0] - moves[1] + moves[0], int[1] - moves[1] + moves[0]))
                originalRanges.append((int[0], int[1]))

        other = getOther(seed[0], seed[1], originalRanges)

        for i in other:
            newSeeds.append(i)
        
        for i in ranges:
            newSeeds.append(i)

    seeds = newSeeds
    
low = seeds[0][0]
for seed in seeds:
    if(seed[0] < low):
        low = seed[0]
print(low)