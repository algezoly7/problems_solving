def iceCream_trip():
    m = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if(i != j):
                answer = arr[i] + arr[j]
                if(answer == m):
                    a = i + 1
                    b = j + 1
                    break
    brr = [a, b]
    brr.sort()
    print(brr[0], brr[1])
T = int(input())
for _ in range(T):
    iceCream_trip()