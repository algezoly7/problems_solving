n = int(input())
arr = list(map(int, input().split()))
max_ = max(arr)
arr.remove(max_)
while(len(arr) > 0):
    if(max_ != max(arr)):
        print(max(arr))
        break
    else:
        arr.remove(max_)