input = open('input.txt', 'r')
Lines = input.readlines()
total = 0

def numAtChar(line, index):
    if(line[index].isnumeric()):
        return int(line[index])
    numDict = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for key in numDict:
        if(line[index:index+len(key)] == key):
            return numDict[key]
    return None
    

for line in Lines:
    first = False
    last = -1

    for index in range(0, len(line)):
        if(numAtChar(line, index) is not None):
            last = numAtChar(line, index)
            if(not first):
                total += 10 * numAtChar(line, index)
                first = True
    total += last

print(total)

