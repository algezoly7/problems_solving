#for more informations copy this link: https://www.hackerrank.com/challenges/circular-array-rotation/problem

nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))

for _ in range(k):
    temp = a[len(a) - 1]
    a.pop(len(a) - 1)
    a.insert(0, temp)

for _ in range(q):
    queries_item = int(input())
    print(a[queries_item])
