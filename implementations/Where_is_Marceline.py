#for more informations copy this link: https://www.hackerrank.com/contests/easyhack4-warmup/challenges/where-is-marceline/copy-from/1323613501
import math
def where():
    n = int(input())
    if(n == 1):
        a = 1
        b = 0
    elif(n % 2 == 1):
        if((n + 1) % 4 == 0):
            a = -(math.ceil(n / 2))
        else:
            a = math.ceil(n / 2)
        n = n - 1
        if(n % 4 == 0):
            b = -(math.ceil(n / 2))
        else:
            b = math.ceil(n / 2) + 1
    else:
        if(n % 4 == 0):
            b = -(math.ceil(n / 2))
        else:
            b = math.ceil(n / 2) + 1
        n = n - 1
        if((n + 1) % 4 == 0):
            a = -(math.ceil(n / 2))
        else:
            a = math.ceil(n / 2)
    print(a, b)
T = int(input())
for _ in range(T):
    where()