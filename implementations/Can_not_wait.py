#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/cant-wait/problem

def shakes():
    n, w = map(int, input().split())
    time = (n * (n - 1)) / 2 * w
    return(round(time))
T = int(input())
for _ in range(T):
    print(shakes())