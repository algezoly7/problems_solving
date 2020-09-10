#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/statistics-1

def sta():
    arr = list(map(int, input().split()))
    arr.pop(0)
    brr = []
    max_ = max(arr)
    min_ = min(arr)
    brr.append(str(min_))
    brr.append(str(max_))
    range_ = max_ - min_
    brr.append(str(range_))
    return(' '.join(brr))
t = int(input())
for _ in range(t):
    print(sta())