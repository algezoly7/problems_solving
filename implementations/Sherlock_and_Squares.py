#for more informations copy this link : https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import math

def squares(a, b):
    a = math.ceil(math.sqrt(a))
    b = math.floor(math.sqrt(b))
    return(int(b - a) + 1)
if __name__ == '__main__':

    q = int(input())

    for _ in range(q):
        
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(result)
