#for more informations copy this link: https://www.hackerrank.com/contests/easyhack3/challenges/rabbit-path
#Source: HackerRank/EasyHack3
n = int(input())
arr = list(map(int, input().split()))
memo = [0] * n
def fun(i):
    if(i >= n):
        return(0)
    if(memo[i] != 0):
        return(memo[i])
    memo[i] = arr[i] + max(fun(i + 2), fun(i + 3))
    return(memo[i])
print(fun(0))
#khalid elmadani code