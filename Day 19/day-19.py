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

lines = lines[ind:]

total = 0
for line in lines:
    line = line.strip()
    line = line[1:len(line)-1].split(',')
    currKey = "in"

    lineData = {}
    val = 0
    for item in line:
        item = item.split('=')
        lineData[item[0]] = int(item[1])
        val += int(item[1])
    print(lineData)

    while(True):
        print(currKey)
        if(currKey == 'A'):
            total += val
            break
        if(currKey == 'R'):
            break
        for key in workflows[currKey]:
            print(key)
            if(key[0] == "default"):
                currKey = key[1]
                break
            if(key[1] == '<'):
                if(lineData[key[0]] < key[2]):
                    currKey = key[3]
                    break
            if(key[1] == '>'):
                if(lineData[key[0]] > key[2]):
                    currKey = key[3]
                    break
print(total)