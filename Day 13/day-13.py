input = open('input.txt', 'r')
lines = input.readlines()

maps = [[]]

current = 0
for line in lines:
    line = line.replace('\n', '')
    if(line == ''):
        current += 1
        maps.append([])
        continue
    maps[current].append(line)

total = 0
for map in maps:
    # for line in map:
    #     print(line)

    flipMap = [""]*len(map[0])
    
    for line in map:
        for ind in range(len(line)):
            flipMap[ind] += line[ind]
    # print()
    # for i in flipMap:
    #     print(i)

    horizInd = -1
    for ind in range(1,len(map)):
        start = map[:ind]
        end = map[ind:]
        start.reverse()

        failed = False
        for i in range(min(len(start), len(end))):
            if(start[i] != end[i]):
                failed = True
                break
        if(not failed):
            horizInd = ind

    vertInd = -1
    for ind in range(1,len(flipMap)):
        start = flipMap[:ind]
        end = flipMap[ind:]
        start.reverse()

        failed = False
        for i in range(min(len(start), len(end))):
            if(start[i] != end[i]):
                failed = True
                break
        if(not failed):
            vertInd = ind
    
    if(vertInd > horizInd):
        total += vertInd
    else:
        total += 100 * horizInd

print(total)