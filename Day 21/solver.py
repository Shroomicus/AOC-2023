p = 202300

e = 5817 + 5844 + 5816 + 5789
v = 7693
o = 7717
i = 27067
l = 980 + 970 + 981 + 980

vMult = 0
for ind in range(0, p//2):
    vMult += ((2 * ind)+ 1)*4
print(vMult)

oMult = 1
for ind in range(1, p//2+1):
    oMult += ((2 * (ind-1)))*4
print(oMult)

print(e + (v * vMult) + (o * oMult) + (i * (p - 1)) + (l * p))
