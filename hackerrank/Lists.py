n = int(input())
arr = []
for i in range(n):
    brr = list(map(str, input().split()))
    if(brr[0] == "insert"):
        arr.insert(int(brr[1]), int(brr[2]))
    elif(brr[0] == "print"):
        print(arr)
    elif(brr[0] == "remove"):
        arr.remove(int(brr[1]))
    elif(brr[0] == "append"):
        arr.append(int(brr[1]))
    elif(brr[0] == "sort"):
        arr.sort()
    elif(brr[0] == "pop"):
        arr.pop()
    elif(brr[0] == "reverse"):
        arr.reverse()