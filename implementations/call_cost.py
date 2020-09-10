#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/call-cost

m, s = map(int, input().split())
total = m * 60 + s
if(total < 300):
    coast = total * 1.5
else:
    coast = 300 * 1.5 + (total - 300)
print(coast)