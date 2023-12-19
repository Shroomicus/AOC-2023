from collections import defaultdict
from pathlib import Path

input = open('input2.txt', 'r')
lines = input.readlines()

workflows = defaultdict(list)

ind = 0
for line in lines:
    ind += 1
    line = line.strip()[:len(line)-2]
    if(line == ""):
        break
    line = line.split("{")
    line[1] = line[1].split(',')
    print(line)
    for path in line[1][:len(line[1])-1]:
        path = path.split(':')
        print(path)
        workflows[line[0]].append((path[0][0], path[0][1], int(path[0][2:]), path[1]))
    workflows[line[0]].append(("default", line[1][-1]))
    workflows[line[0]]

print()
for workflow in workflows:
    print(workflows[workflow])
print()

queue = [["in", []]]

flip = {
    ">": "<=",
    "<": ">="
}

total = 0
rejectTotal = 0
while(len(queue) > 0):
    curr = queue.pop(0)
    data = workflows[curr[0]]
    if(curr[0] == 'A' or curr[0] == 'R'):
        vals = {
            'x' : [1, 4000],
            'm' : [1, 4000],
            'a' : [1, 4000],
            's' : [1, 4000]
        }
        print(curr)
        for item in curr[1]:
            print("\t" + str(item))
            if(item[1] == '>='):
                vals[item[0]][0] = item[2]
            if(item[1] == '>'):
                vals[item[0]][0] = item[2]+1
            if(item[1] == '<='):
                vals[item[0]][1] = item[2]
            if(item[1] == '<'):
                vals[item[0]][1] = item[2]-1
        res = 1
        for val in vals:
            print(vals[val])
            res *= (vals[val][1] - vals[val][0]+1)
        if(curr[0] == 'A'):
            total += res
        if(curr[0] == 'R'):
            rejectTotal += res
        continue
    print()
    print(curr)
    print(data)
    alt = curr[1].copy()
    for item in data[:len(data)-1]:
        newList = alt.copy()
        newList.append(item[:3])
        # print(newList)
        # print(item[:3])
        queue.append((item[3], newList))
        alt.append((item[0], flip[item[1]], item[2]))
    queue.append([data[-1][1], alt])
    # break
print(total)
print(rejectTotal)
print(total + rejectTotal)
print(pow(4000, 4))
print(167409079868000)