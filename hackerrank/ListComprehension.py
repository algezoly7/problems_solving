x = int(input())
y = int(input())
z = int(input())
n = int(input())
arr = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i + j + k == n):
                continue
            arr.append([i, j, k])
print(arr)