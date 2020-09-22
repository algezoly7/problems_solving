#for more informations copy this link: https://www.hackerrank.com/challenges/greedy-florist/problem
#Source: HackerRank
import math
def Greedy_Florist():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    prize = 0
    for i in range(1, n + 1):
        multipli_cons = math.ceil(i/k)
        prize = prize + multipli_cons * arr[-i]
    return(prize)
print(Greedy_Florist())