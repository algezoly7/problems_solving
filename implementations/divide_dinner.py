#for more informations copy this two links:
#https://www.hackerrank.com/contests/easyhack4/challenges/divide-dinner
#https://github.com/alifaki077/easyhack4-solutions/tree/master/divide-dinner
 
def divisble(num, x):
    i = 0
    while(num % x == 0):
        i += 1
        num = num / x
    return(num,i)

ln = {2:0, 3:0, 5:0}
lm = {2:0, 3:0, 5:0}
n, m = map(int, input().split())

n,ln[2] = divisble(n, 2)
n,ln[3] = divisble(n, 3)
n,ln[5] = divisble(n, 5)

m,lm[2] = divisble(m, 2)
m,lm[3] = divisble(m, 3)
m,lm[5] = divisble(m, 5)

if(n != m):
    print(-1)
else:
    print(abs(ln[2] - lm[2]) + abs(ln[3] - lm[3]) + abs(ln[5] - lm[5]))