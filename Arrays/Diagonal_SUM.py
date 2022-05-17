#for more informations copy this link: https://www.hackerrank.com/contests/easyhack4/challenges/diagonal-sum-5-1/copy-from/1323861273
#another solution that i didn't went into: https://github.com/alifaki077/easyhack4-solutions/blob/master/diagonal-sum/solution.py
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

next_dia = 0
for i in reversed(range(n)):
    m = 0
    sum_ = arr[m][i]
    for _ in range(next_dia):
        m += 1
        i += 1
        sum_ += arr[m][i]
    next_dia += 1
    print(sum_)

next_dia = n - 2
for j in range(1, n):
    m = 0
    sum_ = arr[j][m]
    for _ in range(next_dia):
        m += 1
        j += 1
        sum_ += arr[j][m]
    next_dia -= 1
    print(sum_)