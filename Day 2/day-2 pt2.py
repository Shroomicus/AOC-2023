from turtle import color


input = open('input.txt', 'r')
lines = input.readlines()

def numCubes(set):
    data = set.split(", ")
    colorSets = {}
    for i in range(0, len(data)):
        colorSets[data[i].split(" ")[1]] = int(data[i].split(" ")[0])
    return colorSets

# print(numCubes(lines[0].split(": ")[1].split("; ")[0]))

total = 0
for i in range(0, len(lines)):
    line = lines[i].replace('\n', '').split(": ")[1].split("; ")
    max = [0, 0, 0]
    for set in line:
        colorSets = numCubes(set)
        if("red" in colorSets and colorSets["red"] > max[0]):
            max[0] = colorSets["red"]
        if("green" in colorSets and colorSets["green"] > max[1]):
            max[1] = colorSets["green"]
        if("blue" in colorSets and colorSets["blue"] > max[2]):
            max[2] = colorSets["blue"]
    total += max[0] * max[1] * max[2]

print(total)
