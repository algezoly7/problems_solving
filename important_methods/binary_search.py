#Binary_search
import math
arr = list(map(int, input().split()))
arr.sort()
n = int(input())
ans = -1
i = 0
j = len(arr) - 1
while(i <= j):
    mid = math.floor((i + j) / 2)
    if(arr[mid] == n):
        ans = mid
        break
    elif(arr[mid] > n):
        j = mid - 1
    elif(arr[mid] < n):
        i = mid + 1
print(ans)