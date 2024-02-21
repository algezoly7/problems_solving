from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
crr = list(map(int, input().split()))

dictionary = defaultdict( lambda : 0)

for i in range(n):
    dictionary[brr[crr[i] - 1]] += 1

count = 0
for number in arr:
    count += dictionary[number]

print(count)