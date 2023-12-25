from collections import defaultdict
from os import path

input = open('input.txt', 'r')
lines = input.readlines()

hailstones = []

for line in lines:
    line = line.strip().split(' @ ')
    pos = [int(x) for x in line[0].split(', ')]
    move = [int(x) for x in line[1].split(', ')]
    # print(line)
    # print(pos)
    # print(move)
    hailstones.append((pos, move))

def intersectTime(h1, h2):
    matr = []
    numCheck = 2
    # x, y, (soon z), then res
    for ind in range(numCheck):
        matr.append([-h1[1][ind], h2[1][ind], h1[0][ind] - h2[0][ind]])
    for ind in range(1, len(matr)):
        mult = - matr[ind][0] / matr[0][0]
        # print(mult)
        for subind in range(len(matr[ind])):
            matr[ind][subind] += matr[0][subind] * mult

    if(matr[len(matr)-1][numCheck-1] == 0):
        return None
    for ind in range(0, len(matr)-1):

        mult = - matr[ind][1] / matr[len(matr)-1][1]
        # print(mult)
        for subind in range(len(matr[ind])):
            matr[ind][subind] += matr[len(matr)-1][subind] * mult
    
    res = []
    for ind in range(2):
        res.append(matr[ind][-1] / matr[ind][ind])
    # print(matr)
    return res

total = 0
testArea = [200000000000000, 400000000000000]
for ind1 in range(len(hailstones)):
# for ind1 in range(1):
    for ind2 in range(ind1+1, len(hailstones)):
        # print(hailInd)
        hail1 = hailstones[ind1]
        hail2 = hailstones[ind2]
        # print(secInd)
        times = intersectTime(hail1, hail2)
        # print(times)
        if(times == None):
            continue
        pos = []
        for ind in range(2):
            pos.append(round(hail1[0][ind] + hail1[1][ind] * times[0], 3))
        # print(pos)
        

        failed = False
        for item in pos:
            if(not(testArea[0] <= item <= testArea[1])):
                failed = True
        
        if(failed):
            # print("FAILED")
            continue    

        for ind in range(2):
            if(hail1[1][ind] < 0):
                if(pos[ind] > hail1[0][ind]):
                    failed = True
            else:
                if(pos[ind] < hail1[0][ind]):
                    failed = True

            if(hail2[1][ind] < 0):
                if(pos[ind] > hail2[0][ind]):
                    failed = True
            else:
                if(pos[ind] < hail2[0][ind]):
                    failed = True
        if(failed):
            # print("FAILED")
            continue     
        total += 1
        # print()

print(total)

        