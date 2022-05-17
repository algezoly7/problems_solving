def add():
    n, m = map(int, input().split())
    arr = [0] * (n + 1)
    for _ in range(m):
        a, b, k = map(int, input().split())
        arr[a] += k
        if(b + 1 <= n):
            arr[b + 1] -= k
    max_ = 0
    sum_ = 0
    for i in arr:
        sum_ += i
        max_ = max(sum_ , max_)
    return(max_)
print(add())