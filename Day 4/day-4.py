input = open('input2.txt', 'r')
lines = input.readlines()

total = 0
for line in lines:
    cardData = line.replace('\n', '').split(": ")[1].split(" | ")
    cardData[0] = cardData[0].split()
    cardData[1] = cardData[1].split()

    val = 0
    for num in cardData[1]:
        if(num in cardData[0]):
            if(val == 0):
                val = 1
            else:
                val *= 2
    # print(val)
    total += val
print(total)