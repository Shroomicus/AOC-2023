import math
input = open('input.txt', 'r')
lines = input.readlines()
inst = lines[0].replace('\n', '')

moves = {}

for line in lines[2:]:
    moves[line[0:3]] = (line[7:10], line[12:15])

starts = []
zNums = []
gaps = []
for i in moves:
    if(i[2] == 'A'):
        starts.append(i)
        zNums.append([])
        gaps.append([0])

moveNum = 0
done = False
while(not done):
    val = None
    done = True
    if(inst[moveNum % len(inst)] == "L"):
        val = 0
    else:
        val = 1
    for i in range(len(starts)):
        starts[i] = moves[starts[i]][val]
        if(starts[i][2] == 'Z'):
            zNums[i].append(moveNum)
            gaps[i].append(zNums[i][len(zNums[i])-1] - zNums[i][len(zNums[i])-2])
            print()
            for j in zNums:
                print(j)
            for j in gaps:
                print(j)
    for i in gaps:
        if len(i) < 3:
            done = False
    moveNum += 1

res = 1
for i in gaps:
    res = math.lcm(res, i[2])

print(res)