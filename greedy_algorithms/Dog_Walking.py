#for more informations copy this link: https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/dog-walking
#Source: HackerRank, IEEEXtreme 10.0

def Dog_Walking(n, k, arr):
    dif = n - k
    arr.sort()
    brr = []
    for i in range(1, n):
        brr.append(arr[i] - arr[i - 1])
    brr.sort()
    result = 0
    for i in range(dif):
        result += brr[i]
    return(result)

T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)
    print(Dog_Walking(n, k, arr))