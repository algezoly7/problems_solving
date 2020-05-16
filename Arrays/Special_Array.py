T = int(input())
for _ in range(0,T):
    result = -1
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n - 1):
        left = sum(arr[0:i])
        right = sum(arr[i + 1: n])
        if(left == right):
            result = i
            break
    print(result)