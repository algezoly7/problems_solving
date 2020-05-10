#for more informations copy this link: https://www.hackerrank.com/challenges/2d-array/problem

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
maximum = -10000
for i in range(4):
    for j in range(4):
        counter = sum(arr[i][j:j+3])
        counter += arr[i+1][j+1]
        counter += sum(arr[i+2][j:j+3])
        maximum = max(maximum, counter)
print(maximum)