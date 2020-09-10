#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/staircase-printing/problem

n = int(input())
arr = input()
for i in range(1, n + 1):
    brr = arr[0 : i]
    print(brr)