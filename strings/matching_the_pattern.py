#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/pattern-matching-2

a, n = map(str, input().split())
n = int(n)
arr = list(map(str, input().split()))
brr = []
for i in arr:
    tracker = False
    if(len(i) != len(a)):
        pass
    else:
        tracker = True
        for j in range(len(i)):
            if(a[j] == 'X'):
                pass
            else:
                if(a[j] != i[j]):
                    tracker = False
                    break
    if(tracker == True):
        brr.append(i)
print(' '.join(brr))