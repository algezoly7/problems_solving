T = int(input())
import math
for _ in range(T):
    n, a, b = map(int, input().rstrip().split())
    reminder = b % a
    if(reminder == 0):
        print(n // a)
    else:
        gcd = math.gcd(a, b)
        if(gcd == 1):
            print((n // a) + (n // b) - (n // (a * b)))
        else:
            print(((n // a) + ((n // b) / 2)))