#for more informations copy this link: https://www.hackerrank.com/challenges/permutation-equation/problem
n = int(input())
p = list(map(int, input().split()))
for x in range(1, n+1):
    for i in range(n):
        if(x == p[i]):
            for y in range(n):
                if(i+1 == p[y]):
                    print(y + 1)
                    break
            break
