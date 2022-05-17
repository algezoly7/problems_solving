#for more informations copy this link: https://www.hackerrank.com/contests/easyhack3/challenges/human-readable-numbers
#EasyHack 3.0
n = list(input())
arr = []
module = len(n) % 3
for i in range(module):
    a = n.pop(0)
    arr.append(a)
a = len(n) // 3 - 1
for i in range(3, len(n) + a, 4):
    n.insert(i, ',')
if(module != 0):
    n.insert(0, ',')
    print(''.join(arr) + ''.join(n))
else:
    print(''.join(n))