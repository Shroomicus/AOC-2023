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

    horizVals = []
    for ind in range(1,len(map)):
        horizVals.append([])
        start = map[:ind]
        end = map[ind:]
        start.reverse()

        failed = False
        for i in range(min(len(start), len(end))):
            if(start[i] != end[i]):
                horizVals[-1].append(i)
    print(horizVals)

    numDiffs = []
    for ind in range(len(horizVals)):
        numDiffs.append(0)
        if(len(horizVals[ind]) != 1):
            continue
        diff = horizVals[ind][0]
        for i in range(0, len(map[0])):
            if(map[ind+1+diff][i] != map[ind-diff][i]):
                numDiffs[-1] += 1
    print(numDiffs)

    horizInd = -1
    for i in range(len(numDiffs)):
        if(numDiffs[i] == 1):
            horizInd = i

    vertVals = []
    for ind in range(1,len(flipMap)):
        vertVals.append([])
        start = flipMap[:ind]
        end = flipMap[ind:]
        start.reverse()

        failed = False
        for i in range(min(len(start), len(end))):
            if(start[i] != end[i]):
                vertVals[-1].append(i)
    print(vertVals)

    numDiffs = []
    for ind in range(len(vertVals)):
        numDiffs.append(0)
        if(len(vertVals[ind]) != 1):
            continue
        diff = vertVals[ind][0]
        for i in range(0, len(flipMap[0])):
            if(flipMap[ind+1+diff][i] != flipMap[ind-diff][i]):
                numDiffs[-1] += 1
    print(numDiffs)

    vertInd = -1
    for i in range(len(numDiffs)):
        if(numDiffs[i] == 1):
            vertInd = i
    

    print(horizInd+1)
    print(vertInd+1)
    
    if(vertInd > horizInd):
        total += (vertInd+1)
    else:
        total += 100 * (horizInd+1)

print(total)