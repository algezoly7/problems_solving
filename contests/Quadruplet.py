# from collections import defaultdict
# n, target = map(int, input().split())
# arr = list(map(int, input().split()))

# dictionary = defaultdict(lambda : [])

# for i in range(n):
#     for j in range(n):
#         if(i != j):
#             dictionary[target - arr[i] - arr[j]] = [i, j]

# target = True
# for i in range(n):
#     for j in range(n):
#         if(i != j):
#             if(dictionary[arr[i] + arr[j]] != [] and i not in dictionary[arr[i] + arr[j]] and j not in dictionary[arr[i] + arr[j]]):
#                 print(" ".join([str(i + 1), str(j + 1), str(dictionary[arr[i] + arr[j]][0] + 1), str(dictionary[arr[i] + arr[j]][1] + 1)]))
#                 target = False
#                 break

#     if(target == False):
#         break

# if(target == True):
#     print("IMPOSSIBLE")

n, target = map(int, input().split())
arr = list(map(int, input().split()))

store = {}

for i, num in enumerate(arr):

  for j in range(i + 1, len(arr)):
    total = arr[i] + arr[j]
    if target - total in store:
      print(*store[target - total], i + 1, j + 1)
      exit()

  for j in range(i):
    total = arr[i] + arr[j]
    store[total] = (i + 1, j + 1)

print("IMPOSSIBLE")