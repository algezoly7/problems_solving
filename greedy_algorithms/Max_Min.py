#for more informations copy this link: https://www.hackerrank.com/challenges/angry-children/problem
#Source: HackerRank
def Max_Min():
    n = int(input())
    k = int(input())
    k = k - 1
    arr = []
    for i in range(n):
        num = int(input())
        arr.append(num)
    arr.sort()
    minimum = float('inf')
    for i in range(k, n):
        difference = arr[i] - arr[i -k]
        minimum = min(difference, minimum)
    return(minimum)
print(Max_Min())