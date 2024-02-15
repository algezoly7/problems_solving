k = int(input())

max_ = 0
now = 0
for _ in range(k):
    a, b = map(int, input().split())
    now += b
    now -= a
    max_ = max(max_, now)
print(max_)