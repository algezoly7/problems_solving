def binary_search():
    arr = list(map(int, input().split()))
    num = int(input())
    #just for sorted lists
    arr.sort()
    l = 0
    r = len(arr) - 1
    while(l <= r):
        mid = l + (r - l) // 2
        if(arr[mid] == num):
            return(mid)
        elif(arr[mid] < num):
            l = mid + 1
        else:
            r = mid - 1
    return(-1)
print(binary_search())
