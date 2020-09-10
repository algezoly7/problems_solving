#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/magical-counting-machine

# Let c, h, o be the number of carbon, hydrogen and oxygen atoms respectively
c, h, o = map(int, input().split())
co = (o - (h/2))/2
glu = (c - co)/6
ho = ((h/2) - (6 *glu))
print(int(ho), int(co), int(glu))