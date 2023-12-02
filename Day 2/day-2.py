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
    isValid = True
    for set in line:
        colorSets = numCubes(set)
        if("red" in colorSets and colorSets["red"] > 12):
            isValid = False
        if("green" in colorSets and colorSets["green"] > 13):
            isValid = False
        if("blue" in colorSets and colorSets["blue"] > 14):
            isValid = False
    if(isValid):
        total += i + 1

print(total)
