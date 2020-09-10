#for more informations copy this link: https://www.hackerrank.com/challenges/halloween-sale/problem

import math

def howManyGames(p, d, m, s):
    counter = 0
    while(p > m and s > p):
        s = s - p
        p = p - d
        counter += 1
    if(s > p):
        counter += math.floor(s / m)
    return(counter)

if __name__ == '__main__':

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
