n = int(input())
arr = []
mem = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    mem.append([-float('inf')] * 3)
def longest_path(a, m):
    try:
        arr[a][m]
    except:
        return(0)
    if(a == n - 1 and m == n - 1):
        return(arr[n-1][n-1])
    if(mem[a][m] != -float('inf')):
        return(mem[a][m])
    path1 = longest_path(a, m+1)
    path2 = longest_path(a + 1, m)
    mem[a][m] = arr[a][m] + max(path1, path2)
    return(mem[a][m])
print(longest_path(0, 0))