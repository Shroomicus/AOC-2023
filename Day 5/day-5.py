input = open('input2.txt', 'r')
lines = input.readlines()
seeds = [int(x) for x in lines[0][7:].split()]
lines = lines[2:]
print(seeds)

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

for i in range(len(seeds)):
    for map in maps:
        for moves in map:
            if(moves[1] <= seeds[i] <= moves[1]+moves[2]-1):
                seeds[i] = seeds[i] - moves[1] + moves[0]
                break

print(seeds)

print(min(seeds))