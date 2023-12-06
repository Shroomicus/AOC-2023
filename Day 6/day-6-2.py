from math import sqrt, floor

input = open('input.txt', 'r')
lines = input.readlines()

a = -1
b = int("".join(lines[0][5:].split()))
c = -int("".join(lines[1][10:].split()))

one = floor((-b - sqrt(pow(b, 2) - 4*a*c)) / (2* a))
two = floor((-b + sqrt(pow(b, 2) - 4*a*c)) / (2* a))

print(one - two)