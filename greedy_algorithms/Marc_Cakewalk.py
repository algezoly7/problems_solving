#for more informations copy this link: https://www.hackerrank.com/challenges/marcs-cakewalk/problem
#Source: HackerRank
def Marc_Cakewalk():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    total = 0
    for i in range(n):
        total += 2**i * arr[i]
    return(total)
print(Marc_Cakewalk())