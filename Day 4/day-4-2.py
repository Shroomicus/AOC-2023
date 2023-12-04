import re


input = open('input2.txt', 'r')
lines = input.readlines()

cardsWon = []
cardNums = []

for line in lines:
    cardData = line.replace('\n', '').split(": ")[1].split(" | ")
    cardData[0] = cardData[0].split()
    cardData[1] = cardData[1].split()

    val = 0
    for num in cardData[1]:
        if(num in cardData[0]):
            val += 1
    cardsWon.append(val)
    cardNums.append(1)

print(str(cardsWon) + "\n")

total = 0

for index in range(0, len(cardNums)):
    total += cardNums[index]
    for won in range(1, cardsWon[index]+1):
        cardNums[index + won] += cardNums[index]

print(total)