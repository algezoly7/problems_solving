#for more informations copy this link:https://www.hackerrank.com/contests/easyhack3/challenges/inverse-factorial-2/copy-from/1323996821
#EasyHack 3.0
def factorial():
    n = int(input())
    fac = 1
    i = 0
    while(fac < n):
        i += 1
        fac *= i
    return(i)
T = int(input())
for _ in range(T):
    print(factorial())