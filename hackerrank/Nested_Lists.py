def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    return sub_li

n = int(input())
arr = []

for _ in range(n):
    x = input()
    y = float(input())
    arr.append([x, y])
Sort(arr)

brr = []
now = arr[0][1]
flag = False
for i in range(1, n):
    if(flag == False and now == arr[i][1]):
        continue
    else:
        flag = True
        brr.append(arr[i][0])
        now = arr[i][1]
        if(i + 1 >= n or now != arr[i+1][1]):
            break
brr.sort()
for i in brr:
    print(i)