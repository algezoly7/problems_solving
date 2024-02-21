from collections import Counter

T = int(input())

for _ in range(T):

    n = int(input())
    arr = list(map(int, input().split()))

    count = Counter(arr)

    most_frequency = count.most_common(1)[0][1]
    limit = len(arr) - most_frequency
    ans = 0

    while(limit > 0):
        ans += most_frequency + 1
        limit -= most_frequency
        most_frequency = most_frequency * 2

    ans -= abs(limit)
    print(ans)
