#for more informations copy this link: https://www.hackerrank.com/challenges/array-left-rotation/problem

n, d = map(int, input().split())
arr = list(input().rstrip().split())
for _ in range(d):
    b = arr.pop(0)
    arr.append(b)
print(' '.join(arr))